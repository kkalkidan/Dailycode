/***
@Question
Determine whether there exists a one-to-one ch
aracter mapping from one string s1 to another s2.

For example, given s1 = abc and s2 = bcd, return 
true since we can map a to b, b to c, and c to d.

Given s1 = foo and s2 = bar, return false since the
o cannot map to two characters.
***/ 
#include <iostream>
#include <map>
#include <cassert>
bool is_onetoone(std::string s1, std::string s2){
    if(s1.length() != s2.length()) return false;
    std::map<char, char> mapping;
    for(int i=0; i< s1.length(); i++){
       auto check = mapping.insert({s1[i], s2[i]});
    // checks if the mapping already exists, 
    // if it exists, next it checks if the value of the
    // existing mapping equals the value of the new mapping 
       if(!check.second && 
           check.first->second != s2[i]) {
           return false;
       }
    } return true;
}

int main() {

    std::string s1("abc"), s2("bcd"), s3("foo"), s4("bar"), s5("baa");

    assert(is_onetoone(s1, s2) == true);
    assert(is_onetoone(s3, s4) == false);
    assert(is_onetoone(s3, s5) == true);

    return 0;
}

/*** 
@Solution

For all char in string s1, there exists a unique mapping in string s2
for all char (c1 E s1) and (c2 E s1), if (c1 == c2) then s2(c1) == s2(c2)

***/ 