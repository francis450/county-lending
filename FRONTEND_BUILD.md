# DCP Management Frontend Build Guide

## Quick Build & Deploy

Use the automated build script:

```bash
cd /home/frappeuser/frappe-bench/apps/dcp_management
./build_frontend.sh
```

This script will:
1. Build the Vue.js frontend
2. Automatically update `portal.html` with the new asset filenames
3. Tell you when to run `bench restart`

## Manual Build Process

If you need to build manually:

```bash
# 1. Build the frontend
cd dcp_management/public/frontend
npm run build

# 2. Copy the built index.html to portal.html
cd ../../www
echo "{% raw %}" > portal.html
cat ../public/frontend/dist/index.html >> portal.html
echo "{% endraw %}" >> portal.html

# 3. Clear cache and restart
cd /home/frappeuser/frappe-bench
bench clear-cache
bench restart
```

## Development Mode

For development with hot reload:

```bash
cd dcp_management/public/frontend
npm run dev
```

Then access at `http://localhost:5173` (Note: this won't have access to Frappe backend APIs)

## Why This Process?

Vite builds assets with content-based hashes in filenames (e.g., `index-ABC123.js`). These hashes change with each build. Since Frappe serves static HTML from `www/portal.html`, we need to update it with the new filenames after each build.

The `build_frontend.sh` script automates this process.

## Troubleshooting

### Assets not loading (404 errors)
- **Cause**: `portal.html` has old asset filenames
- **Fix**: Run `./build_frontend.sh` or manually update `portal.html`

### Browser showing old version
- **Cause**: Browser cache
- **Fix**: Hard refresh (Ctrl+Shift+R or Cmd+Shift+R) or clear browser cache

### Changes not appearing
1. Clear Frappe cache: `bench clear-cache`
2. Clear browser cache
3. Restart bench: `bench restart`
