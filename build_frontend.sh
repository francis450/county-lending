#!/bin/bash
# Script to update portal.html with the latest build assets

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
FRONTEND_DIR="$SCRIPT_DIR/dcp_management/public/frontend"
WWW_DIR="$SCRIPT_DIR/dcp_management/www"

echo "Building frontend..."
cd "$FRONTEND_DIR" && npm run build

if [ $? -eq 0 ]; then
    echo "Build successful! Updating portal.html..."
    
    # Copy the built index.html to portal.html with Jinja raw tags and CSRF token
    echo "{% raw %}" > "$WWW_DIR/portal.html"
    
    # Add everything except closing body and html tags
    sed '/<\/body>/d; /<\/html>/d' "$FRONTEND_DIR/dist/index.html" >> "$WWW_DIR/portal.html"
    
    echo "{% endraw %}" >> "$WWW_DIR/portal.html"

    # Add CSRF token script before closing body tag
    cat >> "$WWW_DIR/portal.html" << 'EOF'
    <script>
      // Set CSRF token from cookie for API calls
      window.csrf_token = '{{ frappe.session.csrf_token }}';
      if (window.csrf_token) {
        document.cookie = 'csrf_token=' + encodeURIComponent(window.csrf_token) + '; path=/';
      }
    </script>
  </body>
</html>
EOF
    
    echo "✓ portal.html updated successfully!"
    echo "Run 'bench restart' to apply changes."
else
    echo "✗ Build failed!"
    exit 1
fi
