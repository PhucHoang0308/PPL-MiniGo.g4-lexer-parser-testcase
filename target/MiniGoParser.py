# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\62")
        buf.write("\u0206\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\3\2\7\2V\n\2\f\2\16\2Y\13")
        buf.write("\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\5\3c\n\3\3\4\3\4\3")
        buf.write("\4\5\4h\n\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4s\n")
        buf.write("\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\5\6|\n\6\3\6\3\6\3\6\5")
        buf.write("\6\u0081\n\6\3\6\3\6\5\6\u0085\n\6\3\6\3\6\7\6\u0089\n")
        buf.write("\6\f\6\16\6\u008c\13\6\3\6\5\6\u008f\n\6\3\6\3\6\3\6\3")
        buf.write("\7\3\7\3\7\3\7\3\7\6\7\u0099\n\7\r\7\16\7\u009a\3\7\3")
        buf.write("\7\3\7\3\b\3\b\3\b\3\b\3\b\7\b\u00a5\n\b\f\b\16\b\u00a8")
        buf.write("\13\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\5\t\u00b2\n\t\3")
        buf.write("\n\3\n\5\n\u00b6\n\n\3\13\3\13\3\13\6\13\u00bb\n\13\r")
        buf.write("\13\16\13\u00bc\3\13\3\13\3\f\3\f\3\r\3\r\3\r\3\r\3\r")
        buf.write("\7\r\u00c8\n\r\f\r\16\r\u00cb\13\r\3\r\3\r\3\r\3\16\3")
        buf.write("\16\3\16\5\16\u00d3\n\16\3\16\3\16\5\16\u00d7\n\16\3\16")
        buf.write("\3\16\3\17\3\17\3\17\7\17\u00de\n\17\f\17\16\17\u00e1")
        buf.write("\13\17\3\20\3\20\3\20\7\20\u00e6\n\20\f\20\16\20\u00e9")
        buf.write("\13\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3")
        buf.write("\22\3\22\3\22\6\22\u00f7\n\22\r\22\16\22\u00f8\3\23\3")
        buf.write("\23\5\23\u00fd\n\23\3\23\3\23\3\23\5\23\u0102\n\23\3\24")
        buf.write("\3\24\3\24\3\24\6\24\u0108\n\24\r\24\16\24\u0109\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\7\24\u0112\n\24\f\24\16\24\u0115")
        buf.write("\13\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\7\24\u011e\n")
        buf.write("\24\f\24\16\24\u0121\13\24\3\24\3\24\6\24\u0125\n\24\r")
        buf.write("\24\16\24\u0126\3\24\3\24\3\25\3\25\3\25\3\25\6\25\u012f")
        buf.write("\n\25\r\25\16\25\u0130\3\25\3\25\3\25\3\25\3\25\7\25\u0138")
        buf.write("\n\25\f\25\16\25\u013b\13\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\5\26\u0142\n\26\3\26\3\26\3\27\3\27\3\27\7\27\u0149\n")
        buf.write("\27\f\27\16\27\u014c\13\27\3\30\3\30\3\30\3\30\3\31\3")
        buf.write("\31\3\31\5\31\u0155\n\31\3\31\3\31\3\32\3\32\3\32\7\32")
        buf.write("\u015c\n\32\f\32\16\32\u015f\13\32\3\33\3\33\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34\u016d\n")
        buf.write("\34\3\35\3\35\3\35\5\35\u0172\n\35\3\35\3\35\3\35\3\35")
        buf.write("\3\36\3\36\3\36\3\36\7\36\u017c\n\36\f\36\16\36\u017f")
        buf.write("\13\36\3\36\5\36\u0182\n\36\3\36\3\36\3\36\3\36\3\36\3")
        buf.write("\36\7\36\u018a\n\36\f\36\16\36\u018d\13\36\3\36\5\36\u0190")
        buf.write("\n\36\5\36\u0192\n\36\3\37\3\37\3\37\3\37\3\37\3\37\3")
        buf.write("\37\3\37\3\37\3\37\3\37\3\37\5\37\u01a0\n\37\3 \3 \3 ")
        buf.write("\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3")
        buf.write("!\3!\3!\5!\u01b9\n!\3\"\3\"\5\"\u01bd\n\"\3#\3#\3$\3$")
        buf.write("\3$\3%\3%\3%\3&\3&\5&\u01c9\n&\3&\3&\3\'\3\'\3\'\5\'\u01d0")
        buf.write("\n\'\3\'\3\'\3\'\3(\3(\3(\3(\7(\u01d9\n(\f(\16(\u01dc")
        buf.write("\13(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3")
        buf.write(")\3)\3)\3)\5)\u01f2\n)\3)\3)\3)\3)\3)\3)\3)\3)\3)\7)\u01fd")
        buf.write("\n)\f)\16)\u0200\13)\3*\3*\5*\u0204\n*\3*\2\3P+\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\66")
        buf.write("8:<>@BDFHJLNPR\2\5\4\2\35\35\'\'\4\2\20\20\23\24\4\2\34")
        buf.write("\34,,\2\u0226\2W\3\2\2\2\4b\3\2\2\2\6r\3\2\2\2\bt\3\2")
        buf.write("\2\2\ny\3\2\2\2\f\u0093\3\2\2\2\16\u009f\3\2\2\2\20\u00ac")
        buf.write("\3\2\2\2\22\u00b5\3\2\2\2\24\u00ba\3\2\2\2\26\u00c0\3")
        buf.write("\2\2\2\30\u00c2\3\2\2\2\32\u00cf\3\2\2\2\34\u00da\3\2")
        buf.write("\2\2\36\u00e2\3\2\2\2 \u00ec\3\2\2\2\"\u00f2\3\2\2\2$")
        buf.write("\u00fc\3\2\2\2&\u0107\3\2\2\2(\u012e\3\2\2\2*\u013e\3")
        buf.write("\2\2\2,\u0145\3\2\2\2.\u014d\3\2\2\2\60\u0151\3\2\2\2")
        buf.write("\62\u0158\3\2\2\2\64\u0160\3\2\2\2\66\u016c\3\2\2\28\u0171")
        buf.write("\3\2\2\2:\u0191\3\2\2\2<\u019f\3\2\2\2>\u01a1\3\2\2\2")
        buf.write("@\u01b8\3\2\2\2B\u01bc\3\2\2\2D\u01be\3\2\2\2F\u01c0\3")
        buf.write("\2\2\2H\u01c3\3\2\2\2J\u01c6\3\2\2\2L\u01cc\3\2\2\2N\u01d4")
        buf.write("\3\2\2\2P\u01f1\3\2\2\2R\u0203\3\2\2\2TV\5\4\3\2UT\3\2")
        buf.write("\2\2VY\3\2\2\2WU\3\2\2\2WX\3\2\2\2XZ\3\2\2\2YW\3\2\2\2")
        buf.write("Z[\7\2\2\3[\3\3\2\2\2\\c\5\66\34\2]c\5\n\6\2^c\5\f\7\2")
        buf.write("_c\5\16\b\2`c\5\30\r\2ac\5 \21\2b\\\3\2\2\2b]\3\2\2\2")
        buf.write("b^\3\2\2\2b_\3\2\2\2b`\3\2\2\2ba\3\2\2\2c\5\3\2\2\2de")
        buf.write("\7\3\2\2eg\7\'\2\2fh\5\22\n\2gf\3\2\2\2gh\3\2\2\2hi\3")
        buf.write("\2\2\2ij\7\23\2\2jk\5P)\2kl\5R*\2ls\3\2\2\2mn\7\3\2\2")
        buf.write("no\7\'\2\2op\5\22\n\2pq\5R*\2qs\3\2\2\2rd\3\2\2\2rm\3")
        buf.write("\2\2\2s\7\3\2\2\2tu\7\25\2\2uv\7\'\2\2vw\5\22\n\2wx\7")
        buf.write("\26\2\2x\t\3\2\2\2y{\7\4\2\2z|\5\b\5\2{z\3\2\2\2{|\3\2")
        buf.write("\2\2|}\3\2\2\2}~\7\'\2\2~\u0080\7\25\2\2\177\u0081\5\34")
        buf.write("\17\2\u0080\177\3\2\2\2\u0080\u0081\3\2\2\2\u0081\u0082")
        buf.write("\3\2\2\2\u0082\u0084\7\26\2\2\u0083\u0085\5\22\n\2\u0084")
        buf.write("\u0083\3\2\2\2\u0084\u0085\3\2\2\2\u0085\u0086\3\2\2\2")
        buf.write("\u0086\u008a\7\27\2\2\u0087\u0089\5\66\34\2\u0088\u0087")
        buf.write("\3\2\2\2\u0089\u008c\3\2\2\2\u008a\u0088\3\2\2\2\u008a")
        buf.write("\u008b\3\2\2\2\u008b\u008e\3\2\2\2\u008c\u008a\3\2\2\2")
        buf.write("\u008d\u008f\5J&\2\u008e\u008d\3\2\2\2\u008e\u008f\3\2")
        buf.write("\2\2\u008f\u0090\3\2\2\2\u0090\u0091\7\30\2\2\u0091\u0092")
        buf.write("\5R*\2\u0092\13\3\2\2\2\u0093\u0094\7\3\2\2\u0094\u0098")
        buf.write("\7\'\2\2\u0095\u0096\7\31\2\2\u0096\u0097\7%\2\2\u0097")
        buf.write("\u0099\7\32\2\2\u0098\u0095\3\2\2\2\u0099\u009a\3\2\2")
        buf.write("\2\u009a\u0098\3\2\2\2\u009a\u009b\3\2\2\2\u009b\u009c")
        buf.write("\3\2\2\2\u009c\u009d\5\22\n\2\u009d\u009e\5R*\2\u009e")
        buf.write("\r\3\2\2\2\u009f\u00a0\7\5\2\2\u00a0\u00a1\7\'\2\2\u00a1")
        buf.write("\u00a2\7\6\2\2\u00a2\u00a6\7\27\2\2\u00a3\u00a5\5\20\t")
        buf.write("\2\u00a4\u00a3\3\2\2\2\u00a5\u00a8\3\2\2\2\u00a6\u00a4")
        buf.write("\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7\u00a9\3\2\2\2\u00a8")
        buf.write("\u00a6\3\2\2\2\u00a9\u00aa\7\30\2\2\u00aa\u00ab\5R*\2")
        buf.write("\u00ab\17\3\2\2\2\u00ac\u00ad\7\'\2\2\u00ad\u00ae\5\22")
        buf.write("\n\2\u00ae\u00b1\3\2\2\2\u00af\u00b2\7\34\2\2\u00b0\u00b2")
        buf.write("\5R*\2\u00b1\u00af\3\2\2\2\u00b1\u00b0\3\2\2\2\u00b2\21")
        buf.write("\3\2\2\2\u00b3\u00b6\5\24\13\2\u00b4\u00b6\5\26\f\2\u00b5")
        buf.write("\u00b3\3\2\2\2\u00b5\u00b4\3\2\2\2\u00b6\23\3\2\2\2\u00b7")
        buf.write("\u00b8\7\31\2\2\u00b8\u00b9\7%\2\2\u00b9\u00bb\7\32\2")
        buf.write("\2\u00ba\u00b7\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\u00ba")
        buf.write("\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd\u00be\3\2\2\2\u00be")
        buf.write("\u00bf\5\26\f\2\u00bf\25\3\2\2\2\u00c0\u00c1\t\2\2\2\u00c1")
        buf.write("\27\3\2\2\2\u00c2\u00c3\7\5\2\2\u00c3\u00c4\7\'\2\2\u00c4")
        buf.write("\u00c5\7\7\2\2\u00c5\u00c9\7\27\2\2\u00c6\u00c8\5\32\16")
        buf.write("\2\u00c7\u00c6\3\2\2\2\u00c8\u00cb\3\2\2\2\u00c9\u00c7")
        buf.write("\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca\u00cc\3\2\2\2\u00cb")
        buf.write("\u00c9\3\2\2\2\u00cc\u00cd\7\30\2\2\u00cd\u00ce\5R*\2")
        buf.write("\u00ce\31\3\2\2\2\u00cf\u00d0\7\'\2\2\u00d0\u00d2\7\25")
        buf.write("\2\2\u00d1\u00d3\5\34\17\2\u00d2\u00d1\3\2\2\2\u00d2\u00d3")
        buf.write("\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4\u00d6\7\26\2\2\u00d5")
        buf.write("\u00d7\5\22\n\2\u00d6\u00d5\3\2\2\2\u00d6\u00d7\3\2\2")
        buf.write("\2\u00d7\u00d8\3\2\2\2\u00d8\u00d9\5R*\2\u00d9\33\3\2")
        buf.write("\2\2\u00da\u00df\5\36\20\2\u00db\u00dc\7\33\2\2\u00dc")
        buf.write("\u00de\5\36\20\2\u00dd\u00db\3\2\2\2\u00de\u00e1\3\2\2")
        buf.write("\2\u00df\u00dd\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0\35\3")
        buf.write("\2\2\2\u00e1\u00df\3\2\2\2\u00e2\u00e7\7\'\2\2\u00e3\u00e4")
        buf.write("\7\33\2\2\u00e4\u00e6\7\'\2\2\u00e5\u00e3\3\2\2\2\u00e6")
        buf.write("\u00e9\3\2\2\2\u00e7\u00e5\3\2\2\2\u00e7\u00e8\3\2\2\2")
        buf.write("\u00e8\u00ea\3\2\2\2\u00e9\u00e7\3\2\2\2\u00ea\u00eb\5")
        buf.write("\22\n\2\u00eb\37\3\2\2\2\u00ec\u00ed\7\b\2\2\u00ed\u00ee")
        buf.write("\7\'\2\2\u00ee\u00ef\7\23\2\2\u00ef\u00f0\5P)\2\u00f0")
        buf.write("\u00f1\5R*\2\u00f1!\3\2\2\2\u00f2\u00f6\7\'\2\2\u00f3")
        buf.write("\u00f4\7\31\2\2\u00f4\u00f5\7%\2\2\u00f5\u00f7\7\32\2")
        buf.write("\2\u00f6\u00f3\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8\u00f6")
        buf.write("\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f9#\3\2\2\2\u00fa\u00fd")
        buf.write("\7\'\2\2\u00fb\u00fd\5\"\22\2\u00fc\u00fa\3\2\2\2\u00fc")
        buf.write("\u00fb\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe\u0101\7\t\2\2")
        buf.write("\u00ff\u0102\7\'\2\2\u0100\u0102\5\"\22\2\u0101\u00ff")
        buf.write("\3\2\2\2\u0101\u0100\3\2\2\2\u0102%\3\2\2\2\u0103\u0104")
        buf.write("\7\31\2\2\u0104\u0105\5P)\2\u0105\u0106\7\32\2\2\u0106")
        buf.write("\u0108\3\2\2\2\u0107\u0103\3\2\2\2\u0108\u0109\3\2\2\2")
        buf.write("\u0109\u0107\3\2\2\2\u0109\u010a\3\2\2\2\u010a\u010b\3")
        buf.write("\2\2\2\u010b\u010c\5\22\n\2\u010c\u010d\7\27\2\2\u010d")
        buf.write("\u010e\7\27\2\2\u010e\u0113\5P)\2\u010f\u0110\7\33\2\2")
        buf.write("\u0110\u0112\5P)\2\u0111\u010f\3\2\2\2\u0112\u0115\3\2")
        buf.write("\2\2\u0113\u0111\3\2\2\2\u0113\u0114\3\2\2\2\u0114\u0116")
        buf.write("\3\2\2\2\u0115\u0113\3\2\2\2\u0116\u0117\7\30\2\2\u0117")
        buf.write("\u0124\3\2\2\2\u0118\u0119\7\33\2\2\u0119\u011a\7\27\2")
        buf.write("\2\u011a\u011f\5P)\2\u011b\u011c\7\33\2\2\u011c\u011e")
        buf.write("\5P)\2\u011d\u011b\3\2\2\2\u011e\u0121\3\2\2\2\u011f\u011d")
        buf.write("\3\2\2\2\u011f\u0120\3\2\2\2\u0120\u0122\3\2\2\2\u0121")
        buf.write("\u011f\3\2\2\2\u0122\u0123\7\30\2\2\u0123\u0125\3\2\2")
        buf.write("\2\u0124\u0118\3\2\2\2\u0125\u0126\3\2\2\2\u0126\u0124")
        buf.write("\3\2\2\2\u0126\u0127\3\2\2\2\u0127\u0128\3\2\2\2\u0128")
        buf.write("\u0129\7\30\2\2\u0129\'\3\2\2\2\u012a\u012b\7\31\2\2\u012b")
        buf.write("\u012c\5P)\2\u012c\u012d\7\32\2\2\u012d\u012f\3\2\2\2")
        buf.write("\u012e\u012a\3\2\2\2\u012f\u0130\3\2\2\2\u0130\u012e\3")
        buf.write("\2\2\2\u0130\u0131\3\2\2\2\u0131\u0132\3\2\2\2\u0132\u0133")
        buf.write("\5\22\n\2\u0133\u0134\7\27\2\2\u0134\u0139\5P)\2\u0135")
        buf.write("\u0136\7\33\2\2\u0136\u0138\5P)\2\u0137\u0135\3\2\2\2")
        buf.write("\u0138\u013b\3\2\2\2\u0139\u0137\3\2\2\2\u0139\u013a\3")
        buf.write("\2\2\2\u013a\u013c\3\2\2\2\u013b\u0139\3\2\2\2\u013c\u013d")
        buf.write("\7\30\2\2\u013d)\3\2\2\2\u013e\u013f\7\'\2\2\u013f\u0141")
        buf.write("\7\27\2\2\u0140\u0142\5,\27\2\u0141\u0140\3\2\2\2\u0141")
        buf.write("\u0142\3\2\2\2\u0142\u0143\3\2\2\2\u0143\u0144\7\30\2")
        buf.write("\2\u0144+\3\2\2\2\u0145\u014a\5.\30\2\u0146\u0147\7\33")
        buf.write("\2\2\u0147\u0149\5.\30\2\u0148\u0146\3\2\2\2\u0149\u014c")
        buf.write("\3\2\2\2\u014a\u0148\3\2\2\2\u014a\u014b\3\2\2\2\u014b")
        buf.write("-\3\2\2\2\u014c\u014a\3\2\2\2\u014d\u014e\7\'\2\2\u014e")
        buf.write("\u014f\7\n\2\2\u014f\u0150\5P)\2\u0150/\3\2\2\2\u0151")
        buf.write("\u0152\7\'\2\2\u0152\u0154\7\25\2\2\u0153\u0155\5\62\32")
        buf.write("\2\u0154\u0153\3\2\2\2\u0154\u0155\3\2\2\2\u0155\u0156")
        buf.write("\3\2\2\2\u0156\u0157\7\26\2\2\u0157\61\3\2\2\2\u0158\u015d")
        buf.write("\5P)\2\u0159\u015a\7\33\2\2\u015a\u015c\5P)\2\u015b\u0159")
        buf.write("\3\2\2\2\u015c\u015f\3\2\2\2\u015d\u015b\3\2\2\2\u015d")
        buf.write("\u015e\3\2\2\2\u015e\63\3\2\2\2\u015f\u015d\3\2\2\2\u0160")
        buf.write("\u0161\7\'\2\2\u0161\u0162\7\t\2\2\u0162\u0163\5\60\31")
        buf.write("\2\u0163\65\3\2\2\2\u0164\u016d\5\6\4\2\u0165\u016d\5")
        buf.write("8\35\2\u0166\u016d\5:\36\2\u0167\u016d\5@!\2\u0168\u016d")
        buf.write("\5F$\2\u0169\u016d\5H%\2\u016a\u016d\5J&\2\u016b\u016d")
        buf.write("\5L\'\2\u016c\u0164\3\2\2\2\u016c\u0165\3\2\2\2\u016c")
        buf.write("\u0166\3\2\2\2\u016c\u0167\3\2\2\2\u016c\u0168\3\2\2\2")
        buf.write("\u016c\u0169\3\2\2\2\u016c\u016a\3\2\2\2\u016c\u016b\3")
        buf.write("\2\2\2\u016d\67\3\2\2\2\u016e\u0172\7\'\2\2\u016f\u0172")
        buf.write("\5\"\22\2\u0170\u0172\5$\23\2\u0171\u016e\3\2\2\2\u0171")
        buf.write("\u016f\3\2\2\2\u0171\u0170\3\2\2\2\u0172\u0173\3\2\2\2")
        buf.write("\u0173\u0174\t\3\2\2\u0174\u0175\5P)\2\u0175\u0176\5R")
        buf.write("*\2\u01769\3\2\2\2\u0177\u0178\7\13\2\2\u0178\u0179\5")
        buf.write("P)\2\u0179\u017d\5N(\2\u017a\u017c\5<\37\2\u017b\u017a")
        buf.write("\3\2\2\2\u017c\u017f\3\2\2\2\u017d\u017b\3\2\2\2\u017d")
        buf.write("\u017e\3\2\2\2\u017e\u0181\3\2\2\2\u017f\u017d\3\2\2\2")
        buf.write("\u0180\u0182\5> \2\u0181\u0180\3\2\2\2\u0181\u0182\3\2")
        buf.write("\2\2\u0182\u0192\3\2\2\2\u0183\u0184\7\13\2\2\u0184\u0185")
        buf.write("\7\25\2\2\u0185\u0186\5P)\2\u0186\u0187\7\26\2\2\u0187")
        buf.write("\u018b\5N(\2\u0188\u018a\5<\37\2\u0189\u0188\3\2\2\2\u018a")
        buf.write("\u018d\3\2\2\2\u018b\u0189\3\2\2\2\u018b\u018c\3\2\2\2")
        buf.write("\u018c\u018f\3\2\2\2\u018d\u018b\3\2\2\2\u018e\u0190\5")
        buf.write("> \2\u018f\u018e\3\2\2\2\u018f\u0190\3\2\2\2\u0190\u0192")
        buf.write("\3\2\2\2\u0191\u0177\3\2\2\2\u0191\u0183\3\2\2\2\u0192")
        buf.write(";\3\2\2\2\u0193\u0194\7\f\2\2\u0194\u0195\7\13\2\2\u0195")
        buf.write("\u0196\5P)\2\u0196\u0197\5N(\2\u0197\u01a0\3\2\2\2\u0198")
        buf.write("\u0199\7\f\2\2\u0199\u019a\7\13\2\2\u019a\u019b\7\25\2")
        buf.write("\2\u019b\u019c\5P)\2\u019c\u019d\7\26\2\2\u019d\u019e")
        buf.write("\5N(\2\u019e\u01a0\3\2\2\2\u019f\u0193\3\2\2\2\u019f\u0198")
        buf.write("\3\2\2\2\u01a0=\3\2\2\2\u01a1\u01a2\7\f\2\2\u01a2\u01a3")
        buf.write("\5N(\2\u01a3?\3\2\2\2\u01a4\u01a5\7\r\2\2\u01a5\u01a6")
        buf.write("\5P)\2\u01a6\u01a7\5N(\2\u01a7\u01b9\3\2\2\2\u01a8\u01a9")
        buf.write("\7\r\2\2\u01a9\u01aa\5B\"\2\u01aa\u01ab\7\34\2\2\u01ab")
        buf.write("\u01ac\5P)\2\u01ac\u01ad\7\34\2\2\u01ad\u01ae\5D#\2\u01ae")
        buf.write("\u01af\5N(\2\u01af\u01b9\3\2\2\2\u01b0\u01b1\7\r\2\2\u01b1")
        buf.write("\u01b2\7\'\2\2\u01b2\u01b3\7\33\2\2\u01b3\u01b4\7\'\2")
        buf.write("\2\u01b4\u01b5\7\24\2\2\u01b5\u01b6\7\16\2\2\u01b6\u01b7")
        buf.write("\7\'\2\2\u01b7\u01b9\5N(\2\u01b8\u01a4\3\2\2\2\u01b8\u01a8")
        buf.write("\3\2\2\2\u01b8\u01b0\3\2\2\2\u01b9A\3\2\2\2\u01ba\u01bd")
        buf.write("\58\35\2\u01bb\u01bd\5\6\4\2\u01bc\u01ba\3\2\2\2\u01bc")
        buf.write("\u01bb\3\2\2\2\u01bdC\3\2\2\2\u01be\u01bf\58\35\2\u01bf")
        buf.write("E\3\2\2\2\u01c0\u01c1\7\"\2\2\u01c1\u01c2\5R*\2\u01c2")
        buf.write("G\3\2\2\2\u01c3\u01c4\7!\2\2\u01c4\u01c5\5R*\2\u01c5I")
        buf.write("\3\2\2\2\u01c6\u01c8\7 \2\2\u01c7\u01c9\5P)\2\u01c8\u01c7")
        buf.write("\3\2\2\2\u01c8\u01c9\3\2\2\2\u01c9\u01ca\3\2\2\2\u01ca")
        buf.write("\u01cb\5R*\2\u01cbK\3\2\2\2\u01cc\u01cd\7\'\2\2\u01cd")
        buf.write("\u01cf\7\25\2\2\u01ce\u01d0\5\62\32\2\u01cf\u01ce\3\2")
        buf.write("\2\2\u01cf\u01d0\3\2\2\2\u01d0\u01d1\3\2\2\2\u01d1\u01d2")
        buf.write("\7\26\2\2\u01d2\u01d3\5R*\2\u01d3M\3\2\2\2\u01d4\u01da")
        buf.write("\7\27\2\2\u01d5\u01d6\5\66\34\2\u01d6\u01d7\5R*\2\u01d7")
        buf.write("\u01d9\3\2\2\2\u01d8\u01d5\3\2\2\2\u01d9\u01dc\3\2\2\2")
        buf.write("\u01da\u01d8\3\2\2\2\u01da\u01db\3\2\2\2\u01db\u01dd\3")
        buf.write("\2\2\2\u01dc\u01da\3\2\2\2\u01dd\u01de\7\30\2\2\u01de")
        buf.write("O\3\2\2\2\u01df\u01e0\b)\1\2\u01e0\u01e1\7\25\2\2\u01e1")
        buf.write("\u01e2\5P)\2\u01e2\u01e3\7\26\2\2\u01e3\u01f2\3\2\2\2")
        buf.write("\u01e4\u01f2\7%\2\2\u01e5\u01f2\7$\2\2\u01e6\u01f2\7&")
        buf.write("\2\2\u01e7\u01f2\7\36\2\2\u01e8\u01f2\7\37\2\2\u01e9\u01f2")
        buf.write("\5\64\33\2\u01ea\u01f2\5\60\31\2\u01eb\u01f2\5&\24\2\u01ec")
        buf.write("\u01f2\5(\25\2\u01ed\u01f2\5*\26\2\u01ee\u01f2\5\"\22")
        buf.write("\2\u01ef\u01f2\5$\23\2\u01f0\u01f2\7\'\2\2\u01f1\u01df")
        buf.write("\3\2\2\2\u01f1\u01e4\3\2\2\2\u01f1\u01e5\3\2\2\2\u01f1")
        buf.write("\u01e6\3\2\2\2\u01f1\u01e7\3\2\2\2\u01f1\u01e8\3\2\2\2")
        buf.write("\u01f1\u01e9\3\2\2\2\u01f1\u01ea\3\2\2\2\u01f1\u01eb\3")
        buf.write("\2\2\2\u01f1\u01ec\3\2\2\2\u01f1\u01ed\3\2\2\2\u01f1\u01ee")
        buf.write("\3\2\2\2\u01f1\u01ef\3\2\2\2\u01f1\u01f0\3\2\2\2\u01f2")
        buf.write("\u01fe\3\2\2\2\u01f3\u01f4\f\23\2\2\u01f4\u01f5\7\22\2")
        buf.write("\2\u01f5\u01fd\5P)\24\u01f6\u01f7\f\22\2\2\u01f7\u01f8")
        buf.write("\7\21\2\2\u01f8\u01fd\5P)\23\u01f9\u01fa\f\21\2\2\u01fa")
        buf.write("\u01fb\7\17\2\2\u01fb\u01fd\5P)\22\u01fc\u01f3\3\2\2\2")
        buf.write("\u01fc\u01f6\3\2\2\2\u01fc\u01f9\3\2\2\2\u01fd\u0200\3")
        buf.write("\2\2\2\u01fe\u01fc\3\2\2\2\u01fe\u01ff\3\2\2\2\u01ffQ")
        buf.write("\3\2\2\2\u0200\u01fe\3\2\2\2\u0201\u0204\t\4\2\2\u0202")
        buf.write("\u0204\7\2\2\3\u0203\u0201\3\2\2\2\u0203\u0202\3\2\2\2")
        buf.write("\u0204S\3\2\2\2\63Wbgr{\u0080\u0084\u008a\u008e\u009a")
        buf.write("\u00a6\u00b1\u00b5\u00bc\u00c9\u00d2\u00d6\u00df\u00e7")
        buf.write("\u00f8\u00fc\u0101\u0109\u0113\u011f\u0126\u0130\u0139")
        buf.write("\u0141\u014a\u0154\u015d\u016c\u0171\u017d\u0181\u018b")
        buf.write("\u018f\u0191\u019f\u01b8\u01bc\u01c8\u01cf\u01da\u01f1")
        buf.write("\u01fc\u01fe\u0203")
        return buf.getvalue()


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
        self.checkVersion("4.9.2")
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__1) | (1 << MiniGoParser.T__2) | (1 << MiniGoParser.T__5) | (1 << MiniGoParser.T__8) | (1 << MiniGoParser.T__10) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID))) != 0):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVardecl" ):
                return visitor.visitVardecl(self)
            else:
                return visitor.visitChildren(self)




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
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.BRACK_OPEN) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.ID))) != 0):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReceiver" ):
                return visitor.visitReceiver(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncdecl" ):
                return visitor.visitFuncdecl(self)
            else:
                return visitor.visitChildren(self)




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
            if _la==MiniGoParser.PAREN_OPEN:
                self.state = 120
                self.receiver()


            self.state = 123
            self.match(MiniGoParser.ID)
            self.state = 124
            self.match(MiniGoParser.PAREN_OPEN)
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 125
                self.paramlist()


            self.state = 128
            self.match(MiniGoParser.PAREN_CLOSE)
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.BRACK_OPEN) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.ID))) != 0):
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
            if _la==MiniGoParser.RETURN:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraydecl" ):
                return visitor.visitArraydecl(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructdecl" ):
                return visitor.visitStructdecl(self)
            else:
                return visitor.visitChildren(self)




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
            while _la==MiniGoParser.ID:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFielddecl" ):
                return visitor.visitFielddecl(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTyp" ):
                return visitor.visitTyp(self)
            else:
                return visitor.visitChildren(self)




    def typ(self):

        localctx = MiniGoParser.TypContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_typ)
        try:
            self.state = 179
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.BRACK_OPEN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.arraytype()
                pass
            elif token in [MiniGoParser.TYPE, MiniGoParser.ID]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraytype" ):
                return visitor.visitArraytype(self)
            else:
                return visitor.visitChildren(self)




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
                if not (_la==MiniGoParser.BRACK_OPEN):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBasictype" ):
                return visitor.visitBasictype(self)
            else:
                return visitor.visitChildren(self)




    def basictype(self):

        localctx = MiniGoParser.BasictypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_basictype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.TYPE or _la==MiniGoParser.ID):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfacedecl" ):
                return visitor.visitInterfacedecl(self)
            else:
                return visitor.visitChildren(self)




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
            while _la==MiniGoParser.ID:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethoddecl" ):
                return visitor.visitMethoddecl(self)
            else:
                return visitor.visitChildren(self)




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
            if _la==MiniGoParser.ID:
                self.state = 207
                self.paramlist()


            self.state = 210
            self.match(MiniGoParser.PAREN_CLOSE)
            self.state = 212
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.BRACK_OPEN) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.ID))) != 0):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamlist" ):
                return visitor.visitParamlist(self)
            else:
                return visitor.visitChildren(self)




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
            while _la==MiniGoParser.SEPARATOR_COMMA:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




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
            while _la==MiniGoParser.SEPARATOR_COMMA:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstdecl" ):
                return visitor.visitConstdecl(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_access" ):
                return visitor.visitArray_access(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_access" ):
                return visitor.visitStruct_access(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMulti_array_literal" ):
                return visitor.visitMulti_array_literal(self)
            else:
                return visitor.visitChildren(self)




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
            while _la==MiniGoParser.SEPARATOR_COMMA:
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
                while _la==MiniGoParser.SEPARATOR_COMMA:
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
                if not (_la==MiniGoParser.SEPARATOR_COMMA):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_literal" ):
                return visitor.visitArray_literal(self)
            else:
                return visitor.visitChildren(self)




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
            while _la==MiniGoParser.SEPARATOR_COMMA:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_literal" ):
                return visitor.visitStruct_literal(self)
            else:
                return visitor.visitChildren(self)




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
            if _la==MiniGoParser.ID:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_field_list" ):
                return visitor.visitStruct_field_list(self)
            else:
                return visitor.visitChildren(self)




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
            while _la==MiniGoParser.SEPARATOR_COMMA:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_field" ):
                return visitor.visitStruct_field(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunccall" ):
                return visitor.visitFunccall(self)
            else:
                return visitor.visitChildren(self)




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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.PAREN_OPEN) | (1 << MiniGoParser.BRACK_OPEN) | (1 << MiniGoParser.BOOLLIT) | (1 << MiniGoParser.NILLIT) | (1 << MiniGoParser.FLOATLIT) | (1 << MiniGoParser.INTLIT) | (1 << MiniGoParser.STRLIT) | (1 << MiniGoParser.ID))) != 0):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArglist" ):
                return visitor.visitArglist(self)
            else:
                return visitor.visitChildren(self)




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
            while _la==MiniGoParser.SEPARATOR_COMMA:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodcall" ):
                return visitor.visitMethodcall(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignstmt" ):
                return visitor.visitAssignstmt(self)
            else:
                return visitor.visitChildren(self)




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
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.OP_ASSIGN) | (1 << MiniGoParser.OP_EQUAL) | (1 << MiniGoParser.OP_ASSEQ))) != 0)):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfstmt" ):
                return visitor.visitIfstmt(self)
            else:
                return visitor.visitChildren(self)




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
                if _la==MiniGoParser.T__9:
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
                if _la==MiniGoParser.T__9:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseifstmt" ):
                return visitor.visitElseifstmt(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElsestmt" ):
                return visitor.visitElsestmt(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForstmt" ):
                return visitor.visitForstmt(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForinit" ):
                return visitor.visitForinit(self)
            else:
                return visitor.visitChildren(self)




    def forinit(self):

        localctx = MiniGoParser.ForinitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_forinit)
        try:
            self.state = 442
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 440
                self.assignstmt()
                pass
            elif token in [MiniGoParser.T__0]:
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForupdate" ):
                return visitor.visitForupdate(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakstmt" ):
                return visitor.visitBreakstmt(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinuestmt" ):
                return visitor.visitContinuestmt(self)
            else:
                return visitor.visitChildren(self)




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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnstmt" ):
                return visitor.visitReturnstmt(self)
            else:
                return visitor.visitChildren(self)




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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.PAREN_OPEN) | (1 << MiniGoParser.BRACK_OPEN) | (1 << MiniGoParser.BOOLLIT) | (1 << MiniGoParser.NILLIT) | (1 << MiniGoParser.FLOATLIT) | (1 << MiniGoParser.INTLIT) | (1 << MiniGoParser.STRLIT) | (1 << MiniGoParser.ID))) != 0):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallstmt" ):
                return visitor.visitCallstmt(self)
            else:
                return visitor.visitChildren(self)




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
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.PAREN_OPEN) | (1 << MiniGoParser.BRACK_OPEN) | (1 << MiniGoParser.BOOLLIT) | (1 << MiniGoParser.NILLIT) | (1 << MiniGoParser.FLOATLIT) | (1 << MiniGoParser.INTLIT) | (1 << MiniGoParser.STRLIT) | (1 << MiniGoParser.ID))) != 0):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__8) | (1 << MiniGoParser.T__10) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID))) != 0):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNl" ):
                return visitor.visitNl(self)
            else:
                return visitor.visitChildren(self)




    def nl(self):

        localctx = MiniGoParser.NlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_nl)
        self._la = 0 # Token type
        try:
            self.state = 513
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SEPARATOR_SEMI, MiniGoParser.NEWLINE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 511
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.SEPARATOR_SEMI or _la==MiniGoParser.NEWLINE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [MiniGoParser.EOF]:
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
         




