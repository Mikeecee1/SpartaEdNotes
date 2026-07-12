#app interface for S3 operations

#import from s3_operations.py for live connections to AWS S3
#import from s3_operations_test.py for testing purposes without AWS S3 connection

from s3_operations_test import *

#displays all buckets
def show_buckets():
    """Display all buckets."""
    buckets = list_buckets()

    if not buckets:
        print("No buckets found.")
        return

    print("\nAvailable Buckets:")
    for i, bucket in enumerate(buckets, start=1):
        print(f"{i}. {bucket['Name']}")

#Create a new bucket
def create_new_bucket():
    """Prompt user for a bucket name and create it."""
    bucket_name = input("Enter new bucket name: ")
    create_bucket(bucket_name)

#remove bucket
def remove_bucket():
    """Prompt user for bucket name and delete it."""
    bucket_name = input("Enter bucket name to delete: ")
    delete_bucket(bucket_name)

# allows selection of a bucket and displays its contents
def browse_bucket():
    """Select a bucket and display its contents."""

    buckets = list_buckets()

    if not buckets:
        print("No buckets found.")
        return

    print("\nAvailable Buckets:")
    for i, bucket in enumerate(buckets, start=1):
        print(f"{i}. {bucket['Name']}")

    try:
        choice = int(input("\nSelect bucket: "))
        selected_bucket = buckets[choice - 1]["Name"]

    except (ValueError, IndexError):
        print("Invalid selection.")
        return

    objects = list_objects(selected_bucket)

    print(f"\nContents of {selected_bucket}")

    if not objects:
        print("Bucket is empty.")
    else:
        for obj in objects:
            print(obj["Key"])


def main():

    while True:

        print("\n===== S3 Manager =====")
        print("1. List Buckets")
        print("2. Create Bucket")
        print("3. Browse Bucket")
        print("4. Delete Bucket")
        print("5. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            show_buckets()

        elif choice == "2":
            create_new_bucket()

        elif choice == "3":
            browse_bucket()

        elif choice == "4":
            remove_bucket()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")

        input("\nPress Enter to return to the menu...")


if __name__ == "__main__":
    main()