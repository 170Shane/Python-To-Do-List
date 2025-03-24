contents = ['This is some random content for filename 1',
            'This is some random content for filename 2',
            'This is some random content for filename 3']

filenames = ['filename1.txt','filename2.txt','filename3.txt']

authors = ['Peter','John','James']

for filename, content, author in zip(filenames, contents, authors):
    with open(f"files\\{filename}", 'w') as file:
        file.write(f"{content}\n\n\nAuthored by: {author}") # Write the content to the file
        file.close() # Close the file