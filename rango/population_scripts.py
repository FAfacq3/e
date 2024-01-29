from myapp.models import MyModel

def populate():
    # Create instances of MyModel
    my_instance = MyModel(name="Example", description="Sample description")
    my_instance.save()

if __name__ == '__main__':
    print("Populating the database...")
    populate()
    print("Populating complete!")
