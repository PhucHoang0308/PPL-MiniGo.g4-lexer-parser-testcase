# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\62")
        buf.write("\u01fa\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\3\2\3\2\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3")
        buf.write("\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\5\16\u00b7\n\16\3\17\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\17\3\17\5\17\u00c3\n\17\3\20\3\20\3\20")
        buf.write("\3\20\3\20\5\20\u00ca\n\20\3\21\3\21\3\22\3\22\3\23\3")
        buf.write("\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3\27\3\30")
        buf.write("\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\3\34\5\34\u010c\n\34\3\35\3\35\3\35\3")
        buf.write("\35\3\35\3\35\3\35\3\35\3\35\5\35\u0117\n\35\3\36\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3")
        buf.write(" \3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3\"\5\"")
        buf.write("\u0151\n\"\3#\3#\3#\5#\u0156\n#\3$\3$\3%\3%\6%\u015c\n")
        buf.write("%\r%\16%\u015d\5%\u0160\n%\3&\3&\7&\u0164\n&\f&\16&\u0167")
        buf.write("\13&\3\'\3\'\5\'\u016b\n\'\3\'\3\'\3(\3(\3(\3(\5(\u0173")
        buf.write("\n(\3)\3)\7)\u0177\n)\f)\16)\u017a\13)\3)\3)\3*\3*\5*")
        buf.write("\u0180\n*\3+\3+\3+\3+\5+\u0186\n+\3,\3,\3,\3-\3-\7-\u018d")
        buf.write("\n-\f-\16-\u0190\13-\3.\3.\7.\u0194\n.\f.\16.\u0197\13")
        buf.write(".\3.\5.\u019a\n.\3/\3/\3/\6/\u019f\n/\r/\16/\u01a0\3\60")
        buf.write("\3\60\3\60\6\60\u01a6\n\60\r\60\16\60\u01a7\3\61\3\61")
        buf.write("\3\61\6\61\u01ad\n\61\r\61\16\61\u01ae\3\62\7\62\u01b2")
        buf.write("\n\62\f\62\16\62\u01b5\13\62\3\62\5\62\u01b8\n\62\3\62")
        buf.write("\6\62\u01bb\n\62\r\62\16\62\u01bc\3\62\3\62\3\63\6\63")
        buf.write("\u01c2\n\63\r\63\16\63\u01c3\3\63\3\63\3\64\3\64\3\64")
        buf.write("\3\64\3\64\7\64\u01cd\n\64\f\64\16\64\u01d0\13\64\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65\7\65\u01db\n")
        buf.write("\65\f\65\16\65\u01de\13\65\3\65\3\65\3\66\3\66\3\66\3")
        buf.write("\67\3\67\7\67\u01e7\n\67\f\67\16\67\u01ea\13\67\3\67\5")
        buf.write("\67\u01ed\n\67\3\67\3\67\38\38\78\u01f3\n8\f8\168\u01f6")
        buf.write("\138\38\38\38\3\u01ce\29\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36")
        buf.write(";\37= ?!A\"C#E$G\2I\2K\2M\2O%Q&S\2U\2W\2Y\'[(])_*a+c,")
        buf.write("e-g.i/k\60m\61o\62\3\2\24\6\2\'\',-//\61\61\3\2\62;\4")
        buf.write("\2GGgg\4\2--//\5\2\f\f$$^^\7\2$$^^ppttvv\5\2C\\aac|\6")
        buf.write("\2\62;C\\aac|\3\2\63;\4\2DDdd\3\2\62\63\4\2QQqq\3\2\62")
        buf.write("9\4\2ZZzz\5\2\62;CHch\5\2\13\13\16\17\"\"\4\2\f\f\17\17")
        buf.write("\4\3\f\f\17\17\2\u0225\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2")
        buf.write("\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2")
        buf.write("\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2")
        buf.write("\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!")
        buf.write("\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2O\3\2\2\2\2Q\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\3q")
        buf.write("\3\2\2\2\5u\3\2\2\2\7z\3\2\2\2\t\177\3\2\2\2\13\u0086")
        buf.write("\3\2\2\2\r\u0090\3\2\2\2\17\u0096\3\2\2\2\21\u0098\3\2")
        buf.write("\2\2\23\u009a\3\2\2\2\25\u009d\3\2\2\2\27\u00a2\3\2\2")
        buf.write("\2\31\u00a6\3\2\2\2\33\u00b6\3\2\2\2\35\u00c2\3\2\2\2")
        buf.write("\37\u00c9\3\2\2\2!\u00cb\3\2\2\2#\u00cd\3\2\2\2%\u00cf")
        buf.write("\3\2\2\2\'\u00d2\3\2\2\2)\u00d4\3\2\2\2+\u00d6\3\2\2\2")
        buf.write("-\u00d8\3\2\2\2/\u00da\3\2\2\2\61\u00dc\3\2\2\2\63\u00de")
        buf.write("\3\2\2\2\65\u00e0\3\2\2\2\67\u010b\3\2\2\29\u0116\3\2")
        buf.write("\2\2;\u0118\3\2\2\2=\u011c\3\2\2\2?\u0123\3\2\2\2A\u012c")
        buf.write("\3\2\2\2C\u0150\3\2\2\2E\u0152\3\2\2\2G\u0157\3\2\2\2")
        buf.write("I\u015f\3\2\2\2K\u0161\3\2\2\2M\u0168\3\2\2\2O\u0172\3")
        buf.write("\2\2\2Q\u0174\3\2\2\2S\u017f\3\2\2\2U\u0185\3\2\2\2W\u0187")
        buf.write("\3\2\2\2Y\u018a\3\2\2\2[\u0199\3\2\2\2]\u019b\3\2\2\2")
        buf.write("_\u01a2\3\2\2\2a\u01a9\3\2\2\2c\u01ba\3\2\2\2e\u01c1\3")
        buf.write("\2\2\2g\u01c7\3\2\2\2i\u01d6\3\2\2\2k\u01e1\3\2\2\2m\u01e4")
        buf.write("\3\2\2\2o\u01f0\3\2\2\2qr\7x\2\2rs\7c\2\2st\7t\2\2t\4")
        buf.write("\3\2\2\2uv\7h\2\2vw\7w\2\2wx\7p\2\2xy\7e\2\2y\6\3\2\2")
        buf.write("\2z{\7v\2\2{|\7{\2\2|}\7r\2\2}~\7g\2\2~\b\3\2\2\2\177")
        buf.write("\u0080\7u\2\2\u0080\u0081\7v\2\2\u0081\u0082\7t\2\2\u0082")
        buf.write("\u0083\7w\2\2\u0083\u0084\7e\2\2\u0084\u0085\7v\2\2\u0085")
        buf.write("\n\3\2\2\2\u0086\u0087\7k\2\2\u0087\u0088\7p\2\2\u0088")
        buf.write("\u0089\7v\2\2\u0089\u008a\7g\2\2\u008a\u008b\7t\2\2\u008b")
        buf.write("\u008c\7h\2\2\u008c\u008d\7c\2\2\u008d\u008e\7e\2\2\u008e")
        buf.write("\u008f\7g\2\2\u008f\f\3\2\2\2\u0090\u0091\7e\2\2\u0091")
        buf.write("\u0092\7q\2\2\u0092\u0093\7p\2\2\u0093\u0094\7u\2\2\u0094")
        buf.write("\u0095\7v\2\2\u0095\16\3\2\2\2\u0096\u0097\7\60\2\2\u0097")
        buf.write("\20\3\2\2\2\u0098\u0099\7<\2\2\u0099\22\3\2\2\2\u009a")
        buf.write("\u009b\7k\2\2\u009b\u009c\7h\2\2\u009c\24\3\2\2\2\u009d")
        buf.write("\u009e\7g\2\2\u009e\u009f\7n\2\2\u009f\u00a0\7u\2\2\u00a0")
        buf.write("\u00a1\7g\2\2\u00a1\26\3\2\2\2\u00a2\u00a3\7h\2\2\u00a3")
        buf.write("\u00a4\7q\2\2\u00a4\u00a5\7t\2\2\u00a5\30\3\2\2\2\u00a6")
        buf.write("\u00a7\7t\2\2\u00a7\u00a8\7c\2\2\u00a8\u00a9\7p\2\2\u00a9")
        buf.write("\u00aa\7i\2\2\u00aa\u00ab\7g\2\2\u00ab\32\3\2\2\2\u00ac")
        buf.write("\u00ad\7?\2\2\u00ad\u00b7\7?\2\2\u00ae\u00af\7#\2\2\u00af")
        buf.write("\u00b7\7?\2\2\u00b0\u00b7\7>\2\2\u00b1\u00b2\7>\2\2\u00b2")
        buf.write("\u00b7\7?\2\2\u00b3\u00b7\7@\2\2\u00b4\u00b5\7@\2\2\u00b5")
        buf.write("\u00b7\7?\2\2\u00b6\u00ac\3\2\2\2\u00b6\u00ae\3\2\2\2")
        buf.write("\u00b6\u00b0\3\2\2\2\u00b6\u00b1\3\2\2\2\u00b6\u00b3\3")
        buf.write("\2\2\2\u00b6\u00b4\3\2\2\2\u00b7\34\3\2\2\2\u00b8\u00b9")
        buf.write("\7-\2\2\u00b9\u00c3\7?\2\2\u00ba\u00bb\7/\2\2\u00bb\u00c3")
        buf.write("\7?\2\2\u00bc\u00bd\7,\2\2\u00bd\u00c3\7?\2\2\u00be\u00bf")
        buf.write("\7\61\2\2\u00bf\u00c3\7?\2\2\u00c0\u00c1\7\'\2\2\u00c1")
        buf.write("\u00c3\7?\2\2\u00c2\u00b8\3\2\2\2\u00c2\u00ba\3\2\2\2")
        buf.write("\u00c2\u00bc\3\2\2\2\u00c2\u00be\3\2\2\2\u00c2\u00c0\3")
        buf.write("\2\2\2\u00c3\36\3\2\2\2\u00c4\u00c5\7(\2\2\u00c5\u00ca")
        buf.write("\7(\2\2\u00c6\u00c7\7~\2\2\u00c7\u00ca\7~\2\2\u00c8\u00ca")
        buf.write("\7#\2\2\u00c9\u00c4\3\2\2\2\u00c9\u00c6\3\2\2\2\u00c9")
        buf.write("\u00c8\3\2\2\2\u00ca \3\2\2\2\u00cb\u00cc\t\2\2\2\u00cc")
        buf.write("\"\3\2\2\2\u00cd\u00ce\7?\2\2\u00ce$\3\2\2\2\u00cf\u00d0")
        buf.write("\7<\2\2\u00d0\u00d1\7?\2\2\u00d1&\3\2\2\2\u00d2\u00d3")
        buf.write("\7*\2\2\u00d3(\3\2\2\2\u00d4\u00d5\7+\2\2\u00d5*\3\2\2")
        buf.write("\2\u00d6\u00d7\7}\2\2\u00d7,\3\2\2\2\u00d8\u00d9\7\177")
        buf.write("\2\2\u00d9.\3\2\2\2\u00da\u00db\7]\2\2\u00db\60\3\2\2")
        buf.write("\2\u00dc\u00dd\7_\2\2\u00dd\62\3\2\2\2\u00de\u00df\7.")
        buf.write("\2\2\u00df\64\3\2\2\2\u00e0\u00e1\7=\2\2\u00e1\66\3\2")
        buf.write("\2\2\u00e2\u00e3\7k\2\2\u00e3\u00e4\7p\2\2\u00e4\u010c")
        buf.write("\7v\2\2\u00e5\u00e6\7h\2\2\u00e6\u00e7\7n\2\2\u00e7\u00e8")
        buf.write("\7q\2\2\u00e8\u00e9\7c\2\2\u00e9\u010c\7v\2\2\u00ea\u00eb")
        buf.write("\7d\2\2\u00eb\u00ec\7q\2\2\u00ec\u00ed\7q\2\2\u00ed\u00ee")
        buf.write("\7n\2\2\u00ee\u00ef\7g\2\2\u00ef\u00f0\7c\2\2\u00f0\u010c")
        buf.write("\7p\2\2\u00f1\u00f2\7u\2\2\u00f2\u00f3\7v\2\2\u00f3\u00f4")
        buf.write("\7t\2\2\u00f4\u00f5\7k\2\2\u00f5\u00f6\7p\2\2\u00f6\u010c")
        buf.write("\7i\2\2\u00f7\u00f8\7c\2\2\u00f8\u00f9\7t\2\2\u00f9\u00fa")
        buf.write("\7t\2\2\u00fa\u00fb\7c\2\2\u00fb\u010c\7{\2\2\u00fc\u00fd")
        buf.write("\7u\2\2\u00fd\u00fe\7v\2\2\u00fe\u00ff\7t\2\2\u00ff\u0100")
        buf.write("\7w\2\2\u0100\u0101\7e\2\2\u0101\u010c\7v\2\2\u0102\u0103")
        buf.write("\7k\2\2\u0103\u0104\7p\2\2\u0104\u0105\7v\2\2\u0105\u0106")
        buf.write("\7g\2\2\u0106\u0107\7t\2\2\u0107\u0108\7h\2\2\u0108\u0109")
        buf.write("\7c\2\2\u0109\u010a\7e\2\2\u010a\u010c\7g\2\2\u010b\u00e2")
        buf.write("\3\2\2\2\u010b\u00e5\3\2\2\2\u010b\u00ea\3\2\2\2\u010b")
        buf.write("\u00f1\3\2\2\2\u010b\u00f7\3\2\2\2\u010b\u00fc\3\2\2\2")
        buf.write("\u010b\u0102\3\2\2\2\u010c8\3\2\2\2\u010d\u010e\7v\2\2")
        buf.write("\u010e\u010f\7t\2\2\u010f\u0110\7w\2\2\u0110\u0117\7g")
        buf.write("\2\2\u0111\u0112\7h\2\2\u0112\u0113\7c\2\2\u0113\u0114")
        buf.write("\7n\2\2\u0114\u0115\7u\2\2\u0115\u0117\7g\2\2\u0116\u010d")
        buf.write("\3\2\2\2\u0116\u0111\3\2\2\2\u0117:\3\2\2\2\u0118\u0119")
        buf.write("\7p\2\2\u0119\u011a\7k\2\2\u011a\u011b\7n\2\2\u011b<\3")
        buf.write("\2\2\2\u011c\u011d\7t\2\2\u011d\u011e\7g\2\2\u011e\u011f")
        buf.write("\7v\2\2\u011f\u0120\7w\2\2\u0120\u0121\7t\2\2\u0121\u0122")
        buf.write("\7p\2\2\u0122>\3\2\2\2\u0123\u0124\7e\2\2\u0124\u0125")
        buf.write("\7q\2\2\u0125\u0126\7p\2\2\u0126\u0127\7v\2\2\u0127\u0128")
        buf.write("\7k\2\2\u0128\u0129\7p\2\2\u0129\u012a\7w\2\2\u012a\u012b")
        buf.write("\7g\2\2\u012b@\3\2\2\2\u012c\u012d\7d\2\2\u012d\u012e")
        buf.write("\7t\2\2\u012e\u012f\7g\2\2\u012f\u0130\7c\2\2\u0130\u0131")
        buf.write("\7m\2\2\u0131B\3\2\2\2\u0132\u0133\7k\2\2\u0133\u0151")
        buf.write("\7h\2\2\u0134\u0135\7g\2\2\u0135\u0136\7n\2\2\u0136\u0137")
        buf.write("\7u\2\2\u0137\u0151\7g\2\2\u0138\u0139\7h\2\2\u0139\u013a")
        buf.write("\7q\2\2\u013a\u0151\7t\2\2\u013b\u013c\7h\2\2\u013c\u013d")
        buf.write("\7w\2\2\u013d\u013e\7p\2\2\u013e\u0151\7e\2\2\u013f\u0140")
        buf.write("\7v\2\2\u0140\u0141\7{\2\2\u0141\u0142\7r\2\2\u0142\u0151")
        buf.write("\7g\2\2\u0143\u0144\7e\2\2\u0144\u0145\7q\2\2\u0145\u0146")
        buf.write("\7p\2\2\u0146\u0147\7u\2\2\u0147\u0151\7v\2\2\u0148\u0149")
        buf.write("\7x\2\2\u0149\u014a\7c\2\2\u014a\u0151\7t\2\2\u014b\u014c")
        buf.write("\7t\2\2\u014c\u014d\7c\2\2\u014d\u014e\7p\2\2\u014e\u014f")
        buf.write("\7i\2\2\u014f\u0151\7g\2\2\u0150\u0132\3\2\2\2\u0150\u0134")
        buf.write("\3\2\2\2\u0150\u0138\3\2\2\2\u0150\u013b\3\2\2\2\u0150")
        buf.write("\u013f\3\2\2\2\u0150\u0143\3\2\2\2\u0150\u0148\3\2\2\2")
        buf.write("\u0150\u014b\3\2\2\2\u0151D\3\2\2\2\u0152\u0153\5I%\2")
        buf.write("\u0153\u0155\5K&\2\u0154\u0156\5M\'\2\u0155\u0154\3\2")
        buf.write("\2\2\u0155\u0156\3\2\2\2\u0156F\3\2\2\2\u0157\u0158\t")
        buf.write("\3\2\2\u0158H\3\2\2\2\u0159\u0160\7\62\2\2\u015a\u015c")
        buf.write("\5G$\2\u015b\u015a\3\2\2\2\u015c\u015d\3\2\2\2\u015d\u015b")
        buf.write("\3\2\2\2\u015d\u015e\3\2\2\2\u015e\u0160\3\2\2\2\u015f")
        buf.write("\u0159\3\2\2\2\u015f\u015b\3\2\2\2\u0160J\3\2\2\2\u0161")
        buf.write("\u0165\7\60\2\2\u0162\u0164\5G$\2\u0163\u0162\3\2\2\2")
        buf.write("\u0164\u0167\3\2\2\2\u0165\u0163\3\2\2\2\u0165\u0166\3")
        buf.write("\2\2\2\u0166L\3\2\2\2\u0167\u0165\3\2\2\2\u0168\u016a")
        buf.write("\t\4\2\2\u0169\u016b\t\5\2\2\u016a\u0169\3\2\2\2\u016a")
        buf.write("\u016b\3\2\2\2\u016b\u016c\3\2\2\2\u016c\u016d\5I%\2\u016d")
        buf.write("N\3\2\2\2\u016e\u0173\5[.\2\u016f\u0173\5]/\2\u0170\u0173")
        buf.write("\5_\60\2\u0171\u0173\5a\61\2\u0172\u016e\3\2\2\2\u0172")
        buf.write("\u016f\3\2\2\2\u0172\u0170\3\2\2\2\u0172\u0171\3\2\2\2")
        buf.write("\u0173P\3\2\2\2\u0174\u0178\7$\2\2\u0175\u0177\5S*\2\u0176")
        buf.write("\u0175\3\2\2\2\u0177\u017a\3\2\2\2\u0178\u0176\3\2\2\2")
        buf.write("\u0178\u0179\3\2\2\2\u0179\u017b\3\2\2\2\u017a\u0178\3")
        buf.write("\2\2\2\u017b\u017c\7$\2\2\u017cR\3\2\2\2\u017d\u0180\n")
        buf.write("\6\2\2\u017e\u0180\5U+\2\u017f\u017d\3\2\2\2\u017f\u017e")
        buf.write("\3\2\2\2\u0180T\3\2\2\2\u0181\u0182\7^\2\2\u0182\u0186")
        buf.write("\t\7\2\2\u0183\u0184\7)\2\2\u0184\u0186\7$\2\2\u0185\u0181")
        buf.write("\3\2\2\2\u0185\u0183\3\2\2\2\u0186V\3\2\2\2\u0187\u0188")
        buf.write("\7^\2\2\u0188\u0189\n\7\2\2\u0189X\3\2\2\2\u018a\u018e")
        buf.write("\t\b\2\2\u018b\u018d\t\t\2\2\u018c\u018b\3\2\2\2\u018d")
        buf.write("\u0190\3\2\2\2\u018e\u018c\3\2\2\2\u018e\u018f\3\2\2\2")
        buf.write("\u018fZ\3\2\2\2\u0190\u018e\3\2\2\2\u0191\u0195\t\n\2")
        buf.write("\2\u0192\u0194\t\3\2\2\u0193\u0192\3\2\2\2\u0194\u0197")
        buf.write("\3\2\2\2\u0195\u0193\3\2\2\2\u0195\u0196\3\2\2\2\u0196")
        buf.write("\u019a\3\2\2\2\u0197\u0195\3\2\2\2\u0198\u019a\7\62\2")
        buf.write("\2\u0199\u0191\3\2\2\2\u0199\u0198\3\2\2\2\u019a\\\3\2")
        buf.write("\2\2\u019b\u019c\7\62\2\2\u019c\u019e\t\13\2\2\u019d\u019f")
        buf.write("\t\f\2\2\u019e\u019d\3\2\2\2\u019f\u01a0\3\2\2\2\u01a0")
        buf.write("\u019e\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1^\3\2\2\2\u01a2")
        buf.write("\u01a3\7\62\2\2\u01a3\u01a5\t\r\2\2\u01a4\u01a6\t\16\2")
        buf.write("\2\u01a5\u01a4\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7\u01a5")
        buf.write("\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8`\3\2\2\2\u01a9\u01aa")
        buf.write("\7\62\2\2\u01aa\u01ac\t\17\2\2\u01ab\u01ad\t\20\2\2\u01ac")
        buf.write("\u01ab\3\2\2\2\u01ad\u01ae\3\2\2\2\u01ae\u01ac\3\2\2\2")
        buf.write("\u01ae\u01af\3\2\2\2\u01afb\3\2\2\2\u01b0\u01b2\7\"\2")
        buf.write("\2\u01b1\u01b0\3\2\2\2\u01b2\u01b5\3\2\2\2\u01b3\u01b1")
        buf.write("\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4\u01b7\3\2\2\2\u01b5")
        buf.write("\u01b3\3\2\2\2\u01b6\u01b8\7\17\2\2\u01b7\u01b6\3\2\2")
        buf.write("\2\u01b7\u01b8\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b9\u01bb")
        buf.write("\7\f\2\2\u01ba\u01b3\3\2\2\2\u01bb\u01bc\3\2\2\2\u01bc")
        buf.write("\u01ba\3\2\2\2\u01bc\u01bd\3\2\2\2\u01bd\u01be\3\2\2\2")
        buf.write("\u01be\u01bf\b\62\2\2\u01bfd\3\2\2\2\u01c0\u01c2\t\21")
        buf.write("\2\2\u01c1\u01c0\3\2\2\2\u01c2\u01c3\3\2\2\2\u01c3\u01c1")
        buf.write("\3\2\2\2\u01c3\u01c4\3\2\2\2\u01c4\u01c5\3\2\2\2\u01c5")
        buf.write("\u01c6\b\63\3\2\u01c6f\3\2\2\2\u01c7\u01c8\7\61\2\2\u01c8")
        buf.write("\u01c9\7,\2\2\u01c9\u01ce\3\2\2\2\u01ca\u01cd\5g\64\2")
        buf.write("\u01cb\u01cd\13\2\2\2\u01cc\u01ca\3\2\2\2\u01cc\u01cb")
        buf.write("\3\2\2\2\u01cd\u01d0\3\2\2\2\u01ce\u01cf\3\2\2\2\u01ce")
        buf.write("\u01cc\3\2\2\2\u01cf\u01d1\3\2\2\2\u01d0\u01ce\3\2\2\2")
        buf.write("\u01d1\u01d2\7,\2\2\u01d2\u01d3\7\61\2\2\u01d3\u01d4\3")
        buf.write("\2\2\2\u01d4\u01d5\b\64\3\2\u01d5h\3\2\2\2\u01d6\u01d7")
        buf.write("\7\61\2\2\u01d7\u01d8\7\61\2\2\u01d8\u01dc\3\2\2\2\u01d9")
        buf.write("\u01db\n\22\2\2\u01da\u01d9\3\2\2\2\u01db\u01de\3\2\2")
        buf.write("\2\u01dc\u01da\3\2\2\2\u01dc\u01dd\3\2\2\2\u01dd\u01df")
        buf.write("\3\2\2\2\u01de\u01dc\3\2\2\2\u01df\u01e0\b\65\3\2\u01e0")
        buf.write("j\3\2\2\2\u01e1\u01e2\13\2\2\2\u01e2\u01e3\b\66\4\2\u01e3")
        buf.write("l\3\2\2\2\u01e4\u01e8\7$\2\2\u01e5\u01e7\5S*\2\u01e6\u01e5")
        buf.write("\3\2\2\2\u01e7\u01ea\3\2\2\2\u01e8\u01e6\3\2\2\2\u01e8")
        buf.write("\u01e9\3\2\2\2\u01e9\u01ec\3\2\2\2\u01ea\u01e8\3\2\2\2")
        buf.write("\u01eb\u01ed\t\23\2\2\u01ec\u01eb\3\2\2\2\u01ed\u01ee")
        buf.write("\3\2\2\2\u01ee\u01ef\b\67\5\2\u01efn\3\2\2\2\u01f0\u01f4")
        buf.write("\7$\2\2\u01f1\u01f3\5S*\2\u01f2\u01f1\3\2\2\2\u01f3\u01f6")
        buf.write("\3\2\2\2\u01f4\u01f2\3\2\2\2\u01f4\u01f5\3\2\2\2\u01f5")
        buf.write("\u01f7\3\2\2\2\u01f6\u01f4\3\2\2\2\u01f7\u01f8\5W,\2\u01f8")
        buf.write("\u01f9\b8\6\2\u01f9p\3\2\2\2\"\2\u00b6\u00c2\u00c9\u010b")
        buf.write("\u0116\u0150\u0155\u015d\u015f\u0165\u016a\u0172\u0178")
        buf.write("\u017f\u0185\u018e\u0195\u0199\u01a0\u01a7\u01ae\u01b3")
        buf.write("\u01b7\u01bc\u01c3\u01cc\u01ce\u01dc\u01e8\u01ec\u01f4")
        buf.write("\7\3\62\2\b\2\2\3\66\3\3\67\4\38\5")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    OP_COMPARE = 13
    OP_ASSIGN = 14
    OP_LOGIC = 15
    OP_ARITH = 16
    OP_EQUAL = 17
    OP_ASSEQ = 18
    PAREN_OPEN = 19
    PAREN_CLOSE = 20
    BRACE_OPEN = 21
    BRACE_CLOSE = 22
    BRACK_OPEN = 23
    BRACK_CLOSE = 24
    SEPARATOR_COMMA = 25
    SEPARATOR_SEMI = 26
    TYPE = 27
    BOOLLIT = 28
    NILLIT = 29
    RETURN = 30
    CONTINUE = 31
    BREAK = 32
    KEYWORD = 33
    FLOATLIT = 34
    INTLIT = 35
    STRLIT = 36
    ID = 37
    DECIMAL_LITERAL = 38
    BINARY_LITERAL = 39
    OCTAL_LITERAL = 40
    HEXADECIMAL_LITERAL = 41
    NEWLINE = 42
    WS = 43
    MULTILINE_COMMENT = 44
    COMMENT = 45
    ERROR_CHAR = 46
    UNCLOSE_STRING = 47
    ILLEGAL_ESCAPE = 48

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'var'", "'func'", "'type'", "'struct'", "'interface'", "'const'", 
            "'.'", "':'", "'if'", "'else'", "'for'", "'range'", "'='", "':='", 
            "'('", "')'", "'{'", "'}'", "'['", "']'", "','", "';'", "'nil'", 
            "'return'", "'continue'", "'break'" ]

    symbolicNames = [ "<INVALID>",
            "OP_COMPARE", "OP_ASSIGN", "OP_LOGIC", "OP_ARITH", "OP_EQUAL", 
            "OP_ASSEQ", "PAREN_OPEN", "PAREN_CLOSE", "BRACE_OPEN", "BRACE_CLOSE", 
            "BRACK_OPEN", "BRACK_CLOSE", "SEPARATOR_COMMA", "SEPARATOR_SEMI", 
            "TYPE", "BOOLLIT", "NILLIT", "RETURN", "CONTINUE", "BREAK", 
            "KEYWORD", "FLOATLIT", "INTLIT", "STRLIT", "ID", "DECIMAL_LITERAL", 
            "BINARY_LITERAL", "OCTAL_LITERAL", "HEXADECIMAL_LITERAL", "NEWLINE", 
            "WS", "MULTILINE_COMMENT", "COMMENT", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "OP_COMPARE", 
                  "OP_ASSIGN", "OP_LOGIC", "OP_ARITH", "OP_EQUAL", "OP_ASSEQ", 
                  "PAREN_OPEN", "PAREN_CLOSE", "BRACE_OPEN", "BRACE_CLOSE", 
                  "BRACK_OPEN", "BRACK_CLOSE", "SEPARATOR_COMMA", "SEPARATOR_SEMI", 
                  "TYPE", "BOOLLIT", "NILLIT", "RETURN", "CONTINUE", "BREAK", 
                  "KEYWORD", "FLOATLIT", "DIGIT", "DIGITS", "FRAC", "EXP", 
                  "INTLIT", "STRLIT", "STRING_CHAR", "ESC_SEQ", "ESC_ILLEGAL", 
                  "ID", "DECIMAL_LITERAL", "BINARY_LITERAL", "OCTAL_LITERAL", 
                  "HEXADECIMAL_LITERAL", "NEWLINE", "WS", "MULTILINE_COMMENT", 
                  "COMMENT", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    preType = None
    def emit(self):
        tk = self.type
        if tk == self.UNCLOSE_STRING:       
            result = super().emit();
            raise UncloseString(result.text);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text); 
        else:
            self.preType = tk
            print("preType hiện tại:", self.preType, " text:", self.text)
            return super().emit();


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[48] = self.NEWLINE_action 
            actions[52] = self.ERROR_CHAR_action 
            actions[53] = self.UNCLOSE_STRING_action 
            actions[54] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def NEWLINE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                        if self.preType in [
                            MiniGoLexer.ID,
                            MiniGoLexer.INTLIT,
                            MiniGoLexer.FLOATLIT,
                            MiniGoLexer.STRLIT,
                            MiniGoLexer.BOOLLIT,
                            MiniGoLexer.NILLIT,     
                            MiniGoLexer.TYPE,
                            MiniGoLexer.RETURN,
                            MiniGoLexer.CONTINUE,
                            MiniGoLexer.BREAK,
                            MiniGoLexer.PAREN_CLOSE,
                            MiniGoLexer.BRACK_CLOSE,
                            MiniGoLexer.BRACE_CLOSE,
                        ]:
                            self.text = ';'
                        else:
                            self.skip()
                     
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                self.text = self.text.rstrip('\r\n')  
                raise UncloseString(self.text)

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                raise IllegalEscape(self.text[:])

     


