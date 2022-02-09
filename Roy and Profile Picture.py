def validate_profile_pic(width, height):
    if width < minimum_length or height < minimum_length:
        print ('UPLOAD ANOTHER')
    elif width == height:
        print ('ACCEPTED')
    elif width > minimum_length or height > minimum_length:
        print('CROP IT')

minimum_length = int(input())
no_of_photos = int(input())

i = 0
while i < no_of_photos:
    width, height = map(int,input().split())
    validate_profile_pic (width,height)
    i += 1