from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from staffapp.models import MyUser

class Zone(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    #zone_posts

class Post(models.Model):
    author = models.CharField(max_length=255)
    user = models.ForeignKey(MyUser, related_name="posts", on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    website = models.URLField(max_length=500, blank=True, default='')
    image = models.ImageField(null=True, upload_to='profile_pic', default='default.jpg')   #arguments to be changed
    zone = models.ForeignKey(Zone, related_name="zone_posts", on_delete=models.SET_NULL, null=True)
    sitspot = models.CharField(max_length=255)
    flagged=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    #tags
    #comments


class Tag(models.Model):
    type = models.CharField(max_length=255)
    name =  models.CharField(max_length=255)
    scientific_name = models.TextField()
    description = models.TextField()
    diet = models.TextField()
    habitat = models.TextField()
    terrestrial_biome = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tagged = models.ManyToManyField(Post, related_name='tags')
    def __str__(self):
        return self.name

class Comment(models.Model):
    content = models.TextField()
    author = models.TextField()
    user = models.ForeignKey(MyUser,related_name='comments', on_delete=models.SET_NULL, null=True, blank=True)
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    flagged=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    icon = models.PositiveSmallIntegerField(default=1)
    def __str__(self):
        return f"comment id {self.id} by {self.author}"
    #replies

class Reply(models.Model):
    content = models.TextField()
    author = models.TextField()
    user = models.ForeignKey(MyUser,related_name='replies', on_delete=models.SET_NULL, null=True, blank=True)
    website = models.URLField(max_length=500, blank=True, default='')
    comment = models.ForeignKey(Comment, related_name='replies', on_delete=models.CASCADE)
    flagged=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"reply id {self.id} by {self.author}"

# Create your models here.

# Creating a new record
#     ClassName.objects.create(field1="value for field1", field2="value for field2", etc.)
# Reading existing records
#     Methods that return a single instance of a class
#         ClassName.objects.first() - gets the first record in the table
#         ClassName.objects.last() - gets the last record in the table
#         ClassName.objects.get(id=1) - gets the record in the table with the specified id
#             this method will throw an error unless only and exactly one record matches the query
#     Methods that return a list of instances of a class
#         ClassName.objects.all() - gets all the records in the table
#         ClassName.objects.filter(field1="value for field1", etc.) - gets any records matching the query provided
#         ClassName.objects.exclude(field1="value for field1", etc.) - gets any records not matching the query provided
# Updating an existing record
#     c = ClassName.objects.get(id=1)
#     c.field_name = "some new value for field_name"
#     c.save()
# Deleting an existing record
#     c = ClassName.objects.get(id=1)
#     c.delete()
# Other helpful methods
#     Displaying records
#         ClassName.objects.get(id=1).__dict__ - shows all the values of a single record as a dictionary
#         ClassName.objects.all().values() - shows all the values of a QuerySet (i.e. multiple instances)
#     Ordering records
#         ClassName.objects.all().order_by("field_name") - orders by field provided, ascending
#         ClassName.objects.all().order_by("-field_name") - orders by field provided, descending

#     CharField
#         Any text that a user may enter. This has one required parameter, max_length, that is the maximum length of text that can be saved.
#     TextField
#         Like a CharField, but with no maximum length. Your user could copy the entire text of the Harry Potter series into the field and it would save in the database correctly.
#     IntegerField
#         Holds an integer value
#     FloatField
#         Holds a float value; this is good for numbers with potentially varying numbers of decimal places
#     DecimalField
#         This is a good field for a number with a fixed number of decimal places, like currency. There are 2 required parameters: max_digits refers to the total number of digits (before and after the decimal place), and decimal_places refers to how many decimal places.
#     BooleanField
#         Holds a boolean value
#     DateTimeField
#         Used for a combination of a specific date and time. This field can take two very useful optional parameters. Setting the auto_now_add argument to True adds the current date/time when an object is created. Setting auto_now=True automatically updates any time the object is modified.


# one to many:
#     class Author(models.Model):
#         name = models.CharField(max_length=255)
#         created_at = models.DateTimeField(auto_now_add=True)
#         updated_at = models.DateTimeField(auto_now=True)
#     class Book(models.Model):
#         title = models.CharField(max_length=255)
#         author = models.ForeignKey(Author, related_name="books", on_delete = models.CASCADE)
#         created_at = models.DateTimeField(auto_now_add=True)
#         updated_at = models.DateTimeField(auto_now=True)
#     some_book.author	# returns the Author instance associated with this book
#     this_author = Author.objects.get(id=2)
#     books = Book.objects.filter(author=this_author)
#     this_author.books.all()



# Many to many:
#     class Book(models.Model):
#         title = models.CharField(max_length=255)
#         created_at = models.DateTimeField(auto_now_add=True)
#         updated_at = models.DateTimeField(auto_now=True)
#     class Publisher(models.Model):
#         name = models.CharField(max_length=255)
#         books = models.ManyToManyField(Book, related_name="publishers")
#         created_at = models.DateTimeField(auto_now_add=True)
#         updated_at = models.DateTimeField(auto_now=True)
#     add to each other
#         this_book = Book.objects.get(id=4)	# retrieve an instance of a book
#         this_publisher = Publisher.objects.get(id=2)	# retrieve an instance of a publisher
            
#         # 2 options that do the same thing:
#         this_publisher.books.add(this_book)		# add the book to this publisher's list of books
#         # OR
#         this_book.publishers.add(this_publisher)	# add the publisher to this book's list of publishers
#     remove relation:
#         this_book = Book.objects.get(id=4)	# retrieve an instance of a book
#         this_publisher = Publisher.objects.get(id=2)	# retrieve an instance of a publisher
            
#         # 2 options that do the same thing:
#         this_publisher.books.remove(this_book)		# remove the book from this publisher's list of books
#         # OR
#         this_book.publishers.remove(this_publisher)	# remove the publisher from this book's list of publishers
#     reverse lookup
#         this_publisher.books.all()	# get all the books this publisher is publishing
#         this_book.p ublishers.all()	# get all the publishers for this book