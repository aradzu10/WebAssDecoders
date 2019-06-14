#include <string>
#include <ctype.h>
#include "substitution_cipher.h"

using namespace std;

bool SubstitutionCipher::cipher(string input, string old_alphabet, string new_alphabet, string& output)
{
	output = "";
	const int inputLen = input.size();

	if (old_alphabet.size() != new_alphabet.size())
		return false;

	for (auto i = 0; i < inputLen; ++i)
	{
		 int old_char_index = old_alphabet.find(input[i]);

		if (old_char_index >= 0)
			output += new_alphabet[old_char_index];
		else
			output += input[i];
	}
	return true;
}

bool SubstitutionCipher::encrypt(string input, string plainAlphabet, string cipherAlphabet, string &output)
{
	return cipher(input, plainAlphabet, cipherAlphabet, output);
}

bool SubstitutionCipher::decrypt(string input, string plainAlphabet, string cipherAlphabet, string &output)
{
	return cipher(input, cipherAlphabet, plainAlphabet, output);
}