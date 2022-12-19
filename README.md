# CS5700, Project 1: Simple Client

# Approach 

My general approach for this project was that I started off using the non-TLS server to make sure that I had the correct concepts implemented. Later on, I had to switch to using the TLS server so I had to refactor my code accordingly. In general, my approach involved a step-by-step or little-by-little mindset where I gradually implemented different functionalities starting off with simply being able to read messages from the server to sending the correct results back to it and ending the program and writing the secret flag to file. 
## Challenges faced
The main challenges I faced in this project are as follows: 
1. Understanding the differences between TLS and non-TLS in terms of implementation ( For example, I always read the entire message with just one recv call when communicating with the non-TLS server, but that was not the case when I tested on the TLS server)
2. Getting to parse the command line arguments and adding shebang in my client Python script
3. Debugging errors such as why I was not reading entire messages from the server 
4. Refreshing implementation of parsing mathematical expressions 
## Testing Overview 
In order to test that my code and logic are correct, I underwent several iterations of code. During that process, I had many print statements across the code to make sure that the tokens produced where correct, and I also had to manually check that I was producing the correct results. Once I was satisfied that my code was behaving in the appropriate way, I had to test for the some of the edge cases (getting an empty message, invalid id), and handle those cases appropriately. I also had to test ( using print statements as well) that I was receiving the entire message from the server. 