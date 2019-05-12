#include <string>
#include <ctype.h>

using namespace std;

class SubsetituionCipher {
    private:
    static bool cipher(string input, string oldAlphabet, string newAlphabet, string &output)
    {
    	output = "";
    	int inputLen = input.size();

    	if (oldAlphabet.size() != newAlphabet.size())
    		return false;

    	for (int i = 0; i < inputLen; ++i)
    	{
    		int oldCharIndex = oldAlphabet.find(tolower(input[i]));

    		if (oldCharIndex >= 0)
    			output += isupper(input[i]) ? toupper(newAlphabet[oldCharIndex]) : newAlphabet[oldCharIndex];
    		else
    			output += input[i];
    	}
    	return true;
    }

    public:
    static bool encrypt(string input, string plainAlphabet, string cipherAlphabet, string &output)
    {
    	return cipher(input, plainAlphabet, cipherAlphabet, output);
    }

    static bool decrypt(string input, string plainAlphabet, string cipherAlphabet, string &output)
    {
    	return cipher(input, cipherAlphabet, plainAlphabet, output);
    }
}