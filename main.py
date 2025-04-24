
counter= 0

print('---Welcome to the Counter Application---')
print('You can stop the counter by typing "stop"')
print('Press Enter to Increment Counter')
print()
while True:
    if input() == 'stop':
        break
    counter += 1
    print(counter)

print('Thank you for Using Our Counter Application')
print("Download version 12.0.1")
