def main():
    file = input("File name: ").strip().lower()

    extension = file.split(".")
    print(getFileType(extension[1]))
    
def getFileType(fileExtension: str):
    fileType = ""

    match fileExtension:
        case "jpg" | "jpeg":
            fileType = f"image/jpeg"
        case "gif" | "jpg" | "jpeg" | "png":
            fileType = f"image/{fileExtension}"
        case "pdf":
            fileType = "application/pdf"
        case "txt":
            fileType = "text/plain"
        case "zip":
            fileType = "application/zip"
        case _:
            fileType = "application/octet-stream"

    return fileType

main()