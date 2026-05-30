import { createServer } from "node:http";
import { readFile } from "node:fs/promises";
import { extname, join, normalize } from "node:path";
import { fileURLToPath } from "node:url";

const root = fileURLToPath(new URL(".", import.meta.url));
const port = Number(process.env.PORT || 4173);
const host = process.env.HOST || "127.0.0.1";
const maxJsonBodyBytes = 64 * 1024;

const contentTypes = {
  ".html": "text/html; charset=utf-8",
  ".css": "text/css; charset=utf-8",
  ".js": "text/javascript; charset=utf-8",
  ".json": "application/json; charset=utf-8",
  ".png": "image/png",
  ".jpg": "image/jpeg",
  ".jpeg": "image/jpeg",
  ".svg": "image/svg+xml",
  ".mp4": "video/mp4"
};

function sendJson(response, status, payload) {
  response.writeHead(status, { "Content-Type": "application/json; charset=utf-8" });
  response.end(JSON.stringify(payload, null, 2));
}

class HttpError extends Error {
  constructor(status, message) {
    super(message);
    this.status = status;
  }
}

async function readJsonBody(request) {
  let body = "";
  let bytes = 0;

  for await (const chunk of request) {
    bytes += chunk.length;
    if (bytes > maxJsonBodyBytes) {
      throw new HttpError(413, "Request body too large");
    }
    body += chunk.toString("utf8");
  }

  if (!body.trim()) return {};

  try {
    return JSON.parse(body);
  } catch {
    throw new HttpError(400, "Invalid JSON body");
  }
}

function safeStaticPath(urlPath) {
  const cleanPath = urlPath === "/" ? "/index.html" : decodeURIComponent(urlPath);
  const resolved = normalize(join(root, cleanPath));
  if (!resolved.startsWith(root)) return null;
  return resolved;
}

const server = createServer(async (request, response) => {
  try {
    const url = new URL(request.url || "/", `http://${request.headers.host || `${host}:${port}`}`);

    if (request.method === "POST" && url.pathname === "/api/pixverse/generate") {
      const body = await readJsonBody(request);
      const jobId = body.job?.job_id || "pv_local_mock";
      sendJson(response, 200, {
        ok: true,
        status: "submitted",
        video_id: `mock_${jobId}_${Date.now()}`,
        trace_id: `trace_${Date.now()}`,
        message: "Local mock only. No PixVerse API key was used or exposed."
      });
      return;
    }

    if (request.method === "GET" && url.pathname.startsWith("/api/pixverse/status/")) {
      const videoId = url.pathname.split("/").pop();
      sendJson(response, 200, {
        ok: true,
        status: "ready",
        video_id: videoId,
        output_url: "",
        message: "Mock status ready. Wire real PixVerse polling server-side later."
      });
      return;
    }

    if (request.method !== "GET" && request.method !== "HEAD") {
      sendJson(response, 405, { error: "Method not allowed" });
      return;
    }

    const staticPath = safeStaticPath(url.pathname);
    if (!staticPath) {
      sendJson(response, 403, { error: "Forbidden" });
      return;
    }

    const data = await readFile(staticPath);
    response.writeHead(200, {
      "Content-Type": contentTypes[extname(staticPath)] || "application/octet-stream"
    });
    response.end(request.method === "HEAD" ? undefined : data);
  } catch (error) {
    if (error?.code === "ENOENT") {
      response.writeHead(404, { "Content-Type": "text/plain; charset=utf-8" });
      response.end("Not found");
      return;
    }
    if (error?.status) {
      sendJson(response, error.status, { error: error.message });
      return;
    }
    response.writeHead(500, { "Content-Type": "text/plain; charset=utf-8" });
    response.end(error.message);
  }
});

server.listen(port, host, () => {
  console.log(`PaperMotion Workbench site running at http://${host}:${port}`);
});
