#include <stdio.h>
#include <string.h>

char* getXOR(char txt1[], char txt2[])
{
    int i;
    // int size = (strlen(txt2) > strlen(txt1)) ? strlen(txt1) : strlen(txt2);
    // null terminators due to xor give wrong string length
    int size = 42;
    for (i = 0; i < size; i++)
    {
        char temp = txt1[i] ^ txt2[i];
        txt1[i] = temp;
    }
    return txt1;
}

char* getRandom(char ptxt[], char rand[], int iv)
{
    for (int i = 0; i < iv; ++i)
    {
        ptxt = getXOR(ptxt, rand);
    }
    return ptxt;
}

int main()
{
    char key1[42] = "gnu-strings-is-convenient-dont-you-think?";
    char key2[42] = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa";
    char key3[42] = "<REDACTED>";

    char* pass1 = getRandom(key1, key2, 5);
    char* pass2 = getRandom(key1, key3, 3);
    char* pass3 = getRandom(key1, key2, 7);
    char* pass4 = getRandom(key1, key3, 2);
    printf("%s\n", pass4);

    return 0;
}