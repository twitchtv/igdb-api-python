#! /bin/sh

SRC_DIR="src/igdb"
DST_DIR="src/igdb"

echo "Fetching latest protocol buffers from IGDB API"
curl https://api.igdb.com/v4/igdbapi.proto -o "${SRC_DIR}/igdbapi.proto"

echo "Compiling protocol buffers"
protoc -I=$SRC_DIR --python_out=$DST_DIR $SRC_DIR/igdbapi.proto

echo "Update complete"
