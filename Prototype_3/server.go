package main

import (
	"encoding/json"
	"net/http"
	"os"
	"path/filepath"
	"strings"
)

const WORKSPACE = "workspace"

// this function makes sure that the  user provided file path stays within workspace
func safePath(p string) (string, error) {
	full := filepath.Join(WORKSPACE, p)
	abs, _ := filepath.Abs(full)
	root, _ := filepath.Abs(WORKSPACE)

	if !strings.HasPrefix(abs, root) {
		return "", http.ErrAbortHandler
	}
	//else return the abs path
	return abs, nil

}

//

func createFolder(w http.ResponseWriter, r *http.Request) {
	var data struct {
		Path string
	}
	json.NewDecoder(r.Body).Decode(&data)

	full, err := safePath(data.Path)
	if err != nil {
		http.Error(w, "blocked", 403)
		return
	}
	// this is the else block
	os.MkdirAll(full, 0755)
	w.Write([]byte("Folder created"))
}

func writefile(w http.ResponseWriter, r *http.Request) {
	var data struct {
		Path    string
		Content string
	}
	json.NewDecoder(r.Body).Decode(&data)

	full, err := safePath(data.Path)

	if err != nil {
		http.Error(w, "blocked", 403)
		return
	}

	//else run this block if no error
	os.MkdirAll(filepath.Dir(full), 0755)
	os.WriteFile(full, []byte(data.Content), 0644)
	w.Write([]byte("file written"))
}

func main() {
	os.MkdirAll(WORKSPACE, 0755)

	http.HandleFunc("/create_folder", createFolder)
	http.HandleFunc("/write_file", writefile)

	http.ListenAndServe(":8080", nil)
}
