import validators

url = input('Enter url')
r = validators.url(url)

if isinstance(r, validators.ValidationFailure):
    print('False')
else:
    print('True')


if __name__ == '__main__':
    print('')
