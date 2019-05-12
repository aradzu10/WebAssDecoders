class SubsetituionCipher 
{
    private:
    static bool cipher(string input, string oldAlphabet, string newAlphabet, string &output);

    public:
    static bool encrypt(string input, string plainAlphabet, string cipherAlphabet, string &output);
    static bool decrypt(string input, string plainAlphabet, string cipherAlphabet, string &output);

}