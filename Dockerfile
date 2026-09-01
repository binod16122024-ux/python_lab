# Static nginx image serving the practical-labs site (no backend needed —
# every lab runs its Python in-browser via Pyodide).
FROM nginx:alpine

COPY nginx.conf /etc/nginx/nginx.conf
COPY . /usr/share/nginx/html

EXPOSE 80
