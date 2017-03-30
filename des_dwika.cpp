// BLOCK CIPHER ENCRYPTION
// MODE COUNTER
#include<iostream>
#include<string>
#include<bitset>
#include<math.h>
#include<stdio.h>
#include<stdlib.h>

using namespace std;

// FUNGSI ASCII TO BINARY
string asciiToBinary(string input)
{
    string output="", temp;
    for(int i=0; i<input.size(); i++)
    {
        bitset<8> bin(input[i]);
        temp = bin.to_string();
        output.append(temp);
    }
    return output;
}

// FUNGSI HEX TO BINARY
string hexToBinary(string input)
{
    string output="";
    for(int i=0; i<input.size(); i++)
    {
        switch(input[i])
        {
            case '0' : output.append("0000"); break;
            case '1' : output.append("0001"); break;
            case '2' : output.append("0010"); break;
            case '3' : output.append("0011"); break;
            case '4' : output.append("0100"); break;
            case '5' : output.append("0101"); break;
            case '6' : output.append("0110"); break;
            case '7' : output.append("0111"); break;
            case '8' : output.append("1000"); break;
            case '9' : output.append("1001"); break;
            case 'A' : output.append("1010"); break;
            case 'B' : output.append("1011"); break;
            case 'C' : output.append("1100"); break;
            case 'D' : output.append("1101"); break;
            case 'E' : output.append("1110"); break;
            case 'F' : output.append("1111"); break;

        }
    }
    return output;
}

// FUNGSI BINARY TO HEX
string binaryToHex(string input)
{
    string output="", temp;
    for(int i=0;i<input.size();i+=4)
    {
        temp = input.substr(i,4);
        if (!temp.compare("0000")){output.append("0");}
        else if (!temp.compare("0001")){output.append("1");}
        else if (!temp.compare("0010")){output.append("2");}
        else if (!temp.compare("0011")){output.append("3");}
        else if (!temp.compare("0100")){output.append("4");}
        else if (!temp.compare("0101")){output.append("5");}
        else if (!temp.compare("0110")){output.append("6");}
        else if (!temp.compare("0111")){output.append("7");}
        else if (!temp.compare("1000")){output.append("8");}
        else if (!temp.compare("1001")){output.append("9");}
        else if (!temp.compare("1010")){output.append("A");}
        else if (!temp.compare("1011")){output.append("B");}
        else if (!temp.compare("1100")){output.append("C");}
        else if (!temp.compare("1101")){output.append("D");}
        else if (!temp.compare("1110")){output.append("E");}
        else if (!temp.compare("1111")){output.append("F");}
    }
    return output;
}

// FUNGSI HET TO ASCII
string hexToAscii(string input)
{
    string output, temp;
    char chr;
    for(int i=0; i<input.size(); i+=2)
    {
        temp = input.substr(i,2);
        chr = (char) (int)strtol(temp.c_str(), NULL, 16);
        output.push_back(chr);
    }
    return output;
}

// FUNGSI SHIFT LEFT
string shiftleft(string input)
{
    string output = input;
    for(int i=0; i<input.size(); i++)
    {
        if(i==input.size()-1) output[i]=input[0];
        else output[i]=input[i+1];
    }
    return output;
}

// FUNGSI PERMUTASI
string permutate(string input, int table[], int tablesize)
{
    string output="", temp="";
    for(int i=0; i<tablesize; i++)
    {
        temp = input[table[i]-1];
        output.append(temp);
    }
    return output;
}

// FUNGSI XOR
string xorr(string input1, string input2, int insize)
{
//    cout << insize << endl;
    string output="";
    for(int i=0; i<insize; i++)
    {
        if(input1[i] == input2[i]) output.append("0");
        else output.append("1");
    }
    return output;
}

// FUNGSI SBOX
string sbox(string input, int table[4][16])
{
//    cout << "input = " << input << endl;
    string kolom="",baris="", output="";
    int kolomi=0, barisi=0, outputi;
    kolom.append(input.substr(1,4));
    baris.append(input.substr(0,1));
    baris.append(input.substr(5,1));
    for(int i=kolom.size()-1 , j=0; i>=0; i--, j++)
    {
        kolomi += (pow(2,j) * ((int)kolom[i]-48));
    }
    for(int i=baris.size()-1 , j=0; i>=0; i--, j++)
    {
        barisi+= (pow(2,j) * ((int)baris[i]-48));
    }
    outputi = table[barisi][kolomi];
    output = bitset<4> (outputi).to_string();
//    cout << kolom << " = " << kolomi << endl;
//    cout << baris << " = " << barisi << endl;
//    cout << "outputi = " << outputi << endl;
//    cout << "output = " << output << endl;
    return output;
}

