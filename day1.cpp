#include <iostream>
#include <cassert>

/***
@Question 
* Given a string, return the first recurring character 
* in it,or null if there is no recurring character.
* For example, given the string "acbbac", return "b".
* Given the string "abcdef", return null.
 ***/
using namespace std;

char recurring(string word){
    char characters[word.length()];

    for(int i=0; i< word.length(); i++){
       for(int j =0; j < i; j++){
           if(word[i] == characters[j]){
               return word[i];
           } 
       }characters[i] = word[i];
    }
    return '\0';
}

int main(){
     assert('b' == recurring("abbaa"));
     assert('\0' == recurring("ab"));
}