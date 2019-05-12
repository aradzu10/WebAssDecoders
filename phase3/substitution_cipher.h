#pragma once
#include <string>

using namespace std;

class SubstitutionCipher 
{
	static bool cipher(string input, string old_alphabet, string new_alphabet, string& output);
public:
	static bool encrypt(string input, string plainAlphabet, string cipherAlphabet, string &output);
	static bool decrypt(string input, string plainAlphabet, string cipherAlphabet, string &output);
};