// FUNGSI F
string f(string input1, string input2)
{
    int E[48] ={32,1,2,3,4,5,
                4,5,6,7,8,9,
                8,9,10,11,12,13,
                12,13,14,15,16,17,
                16,17,18,19,20,21,
                20,21,22,23,24,25,
                24,25,26,27,28,29,
                28,29,30,31,32,1};
    int s[8][4][16]=
    {
        {14,4,13,1,2,15,11,8,3,10,6,12,5,9,0,7,
        0,15,7,4,14,2,13,1,10,6,12,11,9,5,3,8,
        4,1,14,8,13,6,2,11,15,12,9,7,3,10,5,0,
        15,12,8,2,4,9,1,7,5,11,3,14,10,0,6,13}
        ,
        {15,1,8,14,6,11,3,4,9,7,2,13,12,0,5,10,
        3,13,4,7,15,2,8,14,12,0,1,10,6,9,11,5,
        0,14,7,11,10,4,13,1,5,8,12,6,9,3,2,15,
        13,8,10,1,3,15,4,2,11,6,7,12,0,5,14,9}
        ,
        {10,0,9,14,6,3,15,5,1,13,12,7,11,4,2,8,
        13,7,0,9,3,4,6,10,2,8,5,14,12,11,15,1,
        13,6,4,9,8,15,3,0,11,1,2,12,5,10,14,7,
        1,10,13,0,6,9,8,7,4,15,14,3,11,5,2,12}
        ,
        {7,13,14,3,0,6,9,10,1,2,8,5,11,12,4,15,
        13,8,11,5,6,15,0,3,4,7,2,12,1,10,14,9,
        10,6,9,0,12,11,7,13,15,1,3,14,5,2,8,4,
        3,15,0,6,10,1,13,8,9,4,5,11,12,7,2,14}
        ,
        {2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9,
        14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6,
        4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14,
        11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3}
        ,
        {12,1,10,15,9,2,6,8,0,13,3,4,14,7,5,11,
        10,15,4,2,7,12,9,5,6,1,13,14,0,11,3,8,
        9,14,15,5,2,8,12,3,7,0,4,10,1,13,11,6,
        4,3,2,12,9,5,15,10,11,14,1,7,6,0,8,13}
        ,
        {4,11,2,14,15,0,8,13,3,12,9,7,5,10,6,1,
        13,0,11,7,4,9,1,10,14,3,5,12,2,15,8,6,
        1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2,
        6,11,13,8,1,4,10,7,9,5,0,15,14,2,3,12}
        ,
        {13,2,8,4,6,15,11,1,10,9,3,14,5,0,12,7,
        1,15,13,8,10,3,7,4,12,5,6,11,0,14,9,2,
        7,11,4,1,9,12,14,2,0,6,10,13,15,3,5,8,
        2,1,14,7,4,10,8,13,15,12,9,0,3,5,6,11}
    };
    int p[32] = {16,7,20,21,
                29,12,28,17,
                1,15,23,26,
                5,18,31,10,
                2,8,24,14,
                32,27,3,9,
                19,13,30,6,
                22,11,4,25};
    string output="";
    input1 = permutate(input1, E, sizeof(E)/sizeof(E[0]));
    input1 = xorr(input1, input2, 48);
    for(int i=0;i<8;i++)
    {
//        b[i]=sbox(input1.substr(i*6,6),s[i]);
        output.append(sbox(input1.substr(i*6,6),s[i]));
    }
//    cout << input1 << endl;
//    cout << output << endl;
    output = permutate(output, p, sizeof(p)/sizeof(p[0]));
//    cout << "output = " << output << endl;
    return output;
}

