# Generated from d:/PPL/BTL1/initial/src/main/minigo/parser/MiniGo.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,48,516,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,1,0,5,0,84,8,0,10,0,12,0,87,9,0,1,0,1,0,1,1,1,1,1,1,1,
        1,1,1,1,1,3,1,97,8,1,1,2,1,2,1,2,3,2,102,8,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,3,2,113,8,2,1,3,1,3,1,3,1,3,1,3,1,4,1,4,3,4,122,
        8,4,1,4,1,4,1,4,3,4,127,8,4,1,4,1,4,3,4,131,8,4,1,4,1,4,5,4,135,
        8,4,10,4,12,4,138,9,4,1,4,3,4,141,8,4,1,4,1,4,1,4,1,5,1,5,1,5,1,
        5,1,5,4,5,151,8,5,11,5,12,5,152,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,
        5,6,163,8,6,10,6,12,6,166,9,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,3,
        7,176,8,7,1,8,1,8,3,8,180,8,8,1,9,1,9,1,9,4,9,185,8,9,11,9,12,9,
        186,1,9,1,9,1,10,1,10,1,11,1,11,1,11,1,11,1,11,5,11,198,8,11,10,
        11,12,11,201,9,11,1,11,1,11,1,11,1,12,1,12,1,12,3,12,209,8,12,1,
        12,1,12,3,12,213,8,12,1,12,1,12,1,13,1,13,1,13,5,13,220,8,13,10,
        13,12,13,223,9,13,1,14,1,14,1,14,5,14,228,8,14,10,14,12,14,231,9,
        14,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,4,
        16,245,8,16,11,16,12,16,246,1,17,1,17,3,17,251,8,17,1,17,1,17,1,
        17,3,17,256,8,17,1,18,1,18,1,18,1,18,4,18,262,8,18,11,18,12,18,263,
        1,18,1,18,1,18,1,18,1,18,1,18,5,18,272,8,18,10,18,12,18,275,9,18,
        1,18,1,18,1,18,1,18,1,18,1,18,1,18,5,18,284,8,18,10,18,12,18,287,
        9,18,1,18,1,18,4,18,291,8,18,11,18,12,18,292,1,18,1,18,1,19,1,19,
        1,19,1,19,4,19,301,8,19,11,19,12,19,302,1,19,1,19,1,19,1,19,1,19,
        5,19,310,8,19,10,19,12,19,313,9,19,1,19,1,19,1,20,1,20,1,20,3,20,
        320,8,20,1,20,1,20,1,21,1,21,1,21,5,21,327,8,21,10,21,12,21,330,
        9,21,1,22,1,22,1,22,1,22,1,23,1,23,1,23,3,23,339,8,23,1,23,1,23,
        1,24,1,24,1,24,5,24,346,8,24,10,24,12,24,349,9,24,1,25,1,25,1,25,
        1,25,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,3,26,363,8,26,1,27,
        1,27,1,27,3,27,368,8,27,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,28,
        5,28,378,8,28,10,28,12,28,381,9,28,1,28,3,28,384,8,28,1,28,1,28,
        1,28,1,28,1,28,1,28,5,28,392,8,28,10,28,12,28,395,9,28,1,28,3,28,
        398,8,28,3,28,400,8,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,
        29,1,29,1,29,1,29,3,29,414,8,29,1,30,1,30,1,30,1,31,1,31,1,31,1,
        31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,
        31,1,31,1,31,1,31,3,31,439,8,31,1,32,1,32,3,32,443,8,32,1,33,1,33,
        1,34,1,34,1,34,1,35,1,35,1,35,1,36,1,36,3,36,455,8,36,1,36,1,36,
        1,37,1,37,1,37,3,37,462,8,37,1,37,1,37,1,37,1,38,1,38,1,38,1,38,
        5,38,471,8,38,10,38,12,38,474,9,38,1,38,1,38,1,39,1,39,1,39,1,39,
        1,39,1,39,1,39,1,39,1,39,1,39,1,39,1,39,1,39,1,39,1,39,1,39,1,39,
        1,39,3,39,496,8,39,1,39,1,39,1,39,1,39,1,39,1,39,1,39,1,39,1,39,
        5,39,507,8,39,10,39,12,39,510,9,39,1,40,1,40,3,40,514,8,40,1,40,
        0,1,78,41,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,
        40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,0,
        3,2,0,27,27,37,37,2,0,14,14,17,18,2,0,26,26,42,42,548,0,85,1,0,0,
        0,2,96,1,0,0,0,4,112,1,0,0,0,6,114,1,0,0,0,8,119,1,0,0,0,10,145,
        1,0,0,0,12,157,1,0,0,0,14,170,1,0,0,0,16,179,1,0,0,0,18,184,1,0,
        0,0,20,190,1,0,0,0,22,192,1,0,0,0,24,205,1,0,0,0,26,216,1,0,0,0,
        28,224,1,0,0,0,30,234,1,0,0,0,32,240,1,0,0,0,34,250,1,0,0,0,36,261,
        1,0,0,0,38,300,1,0,0,0,40,316,1,0,0,0,42,323,1,0,0,0,44,331,1,0,
        0,0,46,335,1,0,0,0,48,342,1,0,0,0,50,350,1,0,0,0,52,362,1,0,0,0,
        54,367,1,0,0,0,56,399,1,0,0,0,58,413,1,0,0,0,60,415,1,0,0,0,62,438,
        1,0,0,0,64,442,1,0,0,0,66,444,1,0,0,0,68,446,1,0,0,0,70,449,1,0,
        0,0,72,452,1,0,0,0,74,458,1,0,0,0,76,466,1,0,0,0,78,495,1,0,0,0,
        80,513,1,0,0,0,82,84,3,2,1,0,83,82,1,0,0,0,84,87,1,0,0,0,85,83,1,
        0,0,0,85,86,1,0,0,0,86,88,1,0,0,0,87,85,1,0,0,0,88,89,5,0,0,1,89,
        1,1,0,0,0,90,97,3,52,26,0,91,97,3,8,4,0,92,97,3,10,5,0,93,97,3,12,
        6,0,94,97,3,22,11,0,95,97,3,30,15,0,96,90,1,0,0,0,96,91,1,0,0,0,
        96,92,1,0,0,0,96,93,1,0,0,0,96,94,1,0,0,0,96,95,1,0,0,0,97,3,1,0,
        0,0,98,99,5,1,0,0,99,101,5,37,0,0,100,102,3,16,8,0,101,100,1,0,0,
        0,101,102,1,0,0,0,102,103,1,0,0,0,103,104,5,17,0,0,104,105,3,78,
        39,0,105,106,3,80,40,0,106,113,1,0,0,0,107,108,5,1,0,0,108,109,5,
        37,0,0,109,110,3,16,8,0,110,111,3,80,40,0,111,113,1,0,0,0,112,98,
        1,0,0,0,112,107,1,0,0,0,113,5,1,0,0,0,114,115,5,19,0,0,115,116,5,
        37,0,0,116,117,3,16,8,0,117,118,5,20,0,0,118,7,1,0,0,0,119,121,5,
        2,0,0,120,122,3,6,3,0,121,120,1,0,0,0,121,122,1,0,0,0,122,123,1,
        0,0,0,123,124,5,37,0,0,124,126,5,19,0,0,125,127,3,26,13,0,126,125,
        1,0,0,0,126,127,1,0,0,0,127,128,1,0,0,0,128,130,5,20,0,0,129,131,
        3,16,8,0,130,129,1,0,0,0,130,131,1,0,0,0,131,132,1,0,0,0,132,136,
        5,21,0,0,133,135,3,52,26,0,134,133,1,0,0,0,135,138,1,0,0,0,136,134,
        1,0,0,0,136,137,1,0,0,0,137,140,1,0,0,0,138,136,1,0,0,0,139,141,
        3,72,36,0,140,139,1,0,0,0,140,141,1,0,0,0,141,142,1,0,0,0,142,143,
        5,22,0,0,143,144,3,80,40,0,144,9,1,0,0,0,145,146,5,1,0,0,146,150,
        5,37,0,0,147,148,5,23,0,0,148,149,5,35,0,0,149,151,5,24,0,0,150,
        147,1,0,0,0,151,152,1,0,0,0,152,150,1,0,0,0,152,153,1,0,0,0,153,
        154,1,0,0,0,154,155,3,16,8,0,155,156,3,80,40,0,156,11,1,0,0,0,157,
        158,5,3,0,0,158,159,5,37,0,0,159,160,5,4,0,0,160,164,5,21,0,0,161,
        163,3,14,7,0,162,161,1,0,0,0,163,166,1,0,0,0,164,162,1,0,0,0,164,
        165,1,0,0,0,165,167,1,0,0,0,166,164,1,0,0,0,167,168,5,22,0,0,168,
        169,3,80,40,0,169,13,1,0,0,0,170,171,5,37,0,0,171,172,3,16,8,0,172,
        175,1,0,0,0,173,176,5,26,0,0,174,176,3,80,40,0,175,173,1,0,0,0,175,
        174,1,0,0,0,176,15,1,0,0,0,177,180,3,18,9,0,178,180,3,20,10,0,179,
        177,1,0,0,0,179,178,1,0,0,0,180,17,1,0,0,0,181,182,5,23,0,0,182,
        183,5,35,0,0,183,185,5,24,0,0,184,181,1,0,0,0,185,186,1,0,0,0,186,
        184,1,0,0,0,186,187,1,0,0,0,187,188,1,0,0,0,188,189,3,20,10,0,189,
        19,1,0,0,0,190,191,7,0,0,0,191,21,1,0,0,0,192,193,5,3,0,0,193,194,
        5,37,0,0,194,195,5,5,0,0,195,199,5,21,0,0,196,198,3,24,12,0,197,
        196,1,0,0,0,198,201,1,0,0,0,199,197,1,0,0,0,199,200,1,0,0,0,200,
        202,1,0,0,0,201,199,1,0,0,0,202,203,5,22,0,0,203,204,3,80,40,0,204,
        23,1,0,0,0,205,206,5,37,0,0,206,208,5,19,0,0,207,209,3,26,13,0,208,
        207,1,0,0,0,208,209,1,0,0,0,209,210,1,0,0,0,210,212,5,20,0,0,211,
        213,3,16,8,0,212,211,1,0,0,0,212,213,1,0,0,0,213,214,1,0,0,0,214,
        215,3,80,40,0,215,25,1,0,0,0,216,221,3,28,14,0,217,218,5,25,0,0,
        218,220,3,28,14,0,219,217,1,0,0,0,220,223,1,0,0,0,221,219,1,0,0,
        0,221,222,1,0,0,0,222,27,1,0,0,0,223,221,1,0,0,0,224,229,5,37,0,
        0,225,226,5,25,0,0,226,228,5,37,0,0,227,225,1,0,0,0,228,231,1,0,
        0,0,229,227,1,0,0,0,229,230,1,0,0,0,230,232,1,0,0,0,231,229,1,0,
        0,0,232,233,3,16,8,0,233,29,1,0,0,0,234,235,5,6,0,0,235,236,5,37,
        0,0,236,237,5,17,0,0,237,238,3,78,39,0,238,239,3,80,40,0,239,31,
        1,0,0,0,240,244,5,37,0,0,241,242,5,23,0,0,242,243,5,35,0,0,243,245,
        5,24,0,0,244,241,1,0,0,0,245,246,1,0,0,0,246,244,1,0,0,0,246,247,
        1,0,0,0,247,33,1,0,0,0,248,251,5,37,0,0,249,251,3,32,16,0,250,248,
        1,0,0,0,250,249,1,0,0,0,251,252,1,0,0,0,252,255,5,7,0,0,253,256,
        5,37,0,0,254,256,3,32,16,0,255,253,1,0,0,0,255,254,1,0,0,0,256,35,
        1,0,0,0,257,258,5,23,0,0,258,259,3,78,39,0,259,260,5,24,0,0,260,
        262,1,0,0,0,261,257,1,0,0,0,262,263,1,0,0,0,263,261,1,0,0,0,263,
        264,1,0,0,0,264,265,1,0,0,0,265,266,3,16,8,0,266,267,5,21,0,0,267,
        268,5,21,0,0,268,273,3,78,39,0,269,270,5,25,0,0,270,272,3,78,39,
        0,271,269,1,0,0,0,272,275,1,0,0,0,273,271,1,0,0,0,273,274,1,0,0,
        0,274,276,1,0,0,0,275,273,1,0,0,0,276,277,5,22,0,0,277,290,1,0,0,
        0,278,279,5,25,0,0,279,280,5,21,0,0,280,285,3,78,39,0,281,282,5,
        25,0,0,282,284,3,78,39,0,283,281,1,0,0,0,284,287,1,0,0,0,285,283,
        1,0,0,0,285,286,1,0,0,0,286,288,1,0,0,0,287,285,1,0,0,0,288,289,
        5,22,0,0,289,291,1,0,0,0,290,278,1,0,0,0,291,292,1,0,0,0,292,290,
        1,0,0,0,292,293,1,0,0,0,293,294,1,0,0,0,294,295,5,22,0,0,295,37,
        1,0,0,0,296,297,5,23,0,0,297,298,3,78,39,0,298,299,5,24,0,0,299,
        301,1,0,0,0,300,296,1,0,0,0,301,302,1,0,0,0,302,300,1,0,0,0,302,
        303,1,0,0,0,303,304,1,0,0,0,304,305,3,16,8,0,305,306,5,21,0,0,306,
        311,3,78,39,0,307,308,5,25,0,0,308,310,3,78,39,0,309,307,1,0,0,0,
        310,313,1,0,0,0,311,309,1,0,0,0,311,312,1,0,0,0,312,314,1,0,0,0,
        313,311,1,0,0,0,314,315,5,22,0,0,315,39,1,0,0,0,316,317,5,37,0,0,
        317,319,5,21,0,0,318,320,3,42,21,0,319,318,1,0,0,0,319,320,1,0,0,
        0,320,321,1,0,0,0,321,322,5,22,0,0,322,41,1,0,0,0,323,328,3,44,22,
        0,324,325,5,25,0,0,325,327,3,44,22,0,326,324,1,0,0,0,327,330,1,0,
        0,0,328,326,1,0,0,0,328,329,1,0,0,0,329,43,1,0,0,0,330,328,1,0,0,
        0,331,332,5,37,0,0,332,333,5,8,0,0,333,334,3,78,39,0,334,45,1,0,
        0,0,335,336,5,37,0,0,336,338,5,19,0,0,337,339,3,48,24,0,338,337,
        1,0,0,0,338,339,1,0,0,0,339,340,1,0,0,0,340,341,5,20,0,0,341,47,
        1,0,0,0,342,347,3,78,39,0,343,344,5,25,0,0,344,346,3,78,39,0,345,
        343,1,0,0,0,346,349,1,0,0,0,347,345,1,0,0,0,347,348,1,0,0,0,348,
        49,1,0,0,0,349,347,1,0,0,0,350,351,5,37,0,0,351,352,5,7,0,0,352,
        353,3,46,23,0,353,51,1,0,0,0,354,363,3,4,2,0,355,363,3,54,27,0,356,
        363,3,56,28,0,357,363,3,62,31,0,358,363,3,68,34,0,359,363,3,70,35,
        0,360,363,3,72,36,0,361,363,3,74,37,0,362,354,1,0,0,0,362,355,1,
        0,0,0,362,356,1,0,0,0,362,357,1,0,0,0,362,358,1,0,0,0,362,359,1,
        0,0,0,362,360,1,0,0,0,362,361,1,0,0,0,363,53,1,0,0,0,364,368,5,37,
        0,0,365,368,3,32,16,0,366,368,3,34,17,0,367,364,1,0,0,0,367,365,
        1,0,0,0,367,366,1,0,0,0,368,369,1,0,0,0,369,370,7,1,0,0,370,371,
        3,78,39,0,371,372,3,80,40,0,372,55,1,0,0,0,373,374,5,9,0,0,374,375,
        3,78,39,0,375,379,3,76,38,0,376,378,3,58,29,0,377,376,1,0,0,0,378,
        381,1,0,0,0,379,377,1,0,0,0,379,380,1,0,0,0,380,383,1,0,0,0,381,
        379,1,0,0,0,382,384,3,60,30,0,383,382,1,0,0,0,383,384,1,0,0,0,384,
        400,1,0,0,0,385,386,5,9,0,0,386,387,5,19,0,0,387,388,3,78,39,0,388,
        389,5,20,0,0,389,393,3,76,38,0,390,392,3,58,29,0,391,390,1,0,0,0,
        392,395,1,0,0,0,393,391,1,0,0,0,393,394,1,0,0,0,394,397,1,0,0,0,
        395,393,1,0,0,0,396,398,3,60,30,0,397,396,1,0,0,0,397,398,1,0,0,
        0,398,400,1,0,0,0,399,373,1,0,0,0,399,385,1,0,0,0,400,57,1,0,0,0,
        401,402,5,10,0,0,402,403,5,9,0,0,403,404,3,78,39,0,404,405,3,76,
        38,0,405,414,1,0,0,0,406,407,5,10,0,0,407,408,5,9,0,0,408,409,5,
        19,0,0,409,410,3,78,39,0,410,411,5,20,0,0,411,412,3,76,38,0,412,
        414,1,0,0,0,413,401,1,0,0,0,413,406,1,0,0,0,414,59,1,0,0,0,415,416,
        5,10,0,0,416,417,3,76,38,0,417,61,1,0,0,0,418,419,5,11,0,0,419,420,
        3,78,39,0,420,421,3,76,38,0,421,439,1,0,0,0,422,423,5,11,0,0,423,
        424,3,64,32,0,424,425,5,26,0,0,425,426,3,78,39,0,426,427,5,26,0,
        0,427,428,3,66,33,0,428,429,3,76,38,0,429,439,1,0,0,0,430,431,5,
        11,0,0,431,432,5,37,0,0,432,433,5,25,0,0,433,434,5,37,0,0,434,435,
        5,18,0,0,435,436,5,12,0,0,436,437,5,37,0,0,437,439,3,76,38,0,438,
        418,1,0,0,0,438,422,1,0,0,0,438,430,1,0,0,0,439,63,1,0,0,0,440,443,
        3,54,27,0,441,443,3,4,2,0,442,440,1,0,0,0,442,441,1,0,0,0,443,65,
        1,0,0,0,444,445,3,54,27,0,445,67,1,0,0,0,446,447,5,32,0,0,447,448,
        3,80,40,0,448,69,1,0,0,0,449,450,5,31,0,0,450,451,3,80,40,0,451,
        71,1,0,0,0,452,454,5,30,0,0,453,455,3,78,39,0,454,453,1,0,0,0,454,
        455,1,0,0,0,455,456,1,0,0,0,456,457,3,80,40,0,457,73,1,0,0,0,458,
        459,5,37,0,0,459,461,5,19,0,0,460,462,3,48,24,0,461,460,1,0,0,0,
        461,462,1,0,0,0,462,463,1,0,0,0,463,464,5,20,0,0,464,465,3,80,40,
        0,465,75,1,0,0,0,466,472,5,21,0,0,467,468,3,52,26,0,468,469,3,80,
        40,0,469,471,1,0,0,0,470,467,1,0,0,0,471,474,1,0,0,0,472,470,1,0,
        0,0,472,473,1,0,0,0,473,475,1,0,0,0,474,472,1,0,0,0,475,476,5,22,
        0,0,476,77,1,0,0,0,477,478,6,39,-1,0,478,479,5,19,0,0,479,480,3,
        78,39,0,480,481,5,20,0,0,481,496,1,0,0,0,482,496,5,35,0,0,483,496,
        5,34,0,0,484,496,5,36,0,0,485,496,5,28,0,0,486,496,5,29,0,0,487,
        496,3,50,25,0,488,496,3,46,23,0,489,496,3,36,18,0,490,496,3,38,19,
        0,491,496,3,40,20,0,492,496,3,32,16,0,493,496,3,34,17,0,494,496,
        5,37,0,0,495,477,1,0,0,0,495,482,1,0,0,0,495,483,1,0,0,0,495,484,
        1,0,0,0,495,485,1,0,0,0,495,486,1,0,0,0,495,487,1,0,0,0,495,488,
        1,0,0,0,495,489,1,0,0,0,495,490,1,0,0,0,495,491,1,0,0,0,495,492,
        1,0,0,0,495,493,1,0,0,0,495,494,1,0,0,0,496,508,1,0,0,0,497,498,
        10,17,0,0,498,499,5,16,0,0,499,507,3,78,39,18,500,501,10,16,0,0,
        501,502,5,15,0,0,502,507,3,78,39,17,503,504,10,15,0,0,504,505,5,
        13,0,0,505,507,3,78,39,16,506,497,1,0,0,0,506,500,1,0,0,0,506,503,
        1,0,0,0,507,510,1,0,0,0,508,506,1,0,0,0,508,509,1,0,0,0,509,79,1,
        0,0,0,510,508,1,0,0,0,511,514,7,2,0,0,512,514,5,0,0,1,513,511,1,
        0,0,0,513,512,1,0,0,0,514,81,1,0,0,0,49,85,96,101,112,121,126,130,
        136,140,152,164,175,179,186,199,208,212,221,229,246,250,255,263,
        273,285,292,302,311,319,328,338,347,362,367,379,383,393,397,399,
        413,438,442,454,461,472,495,506,508,513
    ]

