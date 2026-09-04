from composite import Folder
from leaf import File


def main() -> None:
    root = Folder("Root")

    documents = Folder("Documents")
    images = Folder("Images")

    documents.add(File("Resume.pdf", 450))
    documents.add(File("Project.docx", 180))

    images.add(File("Vacation.jpg", 2500))
    images.add(File("Profile.png", 780))

    backup = Folder("Backup")
    backup.add(File("backup.zip", 5000))

    documents.add(backup)

    root.add(documents)
    root.add(images)

    root.display()


if __name__ == "__main__":
    main()