string des(string input, string key, int mode)
{
//    cout << "input = " << input <<endl;
//    cout << "key = " << key <<endl;
//    cout << "MODE = " << mode <<endl;
    string  m = "",
            k[17] = "",
            c[17] = "",
            d[17] = "",
            l[17] = "",
            r[17] = "",
            output_binary = "",
            output = "",
            temp = "";
    int PC1[56] =  {57,49,41,33,25,17,9,
                    1,58,50,42,34,26,18,
                    10,2,59,51,43,35,27,
                    19,11,3,60,52,44,36,
                    63,55,47,39,31,23,15,
                    7,62,54,46,38,30,22,
                    14,6,61,53,45,37,29,
                    21,13,5,28,20,12,4};
    int PC2[48] =  {14,17,11,24,1,5,
                    3,28,15,6,21,10,
                    23,19,12,4,26,8,
                    16,7,27,20,13,2,
                    41,52,31,37,47,55,
                    30,40,51,45,33,48,
                    44,49,39,56,34,53,
                    46,42,50,36,29,32};
    int IP[64] =   {58,50,42,34,26,18,10,2,
                    60,52,44,36,28,20,12,4,
                    62,54,46,38,30,22,14,6,
                    64,56,48,40,32,24,16,8,
                    57,49,41,33,25,17,9,1,
                    59,51,43,35,27,19,11,3,
                    61,53,45,37,29,21,13,5,
                    63,55,47,39,31,23,15,7};
    int IP1[64] =  {40,8,48,16,56,24,64,32,
                    39,7,47,15,55,23,63,31,
                    38,6,46,14,54,22,62,30,
                    37,5,45,13,53,21,61,29,
                    36,4,44,12,52,20,60,28,
                    35,3,43,11,51,19,59,27,
                    34,2,42,10,50,18,58,26,
                    33,1,41,9,49,17,57,25};
//    cout << "Message in binary :\n> " << input << endl;
//    cout << "Key in binary : \n> " << key << endl;
    k[0] = permutate(key, PC1, sizeof(PC1)/sizeof(PC1[0]));
//    cout << "k[0] :\n> " << k[0] <<endl;
    c[0] = k[0].substr(0,k[0].size()/2);
    d[0] = k[0].substr(k[0].size()/2,k[0].size()/2);
//    cout<< "c[0] = " << c[0]<<endl;
//    cout<< "d[0] = " << d[0]<<endl;
    for(int i=1; i<17; i++)
    {
        if(i==1 || i==2 || i==9 || i==16)
        {
            c[i] = shiftleft(c[i-1]);
            d[i] = shiftleft(d[i-1]);
        } else
        {
            c[i] = shiftleft(c[i-1]);
            c[i] = shiftleft(c[i]);
            d[i] = shiftleft(d[i-1]);
            d[i] = shiftleft(d[i]);
        }
//        cout << c[i] << " : " << d[i] <<endl;
        k[i].append(c[i]);
        k[i].append(d[i]);
        k[i] = permutate(k[i], PC2, sizeof(PC2)/sizeof(PC2[0]));
//        cout << "k[" << i << "] = " << k[i] <<endl;
    }
    m = permutate(input, IP, sizeof(IP)/sizeof(IP[0]));
    l[0] = m.substr(0,m.size()/2);
    r[0] = m.substr(m.size()/2,m.size()/2);
//    cout << l[0] << endl;
//    cout << r[0] << endl;
//    cout << xorr(l[0],r[0],32) << endl;
    for(int i=1; i<17; i++)
    {
        l[i] = r[i-1];
        if(mode == 1)
            r[i] = xorr(l[i-1],f(r[i-1],k[i]),32);
        else
            r[i] = xorr(l[i-1],f(r[i-1],k[17-i]),32);
    }
//    for(int i=0; i<17; i++)
//    {
//        cout << l[i] << endl;
//        cout << r[i] << endl;
//        cout << endl;
//    }
//    cout << endl;
//    cout << r[16] << endl;
//    cout << l[16] << endl;
    output_binary.append(r[16]);
    output_binary.append(l[16]);
//    cout << "Output binary = " << output_binary << endl;
    output_binary = permutate(output_binary, IP1, sizeof(IP1)/sizeof(IP1[0]));
//    cout << "Output binary = " << output_binary << endl;
 //NGUBAH KE HEX
    output = binaryToHex(output_binary);
//    cout << "Encrypted Message :\n> " << output << endl;
    return output;
}

int main()
{
    string input, key, output="", output_ascii="", ctr_binary, temp, c, p;
    int mode=-1, ctr=0;
    cout << "=====BLOCK CIPHER ENCRYPTION WITH COUNTER MODE=====" << endl;
    cout << "Modes : " << endl;
    cout << "1. Encrypt" << endl;
    cout << "2. Decrypt" << endl;
    cout << "Choose what to do (1/2) :\n> ";
    while(1)
    {
        cin >> mode;
        getchar();
        if(mode==1||mode==2)break;
        else cout << "Wrong mode. Try again :\n> ";
    }
    if(mode ==1)
    {
        cout << "Word to work with :\n> ";
        getline(cin, input, '\n');
    }else
    {
        cout << "Hex to work with :\n> ";
        getline(cin, input, '\n');
    }
    cout << "Key to use (Exactly 8 characters):\n> ";
    getline(cin, key, '\n');
    while(key.size() != 8)
    {
        cout << "Wrong key. Try again (Exactly 8 characters):\n> ";
        getline(cin, key, '\n');
    }
//    cout << "input = '" << input << "'" <<endl;

    if(mode == 1)
    {
        while(input.size()%8!=0)
        {
            input.append(" ");
        }
        input = asciiToBinary(input);
    }
    else
    {
        input = hexToBinary(input);
    }

    key = asciiToBinary(key);
//    output = des(input, key, mode);
//    cout << "DES BIASA -> Result :\n> ";
//    cout << output << endl;
//    cout << "input size = " << input.size() << endl;
    for(int i=0; i<input.size(); i+=64, ctr++)
    {
//        cout << "ctr = " << ctr << endl;
        ctr_binary = bitset<64>(ctr).to_string(); //to binary
//        cout << "ctr binary = " << ctr_binary << endl;
//        cout << "key = " << key << endl;
        temp = des(ctr_binary,key,1);

//        cout << "temp = " << temp << endl;
        temp = hexToBinary(temp);
//        cout << "temp = " << temp << endl;

        p = input.substr(i,64);
//        cout << "p = " << p << endl;

        c = xorr(p,temp,64);
//        cout << "c = " << c << endl;
        c = binaryToHex(c);
        output.append(c);
    }
    if(mode == 1)
    {
        cout << "CTR Result:\n> " << output;
    }else
    {
        output_ascii = hexToAscii(output);
        cout << "CTR Result:\n> " << output_ascii;
    }

}
