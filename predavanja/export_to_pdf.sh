#!/bin/bash

if [[ $# -ne 1 ]]; then
    echo "One argument expected (the name of the slidev .md file without extension)" >&2
    exit 2
fi

echo "Running slidev export ..."
pnpm slidev export $1.md
echo "Running GhostScript converter ..."
gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/printer -dNOPAUSE -dQUIET -dBATCH -sOutputFile=output.pdf $1.pdf
echo "Finalizing ..."
mv output.pdf $1.pdf
echo "Done."