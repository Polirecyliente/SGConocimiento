/*
    Regex
*/

//T// Regex stands for Regular expressions

//T// regex notation /regex/
var regex1 = /^[a-z\s]+$/;

var str1 = 'first word third word';

//T// boolean match stringVar.match(regexVar)
if(str1.match(regex1))
{
    console.log("Match1");
}

//T// replace with replace(), flags g global, i case insensitive
str2 = str1.replace(/word/gi,'term');
console.log(str2);