class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'var'", "'func'", "'type'", "'struct'", 
                     "'interface'", "'const'", "'.'", "':'", "'if'", "'else'", 
                     "'for'", "'range'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'='", "':='", "'('", "')'", "'{'", "'}'", 
                     "'['", "']'", "','", "';'", "<INVALID>", "<INVALID>", 
                     "'nil'", "'return'", "'continue'", "'break'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "OP_COMPARE", "OP_ASSIGN", "OP_LOGIC", 
                      "OP_ARITH", "OP_EQUAL", "OP_ASSEQ", "PAREN_OPEN", 
                      "PAREN_CLOSE", "BRACE_OPEN", "BRACE_CLOSE", "BRACK_OPEN", 
                      "BRACK_CLOSE", "SEPARATOR_COMMA", "SEPARATOR_SEMI", 
                      "TYPE", "BOOLLIT", "NILLIT", "RETURN", "CONTINUE", 
                      "BREAK", "KEYWORD", "FLOATLIT", "INTLIT", "STRLIT", 
                      "ID", "DECIMAL_LITERAL", "BINARY_LITERAL", "OCTAL_LITERAL", 
                      "HEXADECIMAL_LITERAL", "NEWLINE", "WS", "MULTILINE_COMMENT", 
                      "COMMENT", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_decl = 1
    RULE_vardecl = 2
    RULE_receiver = 3
    RULE_funcdecl = 4
    RULE_arraydecl = 5
    RULE_structdecl = 6
    RULE_fielddecl = 7
    RULE_typ = 8
    RULE_arraytype = 9
    RULE_basictype = 10
    RULE_interfacedecl = 11
    RULE_methoddecl = 12
    RULE_paramlist = 13
    RULE_param = 14
    RULE_constdecl = 15
    RULE_array_access = 16
    RULE_struct_access = 17
    RULE_multi_array_literal = 18
    RULE_array_literal = 19
    RULE_struct_literal = 20
    RULE_struct_field_list = 21
    RULE_struct_field = 22
    RULE_funccall = 23
    RULE_arglist = 24
    RULE_methodcall = 25
    RULE_stmt = 26
    RULE_assignstmt = 27
    RULE_ifstmt = 28
    RULE_elseifstmt = 29
    RULE_elsestmt = 30
    RULE_forstmt = 31
    RULE_forinit = 32
    RULE_forupdate = 33
    RULE_breakstmt = 34
    RULE_continuestmt = 35
    RULE_returnstmt = 36
    RULE_callstmt = 37
    RULE_block = 38
    RULE_expr = 39
    RULE_nl = 40

    ruleNames =  [ "program", "decl", "vardecl", "receiver", "funcdecl", 
                   "arraydecl", "structdecl", "fielddecl", "typ", "arraytype", 
                   "basictype", "interfacedecl", "methoddecl", "paramlist", 
                   "param", "constdecl", "array_access", "struct_access", 
                   "multi_array_literal", "array_literal", "struct_literal", 
                   "struct_field_list", "struct_field", "funccall", "arglist", 
                   "methodcall", "stmt", "assignstmt", "ifstmt", "elseifstmt", 
                   "elsestmt", "forstmt", "forinit", "forupdate", "breakstmt", 
                   "continuestmt", "returnstmt", "callstmt", "block", "expr", 
                   "nl" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    OP_COMPARE=13
    OP_ASSIGN=14
    OP_LOGIC=15
    OP_ARITH=16
    OP_EQUAL=17
    OP_ASSEQ=18
    PAREN_OPEN=19
    PAREN_CLOSE=20
    BRACE_OPEN=21
    BRACE_CLOSE=22
    BRACK_OPEN=23
    BRACK_CLOSE=24
    SEPARATOR_COMMA=25
    SEPARATOR_SEMI=26
    TYPE=27
    BOOLLIT=28
    NILLIT=29
    RETURN=30
    CONTINUE=31
    BREAK=32
    KEYWORD=33
    FLOATLIT=34
    INTLIT=35
    STRLIT=36
    ID=37
    DECIMAL_LITERAL=38
    BINARY_LITERAL=39
    OCTAL_LITERAL=40
    HEXADECIMAL_LITERAL=41
    NEWLINE=42
    WS=43
    MULTILINE_COMMENT=44
    COMMENT=45
    ERROR_CHAR=46
    UNCLOSE_STRING=47
    ILLEGAL_ESCAPE=48

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.DeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.DeclContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_program




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 144955148878) != 0):
                self.state = 82
                self.decl()
                self.state = 87
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 88
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(MiniGoParser.StmtContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(MiniGoParser.FuncdeclContext,0)


        def arraydecl(self):
            return self.getTypedRuleContext(MiniGoParser.ArraydeclContext,0)


        def structdecl(self):
            return self.getTypedRuleContext(MiniGoParser.StructdeclContext,0)


        def interfacedecl(self):
            return self.getTypedRuleContext(MiniGoParser.InterfacedeclContext,0)


        def constdecl(self):
            return self.getTypedRuleContext(MiniGoParser.ConstdeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl




    def decl(self):

        localctx = MiniGoParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl)
        try:
            self.state = 96
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 90
                self.stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 91
                self.funcdecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 92
                self.arraydecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 93
                self.structdecl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 94
                self.interfacedecl()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 95
                self.constdecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def OP_EQUAL(self):
            return self.getToken(MiniGoParser.OP_EQUAL, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def nl(self):
            return self.getTypedRuleContext(MiniGoParser.NlContext,0)


        def typ(self):
            return self.getTypedRuleContext(MiniGoParser.TypContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_vardecl




    def vardecl(self):

        localctx = MiniGoParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_vardecl)
        self._la = 0 # Token type
        try:
            self.state = 112
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                self.match(MiniGoParser.T__0)
                self.state = 99
                self.match(MiniGoParser.ID)
                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 137581559808) != 0):
                    self.state = 100
                    self.typ()


                self.state = 103
                self.match(MiniGoParser.OP_EQUAL)
                self.state = 104
                self.expr(0)
                self.state = 105
                self.nl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 107
                self.match(MiniGoParser.T__0)
                self.state = 108
                self.match(MiniGoParser.ID)
                self.state = 109
                self.typ()
                self.state = 110
                self.nl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReceiverContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PAREN_OPEN(self):
            return self.getToken(MiniGoParser.PAREN_OPEN, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def typ(self):
            return self.getTypedRuleContext(MiniGoParser.TypContext,0)


        def PAREN_CLOSE(self):
            return self.getToken(MiniGoParser.PAREN_CLOSE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_receiver




    def receiver(self):

        localctx = MiniGoParser.ReceiverContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_receiver)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(MiniGoParser.PAREN_OPEN)
            self.state = 115
            self.match(MiniGoParser.ID)
            self.state = 116
            self.typ()
            self.state = 117
            self.match(MiniGoParser.PAREN_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def PAREN_OPEN(self):
            return self.getToken(MiniGoParser.PAREN_OPEN, 0)

        def PAREN_CLOSE(self):
            return self.getToken(MiniGoParser.PAREN_CLOSE, 0)

        def BRACE_OPEN(self):
            return self.getToken(MiniGoParser.BRACE_OPEN, 0)

        def BRACE_CLOSE(self):
            return self.getToken(MiniGoParser.BRACE_CLOSE, 0)

        def nl(self):
            return self.getTypedRuleContext(MiniGoParser.NlContext,0)


        def receiver(self):
            return self.getTypedRuleContext(MiniGoParser.ReceiverContext,0)


        def paramlist(self):
            return self.getTypedRuleContext(MiniGoParser.ParamlistContext,0)


        def typ(self):
            return self.getTypedRuleContext(MiniGoParser.TypContext,0)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StmtContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StmtContext,i)


        def returnstmt(self):
            return self.getTypedRuleContext(MiniGoParser.ReturnstmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcdecl




    def funcdecl(self):

        localctx = MiniGoParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_funcdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(MiniGoParser.T__1)
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 120
                self.receiver()


            self.state = 123
            self.match(MiniGoParser.ID)
            self.state = 124
            self.match(MiniGoParser.PAREN_OPEN)
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
                self.state = 125
                self.paramlist()


            self.state = 128
            self.match(MiniGoParser.PAREN_CLOSE)
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 137581559808) != 0):
                self.state = 129
                self.typ()


            self.state = 132
            self.match(MiniGoParser.BRACE_OPEN)
            self.state = 136
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 133
                    self.stmt() 
                self.state = 138
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==30:
                self.state = 139
                self.returnstmt()


            self.state = 142
            self.match(MiniGoParser.BRACE_CLOSE)
            self.state = 143
            self.nl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraydeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def typ(self):
            return self.getTypedRuleContext(MiniGoParser.TypContext,0)


        def nl(self):
            return self.getTypedRuleContext(MiniGoParser.NlContext,0)


        def BRACK_OPEN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.BRACK_OPEN)
            else:
                return self.getToken(MiniGoParser.BRACK_OPEN, i)

        def INTLIT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.INTLIT)
            else:
                return self.getToken(MiniGoParser.INTLIT, i)

        def BRACK_CLOSE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.BRACK_CLOSE)
            else:
                return self.getToken(MiniGoParser.BRACK_CLOSE, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arraydecl




    def arraydecl(self):

        localctx = MiniGoParser.ArraydeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_arraydecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(MiniGoParser.T__0)
            self.state = 146
            self.match(MiniGoParser.ID)
            self.state = 150 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 147
                    self.match(MiniGoParser.BRACK_OPEN)
                    self.state = 148
                    self.match(MiniGoParser.INTLIT)
                    self.state = 149
                    self.match(MiniGoParser.BRACK_CLOSE)

                else:
                    raise NoViableAltException(self)
                self.state = 152 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

            self.state = 154
            self.typ()
            self.state = 155
            self.nl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def BRACE_OPEN(self):
            return self.getToken(MiniGoParser.BRACE_OPEN, 0)

        def BRACE_CLOSE(self):
            return self.getToken(MiniGoParser.BRACE_CLOSE, 0)

        def nl(self):
            return self.getTypedRuleContext(MiniGoParser.NlContext,0)


        def fielddecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.FielddeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.FielddeclContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structdecl




    def structdecl(self):

        localctx = MiniGoParser.StructdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_structdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(MiniGoParser.T__2)
            self.state = 158
            self.match(MiniGoParser.ID)
            self.state = 159
            self.match(MiniGoParser.T__3)
            self.state = 160
            self.match(MiniGoParser.BRACE_OPEN)
            self.state = 164
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==37:
                self.state = 161
                self.fielddecl()
                self.state = 166
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 167
            self.match(MiniGoParser.BRACE_CLOSE)
            self.state = 168
            self.nl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FielddeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def typ(self):
            return self.getTypedRuleContext(MiniGoParser.TypContext,0)


        def SEPARATOR_SEMI(self):
            return self.getToken(MiniGoParser.SEPARATOR_SEMI, 0)

        def nl(self):
            return self.getTypedRuleContext(MiniGoParser.NlContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_fielddecl




    def fielddecl(self):

        localctx = MiniGoParser.FielddeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_fielddecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(MiniGoParser.ID)
            self.state = 171
            self.typ()
            self.state = 175
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 173
                self.match(MiniGoParser.SEPARATOR_SEMI)
                pass

            elif la_ == 2:
                self.state = 174
                self.nl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arraytype(self):
            return self.getTypedRuleContext(MiniGoParser.ArraytypeContext,0)


        def basictype(self):
            return self.getTypedRuleContext(MiniGoParser.BasictypeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_typ




    def typ(self):

        localctx = MiniGoParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_typ)
        try:
            self.state = 179
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [23]:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.arraytype()
                pass
            elif token in [27, 37]:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                self.basictype()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArraytypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def basictype(self):
            return self.getTypedRuleContext(MiniGoParser.BasictypeContext,0)


        def BRACK_OPEN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.BRACK_OPEN)
            else:
                return self.getToken(MiniGoParser.BRACK_OPEN, i)

        def INTLIT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.INTLIT)
            else:
                return self.getToken(MiniGoParser.INTLIT, i)

        def BRACK_CLOSE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.BRACK_CLOSE)
            else:
                return self.getToken(MiniGoParser.BRACK_CLOSE, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arraytype




    def arraytype(self):

        localctx = MiniGoParser.ArraytypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_arraytype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 181
                self.match(MiniGoParser.BRACK_OPEN)
                self.state = 182
                self.match(MiniGoParser.INTLIT)
                self.state = 183
                self.match(MiniGoParser.BRACK_CLOSE)
                self.state = 186 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==23):
                    break

            self.state = 188
            self.basictype()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BasictypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_basictype




    def basictype(self):

        localctx = MiniGoParser.BasictypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_basictype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            _la = self._input.LA(1)
            if not(_la==27 or _la==37):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfacedeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def BRACE_OPEN(self):
            return self.getToken(MiniGoParser.BRACE_OPEN, 0)

        def BRACE_CLOSE(self):
            return self.getToken(MiniGoParser.BRACE_CLOSE, 0)

        def nl(self):
            return self.getTypedRuleContext(MiniGoParser.NlContext,0)


        def methoddecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.MethoddeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.MethoddeclContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interfacedecl




    def interfacedecl(self):

        localctx = MiniGoParser.InterfacedeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_interfacedecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.match(MiniGoParser.T__2)
            self.state = 193
            self.match(MiniGoParser.ID)
            self.state = 194
            self.match(MiniGoParser.T__4)
            self.state = 195
            self.match(MiniGoParser.BRACE_OPEN)
            self.state = 199
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==37:
                self.state = 196
                self.methoddecl()
                self.state = 201
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 202
            self.match(MiniGoParser.BRACE_CLOSE)
            self.state = 203
            self.nl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethoddeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def PAREN_OPEN(self):
            return self.getToken(MiniGoParser.PAREN_OPEN, 0)

        def PAREN_CLOSE(self):
            return self.getToken(MiniGoParser.PAREN_CLOSE, 0)

        def nl(self):
            return self.getTypedRuleContext(MiniGoParser.NlContext,0)


        def paramlist(self):
            return self.getTypedRuleContext(MiniGoParser.ParamlistContext,0)


        def typ(self):
            return self.getTypedRuleContext(MiniGoParser.TypContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_methoddecl




    def methoddecl(self):

        localctx = MiniGoParser.MethoddeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_methoddecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.match(MiniGoParser.ID)
            self.state = 206
            self.match(MiniGoParser.PAREN_OPEN)
            self.state = 208
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
                self.state = 207
                self.paramlist()


            self.state = 210
            self.match(MiniGoParser.PAREN_CLOSE)
            self.state = 212
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 137581559808) != 0):
                self.state = 211
                self.typ()


            self.state = 214
            self.nl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ParamContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ParamContext,i)


        def SEPARATOR_COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEPARATOR_COMMA)
            else:
                return self.getToken(MiniGoParser.SEPARATOR_COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_paramlist




    def paramlist(self):

        localctx = MiniGoParser.ParamlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_paramlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.param()
            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 217
                self.match(MiniGoParser.SEPARATOR_COMMA)
                self.state = 218
                self.param()
                self.state = 223
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def typ(self):
            return self.getTypedRuleContext(MiniGoParser.TypContext,0)


        def SEPARATOR_COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEPARATOR_COMMA)
            else:
                return self.getToken(MiniGoParser.SEPARATOR_COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_param




    def param(self):

        localctx = MiniGoParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_param)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.match(MiniGoParser.ID)
            self.state = 229
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 225
                self.match(MiniGoParser.SEPARATOR_COMMA)
                self.state = 226
                self.match(MiniGoParser.ID)
                self.state = 231
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 232
            self.typ()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def OP_EQUAL(self):
            return self.getToken(MiniGoParser.OP_EQUAL, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def nl(self):
            return self.getTypedRuleContext(MiniGoParser.NlContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_constdecl




    def constdecl(self):

        localctx = MiniGoParser.ConstdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_constdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(MiniGoParser.T__5)
            self.state = 235
            self.match(MiniGoParser.ID)
            self.state = 236
            self.match(MiniGoParser.OP_EQUAL)
            self.state = 237
            self.expr(0)
            self.state = 238
            self.nl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def BRACK_OPEN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.BRACK_OPEN)
            else:
                return self.getToken(MiniGoParser.BRACK_OPEN, i)

        def INTLIT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.INTLIT)
            else:
                return self.getToken(MiniGoParser.INTLIT, i)

        def BRACK_CLOSE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.BRACK_CLOSE)
            else:
                return self.getToken(MiniGoParser.BRACK_CLOSE, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_access




    def array_access(self):

        localctx = MiniGoParser.Array_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_array_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.match(MiniGoParser.ID)
            self.state = 244 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 241
                    self.match(MiniGoParser.BRACK_OPEN)
                    self.state = 242
                    self.match(MiniGoParser.INTLIT)
                    self.state = 243
                    self.match(MiniGoParser.BRACK_CLOSE)

                else:
                    raise NoViableAltException(self)
                self.state = 246 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_accessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def array_access(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Array_accessContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Array_accessContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_access




    def struct_access(self):

        localctx = MiniGoParser.Struct_accessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_struct_access)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 248
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.state = 249
                self.array_access()
                pass


            self.state = 252
            self.match(MiniGoParser.T__6)
            self.state = 255
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 253
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.state = 254
                self.array_access()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Multi_array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(MiniGoParser.TypContext,0)


        def BRACE_OPEN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.BRACE_OPEN)
            else:
                return self.getToken(MiniGoParser.BRACE_OPEN, i)

        def BRACE_CLOSE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.BRACE_CLOSE)
            else:
                return self.getToken(MiniGoParser.BRACE_CLOSE, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExprContext,i)


        def BRACK_OPEN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.BRACK_OPEN)
            else:
                return self.getToken(MiniGoParser.BRACK_OPEN, i)

        def BRACK_CLOSE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.BRACK_CLOSE)
            else:
                return self.getToken(MiniGoParser.BRACK_CLOSE, i)

        def SEPARATOR_COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEPARATOR_COMMA)
            else:
                return self.getToken(MiniGoParser.SEPARATOR_COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_multi_array_literal




    def multi_array_literal(self):

        localctx = MiniGoParser.Multi_array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_multi_array_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 257
                    self.match(MiniGoParser.BRACK_OPEN)
                    self.state = 258
                    self.expr(0)
                    self.state = 259
                    self.match(MiniGoParser.BRACK_CLOSE)

                else:
                    raise NoViableAltException(self)
                self.state = 263 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

            self.state = 265
            self.typ()
            self.state = 266
            self.match(MiniGoParser.BRACE_OPEN)

            self.state = 267
            self.match(MiniGoParser.BRACE_OPEN)
            self.state = 268
            self.expr(0)
            self.state = 273
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 269
                self.match(MiniGoParser.SEPARATOR_COMMA)
                self.state = 270
                self.expr(0)
                self.state = 275
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 276
            self.match(MiniGoParser.BRACE_CLOSE)
            self.state = 290 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 278
                self.match(MiniGoParser.SEPARATOR_COMMA)
                self.state = 279
                self.match(MiniGoParser.BRACE_OPEN)
                self.state = 280
                self.expr(0)
                self.state = 285
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==25:
                    self.state = 281
                    self.match(MiniGoParser.SEPARATOR_COMMA)
                    self.state = 282
                    self.expr(0)
                    self.state = 287
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 288
                self.match(MiniGoParser.BRACE_CLOSE)
                self.state = 292 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==25):
                    break

            self.state = 294
            self.match(MiniGoParser.BRACE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typ(self):
            return self.getTypedRuleContext(MiniGoParser.TypContext,0)


        def BRACE_OPEN(self):
            return self.getToken(MiniGoParser.BRACE_OPEN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExprContext,i)


        def BRACE_CLOSE(self):
            return self.getToken(MiniGoParser.BRACE_CLOSE, 0)

        def BRACK_OPEN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.BRACK_OPEN)
            else:
                return self.getToken(MiniGoParser.BRACK_OPEN, i)

        def BRACK_CLOSE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.BRACK_CLOSE)
            else:
                return self.getToken(MiniGoParser.BRACK_CLOSE, i)

        def SEPARATOR_COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEPARATOR_COMMA)
            else:
                return self.getToken(MiniGoParser.SEPARATOR_COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_array_literal




    def array_literal(self):

        localctx = MiniGoParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_array_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 296
                    self.match(MiniGoParser.BRACK_OPEN)
                    self.state = 297
                    self.expr(0)
                    self.state = 298
                    self.match(MiniGoParser.BRACK_CLOSE)

                else:
                    raise NoViableAltException(self)
                self.state = 302 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

            self.state = 304
            self.typ()
            self.state = 305
            self.match(MiniGoParser.BRACE_OPEN)
            self.state = 306
            self.expr(0)
            self.state = 311
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 307
                self.match(MiniGoParser.SEPARATOR_COMMA)
                self.state = 308
                self.expr(0)
                self.state = 313
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 314
            self.match(MiniGoParser.BRACE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def BRACE_OPEN(self):
            return self.getToken(MiniGoParser.BRACE_OPEN, 0)

        def BRACE_CLOSE(self):
            return self.getToken(MiniGoParser.BRACE_CLOSE, 0)

        def struct_field_list(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_field_listContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_literal




    def struct_literal(self):

        localctx = MiniGoParser.Struct_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_struct_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 316
            self.match(MiniGoParser.ID)
            self.state = 317
            self.match(MiniGoParser.BRACE_OPEN)
            self.state = 319
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
                self.state = 318
                self.struct_field_list()


            self.state = 321
            self.match(MiniGoParser.BRACE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_field_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def struct_field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Struct_fieldContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Struct_fieldContext,i)


        def SEPARATOR_COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEPARATOR_COMMA)
            else:
                return self.getToken(MiniGoParser.SEPARATOR_COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_field_list




    def struct_field_list(self):

        localctx = MiniGoParser.Struct_field_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_struct_field_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 323
            self.struct_field()
            self.state = 328
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 324
                self.match(MiniGoParser.SEPARATOR_COMMA)
                self.state = 325
                self.struct_field()
                self.state = 330
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_fieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_struct_field




    def struct_field(self):

        localctx = MiniGoParser.Struct_fieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_struct_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 331
            self.match(MiniGoParser.ID)
            self.state = 332
            self.match(MiniGoParser.T__7)
            self.state = 333
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunccallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def PAREN_OPEN(self):
            return self.getToken(MiniGoParser.PAREN_OPEN, 0)

        def PAREN_CLOSE(self):
            return self.getToken(MiniGoParser.PAREN_CLOSE, 0)

        def arglist(self):
            return self.getTypedRuleContext(MiniGoParser.ArglistContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funccall




    def funccall(self):

        localctx = MiniGoParser.FunccallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_funccall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self.match(MiniGoParser.ID)
            self.state = 336
            self.match(MiniGoParser.PAREN_OPEN)
            self.state = 338
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 258512257024) != 0):
                self.state = 337
                self.arglist()


            self.state = 340
            self.match(MiniGoParser.PAREN_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArglistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExprContext,i)


        def SEPARATOR_COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEPARATOR_COMMA)
            else:
                return self.getToken(MiniGoParser.SEPARATOR_COMMA, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arglist




    def arglist(self):

        localctx = MiniGoParser.ArglistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_arglist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 342
            self.expr(0)
            self.state = 347
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25:
                self.state = 343
                self.match(MiniGoParser.SEPARATOR_COMMA)
                self.state = 344
                self.expr(0)
                self.state = 349
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodcallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def funccall(self):
            return self.getTypedRuleContext(MiniGoParser.FunccallContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_methodcall




    def methodcall(self):

        localctx = MiniGoParser.MethodcallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_methodcall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.match(MiniGoParser.ID)
            self.state = 351
            self.match(MiniGoParser.T__6)
            self.state = 352
            self.funccall()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(MiniGoParser.VardeclContext,0)


        def assignstmt(self):
            return self.getTypedRuleContext(MiniGoParser.AssignstmtContext,0)


        def ifstmt(self):
            return self.getTypedRuleContext(MiniGoParser.IfstmtContext,0)


        def forstmt(self):
            return self.getTypedRuleContext(MiniGoParser.ForstmtContext,0)


        def breakstmt(self):
            return self.getTypedRuleContext(MiniGoParser.BreakstmtContext,0)


        def continuestmt(self):
            return self.getTypedRuleContext(MiniGoParser.ContinuestmtContext,0)


        def returnstmt(self):
            return self.getTypedRuleContext(MiniGoParser.ReturnstmtContext,0)


        def callstmt(self):
            return self.getTypedRuleContext(MiniGoParser.CallstmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_stmt




    def stmt(self):

        localctx = MiniGoParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_stmt)
        try:
            self.state = 362
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 354
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 355
                self.assignstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 356
                self.ifstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 357
                self.forstmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 358
                self.breakstmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 359
                self.continuestmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 360
                self.returnstmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 361
                self.callstmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def nl(self):
            return self.getTypedRuleContext(MiniGoParser.NlContext,0)


        def OP_ASSEQ(self):
            return self.getToken(MiniGoParser.OP_ASSEQ, 0)

        def OP_ASSIGN(self):
            return self.getToken(MiniGoParser.OP_ASSIGN, 0)

        def OP_EQUAL(self):
            return self.getToken(MiniGoParser.OP_EQUAL, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def array_access(self):
            return self.getTypedRuleContext(MiniGoParser.Array_accessContext,0)


        def struct_access(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_accessContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assignstmt




    def assignstmt(self):

        localctx = MiniGoParser.AssignstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_assignstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 364
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.state = 365
                self.array_access()
                pass

            elif la_ == 3:
                self.state = 366
                self.struct_access()
                pass


            self.state = 369
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 409600) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 370
            self.expr(0)
            self.state = 371
            self.nl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def elseifstmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ElseifstmtContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ElseifstmtContext,i)


        def elsestmt(self):
            return self.getTypedRuleContext(MiniGoParser.ElsestmtContext,0)


        def PAREN_OPEN(self):
            return self.getToken(MiniGoParser.PAREN_OPEN, 0)

        def PAREN_CLOSE(self):
            return self.getToken(MiniGoParser.PAREN_CLOSE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_ifstmt




    def ifstmt(self):

        localctx = MiniGoParser.IfstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_ifstmt)
        self._la = 0 # Token type
        try:
            self.state = 399
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 373
                self.match(MiniGoParser.T__8)
                self.state = 374
                self.expr(0)
                self.state = 375
                self.block()
                self.state = 379
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 376
                        self.elseifstmt() 
                    self.state = 381
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

                self.state = 383
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10:
                    self.state = 382
                    self.elsestmt()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 385
                self.match(MiniGoParser.T__8)
                self.state = 386
                self.match(MiniGoParser.PAREN_OPEN)
                self.state = 387
                self.expr(0)
                self.state = 388
                self.match(MiniGoParser.PAREN_CLOSE)
                self.state = 389
                self.block()
                self.state = 393
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 390
                        self.elseifstmt() 
                    self.state = 395
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

                self.state = 397
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==10:
                    self.state = 396
                    self.elsestmt()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseifstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def PAREN_OPEN(self):
            return self.getToken(MiniGoParser.PAREN_OPEN, 0)

        def PAREN_CLOSE(self):
            return self.getToken(MiniGoParser.PAREN_CLOSE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_elseifstmt




    def elseifstmt(self):

        localctx = MiniGoParser.ElseifstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_elseifstmt)
        try:
            self.state = 413
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 401
                self.match(MiniGoParser.T__9)
                self.state = 402
                self.match(MiniGoParser.T__8)
                self.state = 403
                self.expr(0)
                self.state = 404
                self.block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 406
                self.match(MiniGoParser.T__9)
                self.state = 407
                self.match(MiniGoParser.T__8)
                self.state = 408
                self.match(MiniGoParser.PAREN_OPEN)
                self.state = 409
                self.expr(0)
                self.state = 410
                self.match(MiniGoParser.PAREN_CLOSE)
                self.state = 411
                self.block()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElsestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_elsestmt




    def elsestmt(self):

        localctx = MiniGoParser.ElsestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_elsestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
            self.match(MiniGoParser.T__9)
            self.state = 416
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def forinit(self):
            return self.getTypedRuleContext(MiniGoParser.ForinitContext,0)


        def SEPARATOR_SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEPARATOR_SEMI)
            else:
                return self.getToken(MiniGoParser.SEPARATOR_SEMI, i)

        def forupdate(self):
            return self.getTypedRuleContext(MiniGoParser.ForupdateContext,0)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def SEPARATOR_COMMA(self):
            return self.getToken(MiniGoParser.SEPARATOR_COMMA, 0)

        def OP_ASSEQ(self):
            return self.getToken(MiniGoParser.OP_ASSEQ, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_forstmt




    def forstmt(self):

        localctx = MiniGoParser.ForstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_forstmt)
        try:
            self.state = 438
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 418
                self.match(MiniGoParser.T__10)
                self.state = 419
                self.expr(0)
                self.state = 420
                self.block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 422
                self.match(MiniGoParser.T__10)
                self.state = 423
                self.forinit()
                self.state = 424
                self.match(MiniGoParser.SEPARATOR_SEMI)
                self.state = 425
                self.expr(0)
                self.state = 426
                self.match(MiniGoParser.SEPARATOR_SEMI)
                self.state = 427
                self.forupdate()
                self.state = 428
                self.block()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 430
                self.match(MiniGoParser.T__10)
                self.state = 431
                self.match(MiniGoParser.ID)
                self.state = 432
                self.match(MiniGoParser.SEPARATOR_COMMA)
                self.state = 433
                self.match(MiniGoParser.ID)
                self.state = 434
                self.match(MiniGoParser.OP_ASSEQ)
                self.state = 435
                self.match(MiniGoParser.T__11)
                self.state = 436
                self.match(MiniGoParser.ID)
                self.state = 437
                self.block()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForinitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignstmt(self):
            return self.getTypedRuleContext(MiniGoParser.AssignstmtContext,0)


        def vardecl(self):
            return self.getTypedRuleContext(MiniGoParser.VardeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forinit




    def forinit(self):

        localctx = MiniGoParser.ForinitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_forinit)
        try:
            self.state = 442
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 440
                self.assignstmt()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 441
                self.vardecl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForupdateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignstmt(self):
            return self.getTypedRuleContext(MiniGoParser.AssignstmtContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forupdate




    def forupdate(self):

        localctx = MiniGoParser.ForupdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_forupdate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 444
            self.assignstmt()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MiniGoParser.BREAK, 0)

        def nl(self):
            return self.getTypedRuleContext(MiniGoParser.NlContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_breakstmt




    def breakstmt(self):

        localctx = MiniGoParser.BreakstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_breakstmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 446
            self.match(MiniGoParser.BREAK)
            self.state = 447
            self.nl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinuestmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def nl(self):
            return self.getTypedRuleContext(MiniGoParser.NlContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_continuestmt




    def continuestmt(self):

        localctx = MiniGoParser.ContinuestmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_continuestmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 449
            self.match(MiniGoParser.CONTINUE)
            self.state = 450
            self.nl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MiniGoParser.RETURN, 0)

        def nl(self):
            return self.getTypedRuleContext(MiniGoParser.NlContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_returnstmt




    def returnstmt(self):

        localctx = MiniGoParser.ReturnstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_returnstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 452
            self.match(MiniGoParser.RETURN)
            self.state = 454
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 258512257024) != 0):
                self.state = 453
                self.expr(0)


            self.state = 456
            self.nl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallstmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def PAREN_OPEN(self):
            return self.getToken(MiniGoParser.PAREN_OPEN, 0)

        def PAREN_CLOSE(self):
            return self.getToken(MiniGoParser.PAREN_CLOSE, 0)

        def nl(self):
            return self.getTypedRuleContext(MiniGoParser.NlContext,0)


        def arglist(self):
            return self.getTypedRuleContext(MiniGoParser.ArglistContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_callstmt




    def callstmt(self):

        localctx = MiniGoParser.CallstmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_callstmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 458
            self.match(MiniGoParser.ID)
            self.state = 459
            self.match(MiniGoParser.PAREN_OPEN)
            self.state = 461
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 258512257024) != 0):
                self.state = 460
                self.arglist()


            self.state = 463
            self.match(MiniGoParser.PAREN_CLOSE)
            self.state = 464
            self.nl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BRACE_OPEN(self):
            return self.getToken(MiniGoParser.BRACE_OPEN, 0)

        def BRACE_CLOSE(self):
            return self.getToken(MiniGoParser.BRACE_CLOSE, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StmtContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StmtContext,i)


        def nl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.NlContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.NlContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_block




    def block(self):

        localctx = MiniGoParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 466
            self.match(MiniGoParser.BRACE_OPEN)
            self.state = 472
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 144955148802) != 0):
                self.state = 467
                self.stmt()
                self.state = 468
                self.nl()
                self.state = 474
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 475
            self.match(MiniGoParser.BRACE_CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PAREN_OPEN(self):
            return self.getToken(MiniGoParser.PAREN_OPEN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ExprContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ExprContext,i)


        def PAREN_CLOSE(self):
            return self.getToken(MiniGoParser.PAREN_CLOSE, 0)

        def INTLIT(self):
            return self.getToken(MiniGoParser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(MiniGoParser.FLOATLIT, 0)

        def STRLIT(self):
            return self.getToken(MiniGoParser.STRLIT, 0)

        def BOOLLIT(self):
            return self.getToken(MiniGoParser.BOOLLIT, 0)

        def NILLIT(self):
            return self.getToken(MiniGoParser.NILLIT, 0)

        def methodcall(self):
            return self.getTypedRuleContext(MiniGoParser.MethodcallContext,0)


        def funccall(self):
            return self.getTypedRuleContext(MiniGoParser.FunccallContext,0)


        def multi_array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Multi_array_literalContext,0)


        def array_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Array_literalContext,0)


        def struct_literal(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_literalContext,0)


        def array_access(self):
            return self.getTypedRuleContext(MiniGoParser.Array_accessContext,0)


        def struct_access(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_accessContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def OP_ARITH(self):
            return self.getToken(MiniGoParser.OP_ARITH, 0)

        def OP_LOGIC(self):
            return self.getToken(MiniGoParser.OP_LOGIC, 0)

        def OP_COMPARE(self):
            return self.getToken(MiniGoParser.OP_COMPARE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 495
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.state = 478
                self.match(MiniGoParser.PAREN_OPEN)
                self.state = 479
                self.expr(0)
                self.state = 480
                self.match(MiniGoParser.PAREN_CLOSE)
                pass

            elif la_ == 2:
                self.state = 482
                self.match(MiniGoParser.INTLIT)
                pass

            elif la_ == 3:
                self.state = 483
                self.match(MiniGoParser.FLOATLIT)
                pass

            elif la_ == 4:
                self.state = 484
                self.match(MiniGoParser.STRLIT)
                pass

            elif la_ == 5:
                self.state = 485
                self.match(MiniGoParser.BOOLLIT)
                pass

            elif la_ == 6:
                self.state = 486
                self.match(MiniGoParser.NILLIT)
                pass

            elif la_ == 7:
                self.state = 487
                self.methodcall()
                pass

            elif la_ == 8:
                self.state = 488
                self.funccall()
                pass

            elif la_ == 9:
                self.state = 489
                self.multi_array_literal()
                pass

            elif la_ == 10:
                self.state = 490
                self.array_literal()
                pass

            elif la_ == 11:
                self.state = 491
                self.struct_literal()
                pass

            elif la_ == 12:
                self.state = 492
                self.array_access()
                pass

            elif la_ == 13:
                self.state = 493
                self.struct_access()
                pass

            elif la_ == 14:
                self.state = 494
                self.match(MiniGoParser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 508
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,47,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 506
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 497
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 498
                        self.match(MiniGoParser.OP_ARITH)
                        self.state = 499
                        self.expr(18)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 500
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 501
                        self.match(MiniGoParser.OP_LOGIC)
                        self.state = 502
                        self.expr(17)
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 503
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 504
                        self.match(MiniGoParser.OP_COMPARE)
                        self.state = 505
                        self.expr(16)
                        pass

             
                self.state = 510
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,47,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class NlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self):
            return self.getToken(MiniGoParser.NEWLINE, 0)

        def SEPARATOR_SEMI(self):
            return self.getToken(MiniGoParser.SEPARATOR_SEMI, 0)

        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_nl




    def nl(self):

        localctx = MiniGoParser.NlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_nl)
        self._la = 0 # Token type
        try:
            self.state = 513
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26, 42]:
                self.enterOuterAlt(localctx, 1)
                self.state = 511
                _la = self._input.LA(1)
                if not(_la==26 or _la==42):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [-1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 512
                self.match(MiniGoParser.EOF)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[39] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 17)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 16)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 15)
         




