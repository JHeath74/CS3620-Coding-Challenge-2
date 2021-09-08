#Part3

file = open("Demo.txt", 'w')

file.write("Can you Hear Me Now?" + "\n");

file.close();

file = open("Demo.txt", 'r');
content = file.read();

print(content);

file.close();

file = open("Demo.txt", 'a')
file.write("Nope, I can't hear you");
file.close();

file = open("Demo.txt", 'r');
content = file.read();
print(content);

file.close();