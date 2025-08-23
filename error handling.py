

"""
Error Handling Lab
This program asks the user for a filename and tries to read it.
It demonstrates try/except/else/finally blocks for error handling.
"""

def read_file(filename):
    try:
        # Try to open the file in read mode
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
            print("\n📖 File Content:\n")
            print(content)
    except FileNotFoundError:
        print("❌ Error: That file does not exist.")
    except PermissionError:
        print("❌ Error: You don’t have permission to read this file.")
    except IsADirectoryError:
        print("❌ Error: That is a directory, not a file.")
    except UnicodeDecodeError:
        print("❌ Error: File could not be decoded (not plain text).")
    except OSError as e:
        print(f"❌ OS Error: {e}")
    else:
        print("✅ File read successfully.")
    finally:
        print("ℹ Attempt finished.\n")

def main():
    while True:
        filename = input("Enter filename to read (or 'q' to quit): ")
        if filename.lower() == "q":
            print("👋 Exiting program.")
            break
        read_file(filename)

if _name_ == "_main_":
    main()