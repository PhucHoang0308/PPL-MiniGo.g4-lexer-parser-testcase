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
        buf.write("\u0230\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\3\2\7\2V\n\2\f\2\16\2Y\13")
        buf.write("\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\5\3c\n\3\3\4\3\4\3")
        buf.write("\4\5\4h\n\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4s\n")
        buf.write("\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\5\6|\n\6\3\6\3\6\3\6\5")
        buf.write("\6\u0081\n\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u0089\n\6\3\6")
        buf.write("\3\6\7\6\u008d\n\6\f\6\16\6\u0090\13\6\3\6\5\6\u0093\n")
        buf.write("\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\6\b\u00a0")
        buf.write("\n\b\r\b\16\b\u00a1\3\b\3\b\3\t\3\t\3\t\3\t\3\t\7\t\u00ab")
        buf.write("\n\t\f\t\16\t\u00ae\13\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3")
        buf.write("\n\5\n\u00b8\n\n\3\13\3\13\5\13\u00bc\n\13\3\f\3\f\3\r")
        buf.write("\3\r\3\r\3\r\3\r\7\r\u00c5\n\r\f\r\16\r\u00c8\13\r\3\r")
        buf.write("\3\r\3\r\3\16\3\16\3\16\5\16\u00d0\n\16\3\16\3\16\5\16")
        buf.write("\u00d4\n\16\3\16\3\16\3\17\3\17\3\17\7\17\u00db\n\17\f")
        buf.write("\17\16\17\u00de\13\17\3\20\3\20\3\20\7\20\u00e3\n\20\f")
        buf.write("\20\16\20\u00e6\13\20\3\20\3\20\3\21\3\21\3\21\3\21\3")
        buf.write("\21\3\21\3\22\3\22\5\22\u00f2\n\22\3\22\3\22\3\22\6\22")
        buf.write("\u00f7\n\22\r\22\16\22\u00f8\3\23\3\23\5\23\u00fd\n\23")
        buf.write("\3\23\3\23\3\23\3\23\5\23\u0103\n\23\3\24\3\24\3\24\3")
        buf.write("\24\6\24\u0109\n\24\r\24\16\24\u010a\3\24\3\24\3\24\3")
        buf.write("\24\3\24\3\24\7\24\u0113\n\24\f\24\16\24\u0116\13\24\3")
        buf.write("\24\3\24\3\24\3\24\3\24\3\24\3\24\7\24\u011f\n\24\f\24")
        buf.write("\16\24\u0122\13\24\3\24\3\24\6\24\u0126\n\24\r\24\16\24")
        buf.write("\u0127\3\24\3\24\3\25\3\25\3\25\3\25\6\25\u0130\n\25\r")
        buf.write("\25\16\25\u0131\3\25\3\25\3\25\3\25\3\25\7\25\u0139\n")
        buf.write("\25\f\25\16\25\u013c\13\25\3\25\3\25\3\26\3\26\3\26\5")
        buf.write("\26\u0143\n\26\3\26\3\26\3\27\3\27\3\27\7\27\u014a\n\27")
        buf.write("\f\27\16\27\u014d\13\27\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\5\31\u0156\n\31\3\31\3\31\3\32\3\32\3\32\7\32\u015d")
        buf.write("\n\32\f\32\16\32\u0160\13\32\3\33\3\33\3\33\5\33\u0165")
        buf.write("\n\33\3\33\6\33\u0168\n\33\r\33\16\33\u0169\3\33\3\33")
        buf.write("\3\33\5\33\u016f\n\33\3\33\3\33\3\34\3\34\3\34\3\34\3")
        buf.write("\34\3\34\3\34\3\34\5\34\u017b\n\34\3\35\3\35\3\35\5\35")
        buf.write("\u0180\n\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\5")
        buf.write("\36\u018a\n\36\3\36\7\36\u018d\n\36\f\36\16\36\u0190\13")
        buf.write("\36\3\36\5\36\u0193\n\36\3\36\5\36\u0196\n\36\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\36\5\36\u019e\n\36\3\36\7\36\u01a1\n")
        buf.write("\36\f\36\16\36\u01a4\13\36\3\36\5\36\u01a7\n\36\3\36\5")
        buf.write("\36\u01aa\n\36\5\36\u01ac\n\36\3\36\3\36\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\5\37\u01bc")
        buf.write("\n\37\3 \3 \3 \3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!")
        buf.write("\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\3!\5!\u01d9\n!\3\"\3\"")
        buf.write("\3\"\5\"\u01de\n\"\3\"\3\"\3\"\5\"\u01e3\n\"\3#\3#\3#")
        buf.write("\5#\u01e8\n#\3#\3#\3#\3$\3$\3$\3%\3%\3%\3&\3&\5&\u01f5")
        buf.write("\n&\3&\3&\3\'\3\'\3\'\5\'\u01fc\n\'\3\'\3\'\3\'\3(\3(")
        buf.write("\7(\u0203\n(\f(\16(\u0206\13(\3(\3(\3)\3)\3)\3)\3)\3)")
        buf.write("\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\5)\u021c\n)\3)\3")
        buf.write(")\3)\3)\3)\3)\3)\3)\3)\7)\u0227\n)\f)\16)\u022a\13)\3")
        buf.write("*\3*\5*\u022e\n*\3*\2\3P+\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write("\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPR\2\6\4\2%")
        buf.write("%\'\'\4\2\35\35\'\'\4\2\16\16\21\22\4\2\33\33,,\2\u025e")
        buf.write("\2W\3\2\2\2\4b\3\2\2\2\6r\3\2\2\2\bt\3\2\2\2\ny\3\2\2")
        buf.write("\2\f\u0097\3\2\2\2\16\u009f\3\2\2\2\20\u00a5\3\2\2\2\22")
        buf.write("\u00b2\3\2\2\2\24\u00bb\3\2\2\2\26\u00bd\3\2\2\2\30\u00bf")
        buf.write("\3\2\2\2\32\u00cc\3\2\2\2\34\u00d7\3\2\2\2\36\u00df\3")
        buf.write("\2\2\2 \u00e9\3\2\2\2\"\u00f1\3\2\2\2$\u00fc\3\2\2\2&")
        buf.write("\u0108\3\2\2\2(\u012f\3\2\2\2*\u013f\3\2\2\2,\u0146\3")
        buf.write("\2\2\2.\u014e\3\2\2\2\60\u0152\3\2\2\2\62\u0159\3\2\2")
        buf.write("\2\64\u0167\3\2\2\2\66\u017a\3\2\2\28\u017f\3\2\2\2:\u01ab")
        buf.write("\3\2\2\2<\u01bb\3\2\2\2>\u01bd\3\2\2\2@\u01d8\3\2\2\2")
        buf.write("B\u01e2\3\2\2\2D\u01e7\3\2\2\2F\u01ec\3\2\2\2H\u01ef\3")
        buf.write("\2\2\2J\u01f2\3\2\2\2L\u01f8\3\2\2\2N\u0200\3\2\2\2P\u021b")
        buf.write("\3\2\2\2R\u022d\3\2\2\2TV\5\4\3\2UT\3\2\2\2VY\3\2\2\2")
        buf.write("WU\3\2\2\2WX\3\2\2\2XZ\3\2\2\2YW\3\2\2\2Z[\7\2\2\3[\3")
        buf.write("\3\2\2\2\\c\5\66\34\2]c\5\n\6\2^c\5\f\7\2_c\5\20\t\2`")
        buf.write("c\5\30\r\2ac\5 \21\2b\\\3\2\2\2b]\3\2\2\2b^\3\2\2\2b_")
        buf.write("\3\2\2\2b`\3\2\2\2ba\3\2\2\2c\5\3\2\2\2de\7\3\2\2eg\7")
        buf.write("\'\2\2fh\5\24\13\2gf\3\2\2\2gh\3\2\2\2hi\3\2\2\2ij\7\21")
        buf.write("\2\2jk\5P)\2kl\5R*\2ls\3\2\2\2mn\7\3\2\2no\7\'\2\2op\5")
        buf.write("\24\13\2pq\5R*\2qs\3\2\2\2rd\3\2\2\2rm\3\2\2\2s\7\3\2")
        buf.write("\2\2tu\7\24\2\2uv\7\'\2\2vw\5\24\13\2wx\7\25\2\2x\t\3")
        buf.write("\2\2\2y{\7\4\2\2z|\5\b\5\2{z\3\2\2\2{|\3\2\2\2|}\3\2\2")
        buf.write("\2}~\7\'\2\2~\u0080\7\24\2\2\177\u0081\5\34\17\2\u0080")
        buf.write("\177\3\2\2\2\u0080\u0081\3\2\2\2\u0081\u0082\3\2\2\2\u0082")
        buf.write("\u0088\7\25\2\2\u0083\u0089\5\24\13\2\u0084\u0085\7\24")
        buf.write("\2\2\u0085\u0086\5\34\17\2\u0086\u0087\7\25\2\2\u0087")
        buf.write("\u0089\3\2\2\2\u0088\u0083\3\2\2\2\u0088\u0084\3\2\2\2")
        buf.write("\u0088\u0089\3\2\2\2\u0089\u008a\3\2\2\2\u008a\u008e\7")
        buf.write("\26\2\2\u008b\u008d\5\66\34\2\u008c\u008b\3\2\2\2\u008d")
        buf.write("\u0090\3\2\2\2\u008e\u008c\3\2\2\2\u008e\u008f\3\2\2\2")
        buf.write("\u008f\u0092\3\2\2\2\u0090\u008e\3\2\2\2\u0091\u0093\5")
        buf.write("J&\2\u0092\u0091\3\2\2\2\u0092\u0093\3\2\2\2\u0093\u0094")
        buf.write("\3\2\2\2\u0094\u0095\7\27\2\2\u0095\u0096\5R*\2\u0096")
        buf.write("\13\3\2\2\2\u0097\u0098\7\3\2\2\u0098\u0099\7\'\2\2\u0099")
        buf.write("\u009a\5\16\b\2\u009a\u009b\5R*\2\u009b\r\3\2\2\2\u009c")
        buf.write("\u009d\7\30\2\2\u009d\u009e\t\2\2\2\u009e\u00a0\7\31\2")
        buf.write("\2\u009f\u009c\3\2\2\2\u00a0\u00a1\3\2\2\2\u00a1\u009f")
        buf.write("\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3")
        buf.write("\u00a4\5\26\f\2\u00a4\17\3\2\2\2\u00a5\u00a6\7\5\2\2\u00a6")
        buf.write("\u00a7\7\'\2\2\u00a7\u00a8\7\6\2\2\u00a8\u00ac\7\26\2")
        buf.write("\2\u00a9\u00ab\5\22\n\2\u00aa\u00a9\3\2\2\2\u00ab\u00ae")
        buf.write("\3\2\2\2\u00ac\u00aa\3\2\2\2\u00ac\u00ad\3\2\2\2\u00ad")
        buf.write("\u00af\3\2\2\2\u00ae\u00ac\3\2\2\2\u00af\u00b0\7\27\2")
        buf.write("\2\u00b0\u00b1\5R*\2\u00b1\21\3\2\2\2\u00b2\u00b3\7\'")
        buf.write("\2\2\u00b3\u00b4\5\24\13\2\u00b4\u00b7\3\2\2\2\u00b5\u00b8")
        buf.write("\7\33\2\2\u00b6\u00b8\5R*\2\u00b7\u00b5\3\2\2\2\u00b7")
        buf.write("\u00b6\3\2\2\2\u00b8\23\3\2\2\2\u00b9\u00bc\5\16\b\2\u00ba")
        buf.write("\u00bc\5\26\f\2\u00bb\u00b9\3\2\2\2\u00bb\u00ba\3\2\2")
        buf.write("\2\u00bc\25\3\2\2\2\u00bd\u00be\t\3\2\2\u00be\27\3\2\2")
        buf.write("\2\u00bf\u00c0\7\5\2\2\u00c0\u00c1\7\'\2\2\u00c1\u00c2")
        buf.write("\7\7\2\2\u00c2\u00c6\7\26\2\2\u00c3\u00c5\5\32\16\2\u00c4")
        buf.write("\u00c3\3\2\2\2\u00c5\u00c8\3\2\2\2\u00c6\u00c4\3\2\2\2")
        buf.write("\u00c6\u00c7\3\2\2\2\u00c7\u00c9\3\2\2\2\u00c8\u00c6\3")
        buf.write("\2\2\2\u00c9\u00ca\7\27\2\2\u00ca\u00cb\5R*\2\u00cb\31")
        buf.write("\3\2\2\2\u00cc\u00cd\7\'\2\2\u00cd\u00cf\7\24\2\2\u00ce")
        buf.write("\u00d0\5\34\17\2\u00cf\u00ce\3\2\2\2\u00cf\u00d0\3\2\2")
        buf.write("\2\u00d0\u00d1\3\2\2\2\u00d1\u00d3\7\25\2\2\u00d2\u00d4")
        buf.write("\5\24\13\2\u00d3\u00d2\3\2\2\2\u00d3\u00d4\3\2\2\2\u00d4")
        buf.write("\u00d5\3\2\2\2\u00d5\u00d6\5R*\2\u00d6\33\3\2\2\2\u00d7")
        buf.write("\u00dc\5\36\20\2\u00d8\u00d9\7\32\2\2\u00d9\u00db\5\36")
        buf.write("\20\2\u00da\u00d8\3\2\2\2\u00db\u00de\3\2\2\2\u00dc\u00da")
        buf.write("\3\2\2\2\u00dc\u00dd\3\2\2\2\u00dd\35\3\2\2\2\u00de\u00dc")
        buf.write("\3\2\2\2\u00df\u00e4\7\'\2\2\u00e0\u00e1\7\32\2\2\u00e1")
        buf.write("\u00e3\7\'\2\2\u00e2\u00e0\3\2\2\2\u00e3\u00e6\3\2\2\2")
        buf.write("\u00e4\u00e2\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5\u00e7\3")
        buf.write("\2\2\2\u00e6\u00e4\3\2\2\2\u00e7\u00e8\5\24\13\2\u00e8")
        buf.write("\37\3\2\2\2\u00e9\u00ea\7\b\2\2\u00ea\u00eb\7\'\2\2\u00eb")
        buf.write("\u00ec\7\21\2\2\u00ec\u00ed\5P)\2\u00ed\u00ee\5R*\2\u00ee")
        buf.write("!\3\2\2\2\u00ef\u00f2\5\60\31\2\u00f0\u00f2\7\'\2\2\u00f1")
        buf.write("\u00ef\3\2\2\2\u00f1\u00f0\3\2\2\2\u00f2\u00f6\3\2\2\2")
        buf.write("\u00f3\u00f4\7\30\2\2\u00f4\u00f5\7%\2\2\u00f5\u00f7\7")
        buf.write("\31\2\2\u00f6\u00f3\3\2\2\2\u00f7\u00f8\3\2\2\2\u00f8")
        buf.write("\u00f6\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f9#\3\2\2\2\u00fa")
        buf.write("\u00fd\7\'\2\2\u00fb\u00fd\5\"\22\2\u00fc\u00fa\3\2\2")
        buf.write("\2\u00fc\u00fb\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe\u0102")
        buf.write("\7\34\2\2\u00ff\u0103\7\'\2\2\u0100\u0103\5\"\22\2\u0101")
        buf.write("\u0103\5\60\31\2\u0102\u00ff\3\2\2\2\u0102\u0100\3\2\2")
        buf.write("\2\u0102\u0101\3\2\2\2\u0103%\3\2\2\2\u0104\u0105\7\30")
        buf.write("\2\2\u0105\u0106\5P)\2\u0106\u0107\7\31\2\2\u0107\u0109")
        buf.write("\3\2\2\2\u0108\u0104\3\2\2\2\u0109\u010a\3\2\2\2\u010a")
        buf.write("\u0108\3\2\2\2\u010a\u010b\3\2\2\2\u010b\u010c\3\2\2\2")
        buf.write("\u010c\u010d\5\24\13\2\u010d\u010e\7\26\2\2\u010e\u010f")
        buf.write("\7\26\2\2\u010f\u0114\5P)\2\u0110\u0111\7\32\2\2\u0111")
        buf.write("\u0113\5P)\2\u0112\u0110\3\2\2\2\u0113\u0116\3\2\2\2\u0114")
        buf.write("\u0112\3\2\2\2\u0114\u0115\3\2\2\2\u0115\u0117\3\2\2\2")
        buf.write("\u0116\u0114\3\2\2\2\u0117\u0118\7\27\2\2\u0118\u0125")
        buf.write("\3\2\2\2\u0119\u011a\7\32\2\2\u011a\u011b\7\26\2\2\u011b")
        buf.write("\u0120\5P)\2\u011c\u011d\7\32\2\2\u011d\u011f\5P)\2\u011e")
        buf.write("\u011c\3\2\2\2\u011f\u0122\3\2\2\2\u0120\u011e\3\2\2\2")
        buf.write("\u0120\u0121\3\2\2\2\u0121\u0123\3\2\2\2\u0122\u0120\3")
        buf.write("\2\2\2\u0123\u0124\7\27\2\2\u0124\u0126\3\2\2\2\u0125")
        buf.write("\u0119\3\2\2\2\u0126\u0127\3\2\2\2\u0127\u0125\3\2\2\2")
        buf.write("\u0127\u0128\3\2\2\2\u0128\u0129\3\2\2\2\u0129\u012a\7")
        buf.write("\27\2\2\u012a\'\3\2\2\2\u012b\u012c\7\30\2\2\u012c\u012d")
        buf.write("\5P)\2\u012d\u012e\7\31\2\2\u012e\u0130\3\2\2\2\u012f")
        buf.write("\u012b\3\2\2\2\u0130\u0131\3\2\2\2\u0131\u012f\3\2\2\2")
        buf.write("\u0131\u0132\3\2\2\2\u0132\u0133\3\2\2\2\u0133\u0134\5")
        buf.write("\24\13\2\u0134\u0135\7\26\2\2\u0135\u013a\5P)\2\u0136")
        buf.write("\u0137\7\32\2\2\u0137\u0139\5P)\2\u0138\u0136\3\2\2\2")
        buf.write("\u0139\u013c\3\2\2\2\u013a\u0138\3\2\2\2\u013a\u013b\3")
        buf.write("\2\2\2\u013b\u013d\3\2\2\2\u013c\u013a\3\2\2\2\u013d\u013e")
        buf.write("\7\27\2\2\u013e)\3\2\2\2\u013f\u0140\7\'\2\2\u0140\u0142")
        buf.write("\7\26\2\2\u0141\u0143\5,\27\2\u0142\u0141\3\2\2\2\u0142")
        buf.write("\u0143\3\2\2\2\u0143\u0144\3\2\2\2\u0144\u0145\7\27\2")
        buf.write("\2\u0145+\3\2\2\2\u0146\u014b\5.\30\2\u0147\u0148\7\32")
        buf.write("\2\2\u0148\u014a\5.\30\2\u0149\u0147\3\2\2\2\u014a\u014d")
        buf.write("\3\2\2\2\u014b\u0149\3\2\2\2\u014b\u014c\3\2\2\2\u014c")
        buf.write("-\3\2\2\2\u014d\u014b\3\2\2\2\u014e\u014f\7\'\2\2\u014f")
        buf.write("\u0150\7\23\2\2\u0150\u0151\5P)\2\u0151/\3\2\2\2\u0152")
        buf.write("\u0153\7\'\2\2\u0153\u0155\7\24\2\2\u0154\u0156\5\62\32")
        buf.write("\2\u0155\u0154\3\2\2\2\u0155\u0156\3\2\2\2\u0156\u0157")
        buf.write("\3\2\2\2\u0157\u0158\7\25\2\2\u0158\61\3\2\2\2\u0159\u015e")
        buf.write("\5P)\2\u015a\u015b\7\32\2\2\u015b\u015d\5P)\2\u015c\u015a")
        buf.write("\3\2\2\2\u015d\u0160\3\2\2\2\u015e\u015c\3\2\2\2\u015e")
        buf.write("\u015f\3\2\2\2\u015f\63\3\2\2\2\u0160\u015e\3\2\2\2\u0161")
        buf.write("\u0165\5\"\22\2\u0162\u0165\5$\23\2\u0163\u0165\7\'\2")
        buf.write("\2\u0164\u0161\3\2\2\2\u0164\u0162\3\2\2\2\u0164\u0163")
        buf.write("\3\2\2\2\u0165\u0166\3\2\2\2\u0166\u0168\7\34\2\2\u0167")
        buf.write("\u0164\3\2\2\2\u0168\u0169\3\2\2\2\u0169\u0167\3\2\2\2")
        buf.write("\u0169\u016a\3\2\2\2\u016a\u016b\3\2\2\2\u016b\u016c\7")
        buf.write("\'\2\2\u016c\u016e\7\24\2\2\u016d\u016f\5\62\32\2\u016e")
        buf.write("\u016d\3\2\2\2\u016e\u016f\3\2\2\2\u016f\u0170\3\2\2\2")
        buf.write("\u0170\u0171\7\25\2\2\u0171\65\3\2\2\2\u0172\u017b\5\6")
        buf.write("\4\2\u0173\u017b\58\35\2\u0174\u017b\5:\36\2\u0175\u017b")
        buf.write("\5@!\2\u0176\u017b\5F$\2\u0177\u017b\5H%\2\u0178\u017b")
        buf.write("\5J&\2\u0179\u017b\5L\'\2\u017a\u0172\3\2\2\2\u017a\u0173")
        buf.write("\3\2\2\2\u017a\u0174\3\2\2\2\u017a\u0175\3\2\2\2\u017a")
        buf.write("\u0176\3\2\2\2\u017a\u0177\3\2\2\2\u017a\u0178\3\2\2\2")
        buf.write("\u017a\u0179\3\2\2\2\u017b\67\3\2\2\2\u017c\u0180\7\'")
        buf.write("\2\2\u017d\u0180\5$\23\2\u017e\u0180\5\"\22\2\u017f\u017c")
        buf.write("\3\2\2\2\u017f\u017d\3\2\2\2\u017f\u017e\3\2\2\2\u0180")
        buf.write("\u0181\3\2\2\2\u0181\u0182\t\4\2\2\u0182\u0183\5P)\2\u0183")
        buf.write("\u0184\5R*\2\u01849\3\2\2\2\u0185\u0186\7\t\2\2\u0186")
        buf.write("\u0187\5P)\2\u0187\u018e\5N(\2\u0188\u018a\7,\2\2\u0189")
        buf.write("\u0188\3\2\2\2\u0189\u018a\3\2\2\2\u018a\u018b\3\2\2\2")
        buf.write("\u018b\u018d\5<\37\2\u018c\u0189\3\2\2\2\u018d\u0190\3")
        buf.write("\2\2\2\u018e\u018c\3\2\2\2\u018e\u018f\3\2\2\2\u018f\u0195")
        buf.write("\3\2\2\2\u0190\u018e\3\2\2\2\u0191\u0193\7,\2\2\u0192")
        buf.write("\u0191\3\2\2\2\u0192\u0193\3\2\2\2\u0193\u0194\3\2\2\2")
        buf.write("\u0194\u0196\5> \2\u0195\u0192\3\2\2\2\u0195\u0196\3\2")
        buf.write("\2\2\u0196\u01ac\3\2\2\2\u0197\u0198\7\t\2\2\u0198\u0199")
        buf.write("\7\24\2\2\u0199\u019a\5P)\2\u019a\u019b\7\25\2\2\u019b")
        buf.write("\u01a2\5N(\2\u019c\u019e\7,\2\2\u019d\u019c\3\2\2\2\u019d")
        buf.write("\u019e\3\2\2\2\u019e\u019f\3\2\2\2\u019f\u01a1\5<\37\2")
        buf.write("\u01a0\u019d\3\2\2\2\u01a1\u01a4\3\2\2\2\u01a2\u01a0\3")
        buf.write("\2\2\2\u01a2\u01a3\3\2\2\2\u01a3\u01a9\3\2\2\2\u01a4\u01a2")
        buf.write("\3\2\2\2\u01a5\u01a7\7,\2\2\u01a6\u01a5\3\2\2\2\u01a6")
        buf.write("\u01a7\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8\u01aa\5> \2\u01a9")
        buf.write("\u01a6\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa\u01ac\3\2\2\2")
        buf.write("\u01ab\u0185\3\2\2\2\u01ab\u0197\3\2\2\2\u01ac\u01ad\3")
        buf.write("\2\2\2\u01ad\u01ae\5R*\2\u01ae;\3\2\2\2\u01af\u01b0\7")
        buf.write("\n\2\2\u01b0\u01b1\7\t\2\2\u01b1\u01b2\5P)\2\u01b2\u01b3")
        buf.write("\5N(\2\u01b3\u01bc\3\2\2\2\u01b4\u01b5\7\n\2\2\u01b5\u01b6")
        buf.write("\7\t\2\2\u01b6\u01b7\7\24\2\2\u01b7\u01b8\5P)\2\u01b8")
        buf.write("\u01b9\7\25\2\2\u01b9\u01ba\5N(\2\u01ba\u01bc\3\2\2\2")
        buf.write("\u01bb\u01af\3\2\2\2\u01bb\u01b4\3\2\2\2\u01bc=\3\2\2")
        buf.write("\2\u01bd\u01be\7\n\2\2\u01be\u01bf\5N(\2\u01bf?\3\2\2")
        buf.write("\2\u01c0\u01c1\7\13\2\2\u01c1\u01c2\5P)\2\u01c2\u01c3")
        buf.write("\5N(\2\u01c3\u01c4\5R*\2\u01c4\u01d9\3\2\2\2\u01c5\u01c6")
        buf.write("\7\13\2\2\u01c6\u01c7\5B\"\2\u01c7\u01c8\7\33\2\2\u01c8")
        buf.write("\u01c9\5P)\2\u01c9\u01ca\7\33\2\2\u01ca\u01cb\5D#\2\u01cb")
        buf.write("\u01cc\5N(\2\u01cc\u01cd\5R*\2\u01cd\u01d9\3\2\2\2\u01ce")
        buf.write("\u01cf\7\13\2\2\u01cf\u01d0\7\'\2\2\u01d0\u01d1\7\32\2")
        buf.write("\2\u01d1\u01d2\7\'\2\2\u01d2\u01d3\7\22\2\2\u01d3\u01d4")
        buf.write("\7\f\2\2\u01d4\u01d5\7\'\2\2\u01d5\u01d6\5N(\2\u01d6\u01d7")
        buf.write("\5R*\2\u01d7\u01d9\3\2\2\2\u01d8\u01c0\3\2\2\2\u01d8\u01c5")
        buf.write("\3\2\2\2\u01d8\u01ce\3\2\2\2\u01d9A\3\2\2\2\u01da\u01de")
        buf.write("\7\'\2\2\u01db\u01de\5$\23\2\u01dc\u01de\5\"\22\2\u01dd")
        buf.write("\u01da\3\2\2\2\u01dd\u01db\3\2\2\2\u01dd\u01dc\3\2\2\2")
        buf.write("\u01de\u01df\3\2\2\2\u01df\u01e0\t\4\2\2\u01e0\u01e3\5")
        buf.write("P)\2\u01e1\u01e3\5\6\4\2\u01e2\u01dd\3\2\2\2\u01e2\u01e1")
        buf.write("\3\2\2\2\u01e3C\3\2\2\2\u01e4\u01e8\7\'\2\2\u01e5\u01e8")
        buf.write("\5$\23\2\u01e6\u01e8\5\"\22\2\u01e7\u01e4\3\2\2\2\u01e7")
        buf.write("\u01e5\3\2\2\2\u01e7\u01e6\3\2\2\2\u01e8\u01e9\3\2\2\2")
        buf.write("\u01e9\u01ea\t\4\2\2\u01ea\u01eb\5P)\2\u01ebE\3\2\2\2")
        buf.write("\u01ec\u01ed\7\"\2\2\u01ed\u01ee\5R*\2\u01eeG\3\2\2\2")
        buf.write("\u01ef\u01f0\7!\2\2\u01f0\u01f1\5R*\2\u01f1I\3\2\2\2\u01f2")
        buf.write("\u01f4\7 \2\2\u01f3\u01f5\5P)\2\u01f4\u01f3\3\2\2\2\u01f4")
        buf.write("\u01f5\3\2\2\2\u01f5\u01f6\3\2\2\2\u01f6\u01f7\5R*\2\u01f7")
        buf.write("K\3\2\2\2\u01f8\u01f9\7\'\2\2\u01f9\u01fb\7\24\2\2\u01fa")
        buf.write("\u01fc\5\62\32\2\u01fb\u01fa\3\2\2\2\u01fb\u01fc\3\2\2")
        buf.write("\2\u01fc\u01fd\3\2\2\2\u01fd\u01fe\7\25\2\2\u01fe\u01ff")
        buf.write("\5R*\2\u01ffM\3\2\2\2\u0200\u0204\7\26\2\2\u0201\u0203")
        buf.write("\5\66\34\2\u0202\u0201\3\2\2\2\u0203\u0206\3\2\2\2\u0204")
        buf.write("\u0202\3\2\2\2\u0204\u0205\3\2\2\2\u0205\u0207\3\2\2\2")
        buf.write("\u0206\u0204\3\2\2\2\u0207\u0208\7\27\2\2\u0208O\3\2\2")
        buf.write("\2\u0209\u020a\b)\1\2\u020a\u020b\7\24\2\2\u020b\u020c")
        buf.write("\5P)\2\u020c\u020d\7\25\2\2\u020d\u021c\3\2\2\2\u020e")
        buf.write("\u021c\7%\2\2\u020f\u021c\7$\2\2\u0210\u021c\7&\2\2\u0211")
        buf.write("\u021c\7\36\2\2\u0212\u021c\7\37\2\2\u0213\u021c\5\64")
        buf.write("\33\2\u0214\u021c\5\60\31\2\u0215\u021c\5&\24\2\u0216")
        buf.write("\u021c\5(\25\2\u0217\u021c\5*\26\2\u0218\u021c\5$\23\2")
        buf.write("\u0219\u021c\5\"\22\2\u021a\u021c\7\'\2\2\u021b\u0209")
        buf.write("\3\2\2\2\u021b\u020e\3\2\2\2\u021b\u020f\3\2\2\2\u021b")
        buf.write("\u0210\3\2\2\2\u021b\u0211\3\2\2\2\u021b\u0212\3\2\2\2")
        buf.write("\u021b\u0213\3\2\2\2\u021b\u0214\3\2\2\2\u021b\u0215\3")
        buf.write("\2\2\2\u021b\u0216\3\2\2\2\u021b\u0217\3\2\2\2\u021b\u0218")
        buf.write("\3\2\2\2\u021b\u0219\3\2\2\2\u021b\u021a\3\2\2\2\u021c")
        buf.write("\u0228\3\2\2\2\u021d\u021e\f\23\2\2\u021e\u021f\7\20\2")
        buf.write("\2\u021f\u0227\5P)\24\u0220\u0221\f\22\2\2\u0221\u0222")
        buf.write("\7\17\2\2\u0222\u0227\5P)\23\u0223\u0224\f\21\2\2\u0224")
        buf.write("\u0225\7\r\2\2\u0225\u0227\5P)\22\u0226\u021d\3\2\2\2")
        buf.write("\u0226\u0220\3\2\2\2\u0226\u0223\3\2\2\2\u0227\u022a\3")
        buf.write("\2\2\2\u0228\u0226\3\2\2\2\u0228\u0229\3\2\2\2\u0229Q")
        buf.write("\3\2\2\2\u022a\u0228\3\2\2\2\u022b\u022e\t\5\2\2\u022c")
        buf.write("\u022e\7\2\2\3\u022d\u022b\3\2\2\2\u022d\u022c\3\2\2\2")
        buf.write("\u022eS\3\2\2\2<Wbgr{\u0080\u0088\u008e\u0092\u00a1\u00ac")
        buf.write("\u00b7\u00bb\u00c6\u00cf\u00d3\u00dc\u00e4\u00f1\u00f8")
        buf.write("\u00fc\u0102\u010a\u0114\u0120\u0127\u0131\u013a\u0142")
        buf.write("\u014b\u0155\u015e\u0164\u0169\u016e\u017a\u017f\u0189")
        buf.write("\u018e\u0192\u0195\u019d\u01a2\u01a6\u01a9\u01ab\u01bb")
        buf.write("\u01d8\u01dd\u01e2\u01e7\u01f4\u01fb\u0204\u021b\u0226")
        buf.write("\u0228\u022d")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'var'", "'func'", "'type'", "'struct'", 
                     "'interface'", "'const'", "'if'", "'else'", "'for'", 
                     "'range'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'='", "':='", "':'", "'('", "')'", "'{'", "'}'", "'['", 
                     "']'", "','", "';'", "'.'", "<INVALID>", "<INVALID>", 
                     "'nil'", "'return'", "'continue'", "'break'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "OP_COMPARE", 
                      "OP_ASSIGN", "OP_LOGIC", "OP_ARITH", "OP_EQUAL", "OP_ASSEQ", 
                      "COLON", "PAREN_OPEN", "PAREN_CLOSE", "BRACE_OPEN", 
                      "BRACE_CLOSE", "BRACK_OPEN", "BRACK_CLOSE", "SEPARATOR_COMMA", 
                      "SEPARATOR_SEMI", "OP_DOT", "TYPE", "BOOLLIT", "NILLIT", 
                      "RETURN", "CONTINUE", "BREAK", "KEYWORD", "FLOATLIT", 
                      "INTLIT", "STRLIT", "ID", "DECIMAL_LITERAL", "BINARY_LITERAL", 
                      "OCTAL_LITERAL", "HEXADECIMAL_LITERAL", "NEWLINE", 
                      "WS", "MULTILINE_COMMENT", "COMMENT", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_decl = 1
    RULE_vardecl = 2
    RULE_receiver = 3
    RULE_funcdecl = 4
    RULE_arraydecl = 5
    RULE_arraytype = 6
    RULE_structdecl = 7
    RULE_fielddecl = 8
    RULE_typ = 9
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
                   "arraydecl", "arraytype", "structdecl", "fielddecl", 
                   "typ", "basictype", "interfacedecl", "methoddecl", "paramlist", 
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
    OP_COMPARE=11
    OP_ASSIGN=12
    OP_LOGIC=13
    OP_ARITH=14
    OP_EQUAL=15
    OP_ASSEQ=16
    COLON=17
    PAREN_OPEN=18
    PAREN_CLOSE=19
    BRACE_OPEN=20
    BRACE_CLOSE=21
    BRACK_OPEN=22
    BRACK_CLOSE=23
    SEPARATOR_COMMA=24
    SEPARATOR_SEMI=25
    OP_DOT=26
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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__1) | (1 << MiniGoParser.T__2) | (1 << MiniGoParser.T__5) | (1 << MiniGoParser.T__6) | (1 << MiniGoParser.T__8) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID))) != 0):
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

        def PAREN_OPEN(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.PAREN_OPEN)
            else:
                return self.getToken(MiniGoParser.PAREN_OPEN, i)

        def PAREN_CLOSE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.PAREN_CLOSE)
            else:
                return self.getToken(MiniGoParser.PAREN_CLOSE, i)

        def BRACE_OPEN(self):
            return self.getToken(MiniGoParser.BRACE_OPEN, 0)

        def BRACE_CLOSE(self):
            return self.getToken(MiniGoParser.BRACE_CLOSE, 0)

        def nl(self):
            return self.getTypedRuleContext(MiniGoParser.NlContext,0)


        def receiver(self):
            return self.getTypedRuleContext(MiniGoParser.ReceiverContext,0)


        def paramlist(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ParamlistContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ParamlistContext,i)


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
            self.state = 134
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.BRACK_OPEN, MiniGoParser.TYPE, MiniGoParser.ID]:
                self.state = 129
                self.typ()
                pass
            elif token in [MiniGoParser.PAREN_OPEN]:
                self.state = 130
                self.match(MiniGoParser.PAREN_OPEN)
                self.state = 131
                self.paramlist()
                self.state = 132
                self.match(MiniGoParser.PAREN_CLOSE)
                pass
            elif token in [MiniGoParser.BRACE_OPEN]:
                pass
            else:
                pass
            self.state = 136
            self.match(MiniGoParser.BRACE_OPEN)
            self.state = 140
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 137
                    self.stmt() 
                self.state = 142
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.RETURN:
                self.state = 143
                self.returnstmt()


            self.state = 146
            self.match(MiniGoParser.BRACE_CLOSE)
            self.state = 147
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

        def arraytype(self):
            return self.getTypedRuleContext(MiniGoParser.ArraytypeContext,0)


        def nl(self):
            return self.getTypedRuleContext(MiniGoParser.NlContext,0)


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
            self.state = 149
            self.match(MiniGoParser.T__0)
            self.state = 150
            self.match(MiniGoParser.ID)
            self.state = 151
            self.arraytype()
            self.state = 152
            self.nl()
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

        def BRACK_CLOSE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.BRACK_CLOSE)
            else:
                return self.getToken(MiniGoParser.BRACK_CLOSE, i)

        def INTLIT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.INTLIT)
            else:
                return self.getToken(MiniGoParser.INTLIT, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arraytype

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArraytype" ):
                return visitor.visitArraytype(self)
            else:
                return visitor.visitChildren(self)




    def arraytype(self):

        localctx = MiniGoParser.ArraytypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_arraytype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 154
                self.match(MiniGoParser.BRACK_OPEN)
                self.state = 155
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.INTLIT or _la==MiniGoParser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 156
                self.match(MiniGoParser.BRACK_CLOSE)
                self.state = 159 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.BRACK_OPEN):
                    break

            self.state = 161
            self.basictype()
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
        self.enterRule(localctx, 14, self.RULE_structdecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(MiniGoParser.T__2)
            self.state = 164
            self.match(MiniGoParser.ID)
            self.state = 165
            self.match(MiniGoParser.T__3)
            self.state = 166
            self.match(MiniGoParser.BRACE_OPEN)
            self.state = 170
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.ID:
                self.state = 167
                self.fielddecl()
                self.state = 172
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 173
            self.match(MiniGoParser.BRACE_CLOSE)
            self.state = 174
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
        self.enterRule(localctx, 16, self.RULE_fielddecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(MiniGoParser.ID)
            self.state = 177
            self.typ()
            self.state = 181
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 179
                self.match(MiniGoParser.SEPARATOR_SEMI)
                pass

            elif la_ == 2:
                self.state = 180
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
        self.enterRule(localctx, 18, self.RULE_typ)
        try:
            self.state = 185
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.BRACK_OPEN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.arraytype()
                pass
            elif token in [MiniGoParser.TYPE, MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
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
            self.state = 187
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
            self.state = 189
            self.match(MiniGoParser.T__2)
            self.state = 190
            self.match(MiniGoParser.ID)
            self.state = 191
            self.match(MiniGoParser.T__4)
            self.state = 192
            self.match(MiniGoParser.BRACE_OPEN)
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.ID:
                self.state = 193
                self.methoddecl()
                self.state = 198
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 199
            self.match(MiniGoParser.BRACE_CLOSE)
            self.state = 200
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
            self.state = 202
            self.match(MiniGoParser.ID)
            self.state = 203
            self.match(MiniGoParser.PAREN_OPEN)
            self.state = 205
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 204
                self.paramlist()


            self.state = 207
            self.match(MiniGoParser.PAREN_CLOSE)
            self.state = 209
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.BRACK_OPEN) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.ID))) != 0):
                self.state = 208
                self.typ()


            self.state = 211
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
            self.state = 213
            self.param()
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.SEPARATOR_COMMA:
                self.state = 214
                self.match(MiniGoParser.SEPARATOR_COMMA)
                self.state = 215
                self.param()
                self.state = 220
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
            self.state = 221
            self.match(MiniGoParser.ID)
            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.SEPARATOR_COMMA:
                self.state = 222
                self.match(MiniGoParser.SEPARATOR_COMMA)
                self.state = 223
                self.match(MiniGoParser.ID)
                self.state = 228
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 229
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
            self.state = 231
            self.match(MiniGoParser.T__5)
            self.state = 232
            self.match(MiniGoParser.ID)
            self.state = 233
            self.match(MiniGoParser.OP_EQUAL)
            self.state = 234
            self.expr(0)
            self.state = 235
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

        def funccall(self):
            return self.getTypedRuleContext(MiniGoParser.FunccallContext,0)


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
            self.state = 239
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 237
                self.funccall()
                pass

            elif la_ == 2:
                self.state = 238
                self.match(MiniGoParser.ID)
                pass


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

        def OP_DOT(self):
            return self.getToken(MiniGoParser.OP_DOT, 0)

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


        def funccall(self):
            return self.getTypedRuleContext(MiniGoParser.FunccallContext,0)


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
            self.match(MiniGoParser.OP_DOT)
            self.state = 256
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

            elif la_ == 3:
                self.state = 255
                self.funccall()
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
            self.state = 262 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 258
                    self.match(MiniGoParser.BRACK_OPEN)
                    self.state = 259
                    self.expr(0)
                    self.state = 260
                    self.match(MiniGoParser.BRACK_CLOSE)

                else:
                    raise NoViableAltException(self)
                self.state = 264 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

            self.state = 266
            self.typ()
            self.state = 267
            self.match(MiniGoParser.BRACE_OPEN)

            self.state = 268
            self.match(MiniGoParser.BRACE_OPEN)
            self.state = 269
            self.expr(0)
            self.state = 274
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.SEPARATOR_COMMA:
                self.state = 270
                self.match(MiniGoParser.SEPARATOR_COMMA)
                self.state = 271
                self.expr(0)
                self.state = 276
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 277
            self.match(MiniGoParser.BRACE_CLOSE)
            self.state = 291 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 279
                self.match(MiniGoParser.SEPARATOR_COMMA)
                self.state = 280
                self.match(MiniGoParser.BRACE_OPEN)
                self.state = 281
                self.expr(0)
                self.state = 286
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==MiniGoParser.SEPARATOR_COMMA:
                    self.state = 282
                    self.match(MiniGoParser.SEPARATOR_COMMA)
                    self.state = 283
                    self.expr(0)
                    self.state = 288
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 289
                self.match(MiniGoParser.BRACE_CLOSE)
                self.state = 293 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==MiniGoParser.SEPARATOR_COMMA):
                    break

            self.state = 295
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
            self.state = 301 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 297
                    self.match(MiniGoParser.BRACK_OPEN)
                    self.state = 298
                    self.expr(0)
                    self.state = 299
                    self.match(MiniGoParser.BRACK_CLOSE)

                else:
                    raise NoViableAltException(self)
                self.state = 303 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

            self.state = 305
            self.typ()
            self.state = 306
            self.match(MiniGoParser.BRACE_OPEN)
            self.state = 307
            self.expr(0)
            self.state = 312
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.SEPARATOR_COMMA:
                self.state = 308
                self.match(MiniGoParser.SEPARATOR_COMMA)
                self.state = 309
                self.expr(0)
                self.state = 314
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 315
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
            self.state = 317
            self.match(MiniGoParser.ID)
            self.state = 318
            self.match(MiniGoParser.BRACE_OPEN)
            self.state = 320
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ID:
                self.state = 319
                self.struct_field_list()


            self.state = 322
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
            self.state = 324
            self.struct_field()
            self.state = 329
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.SEPARATOR_COMMA:
                self.state = 325
                self.match(MiniGoParser.SEPARATOR_COMMA)
                self.state = 326
                self.struct_field()
                self.state = 331
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

        def COLON(self):
            return self.getToken(MiniGoParser.COLON, 0)

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
            self.state = 332
            self.match(MiniGoParser.ID)
            self.state = 333
            self.match(MiniGoParser.COLON)
            self.state = 334
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
            self.state = 336
            self.match(MiniGoParser.ID)
            self.state = 337
            self.match(MiniGoParser.PAREN_OPEN)
            self.state = 339
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.PAREN_OPEN) | (1 << MiniGoParser.BRACK_OPEN) | (1 << MiniGoParser.BOOLLIT) | (1 << MiniGoParser.NILLIT) | (1 << MiniGoParser.FLOATLIT) | (1 << MiniGoParser.INTLIT) | (1 << MiniGoParser.STRLIT) | (1 << MiniGoParser.ID))) != 0):
                self.state = 338
                self.arglist()


            self.state = 341
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
            self.state = 343
            self.expr(0)
            self.state = 348
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MiniGoParser.SEPARATOR_COMMA:
                self.state = 344
                self.match(MiniGoParser.SEPARATOR_COMMA)
                self.state = 345
                self.expr(0)
                self.state = 350
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

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def PAREN_OPEN(self):
            return self.getToken(MiniGoParser.PAREN_OPEN, 0)

        def PAREN_CLOSE(self):
            return self.getToken(MiniGoParser.PAREN_CLOSE, 0)

        def OP_DOT(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.OP_DOT)
            else:
                return self.getToken(MiniGoParser.OP_DOT, i)

        def arglist(self):
            return self.getTypedRuleContext(MiniGoParser.ArglistContext,0)


        def array_access(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Array_accessContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Array_accessContext,i)


        def struct_access(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.Struct_accessContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.Struct_accessContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 354
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
                    if la_ == 1:
                        self.state = 351
                        self.array_access()
                        pass

                    elif la_ == 2:
                        self.state = 352
                        self.struct_access()
                        pass

                    elif la_ == 3:
                        self.state = 353
                        self.match(MiniGoParser.ID)
                        pass


                    self.state = 356
                    self.match(MiniGoParser.OP_DOT)

                else:
                    raise NoViableAltException(self)
                self.state = 359 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,33,self._ctx)

            self.state = 361
            self.match(MiniGoParser.ID)
            self.state = 362
            self.match(MiniGoParser.PAREN_OPEN)
            self.state = 364
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.PAREN_OPEN) | (1 << MiniGoParser.BRACK_OPEN) | (1 << MiniGoParser.BOOLLIT) | (1 << MiniGoParser.NILLIT) | (1 << MiniGoParser.FLOATLIT) | (1 << MiniGoParser.INTLIT) | (1 << MiniGoParser.STRLIT) | (1 << MiniGoParser.ID))) != 0):
                self.state = 363
                self.arglist()


            self.state = 366
            self.match(MiniGoParser.PAREN_CLOSE)
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
            self.state = 376
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 368
                self.vardecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 369
                self.assignstmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 370
                self.ifstmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 371
                self.forstmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 372
                self.breakstmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 373
                self.continuestmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 374
                self.returnstmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 375
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

        def struct_access(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_accessContext,0)


        def array_access(self):
            return self.getTypedRuleContext(MiniGoParser.Array_accessContext,0)


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
            self.state = 381
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 378
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.state = 379
                self.struct_access()
                pass

            elif la_ == 3:
                self.state = 380
                self.array_access()
                pass


            self.state = 383
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.OP_ASSIGN) | (1 << MiniGoParser.OP_EQUAL) | (1 << MiniGoParser.OP_ASSEQ))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 384
            self.expr(0)
            self.state = 385
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

        def nl(self):
            return self.getTypedRuleContext(MiniGoParser.NlContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def block(self):
            return self.getTypedRuleContext(MiniGoParser.BlockContext,0)


        def PAREN_OPEN(self):
            return self.getToken(MiniGoParser.PAREN_OPEN, 0)

        def PAREN_CLOSE(self):
            return self.getToken(MiniGoParser.PAREN_CLOSE, 0)

        def elseifstmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.ElseifstmtContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.ElseifstmtContext,i)


        def elsestmt(self):
            return self.getTypedRuleContext(MiniGoParser.ElsestmtContext,0)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.NEWLINE)
            else:
                return self.getToken(MiniGoParser.NEWLINE, i)

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
            self.enterOuterAlt(localctx, 1)
            self.state = 425
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.state = 387
                self.match(MiniGoParser.T__6)
                self.state = 388
                self.expr(0)
                self.state = 389
                self.block()
                self.state = 396
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 391
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==MiniGoParser.NEWLINE:
                            self.state = 390
                            self.match(MiniGoParser.NEWLINE)


                        self.state = 393
                        self.elseifstmt() 
                    self.state = 398
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

                self.state = 403
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
                if la_ == 1:
                    self.state = 400
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==MiniGoParser.NEWLINE:
                        self.state = 399
                        self.match(MiniGoParser.NEWLINE)


                    self.state = 402
                    self.elsestmt()


                pass

            elif la_ == 2:
                self.state = 405
                self.match(MiniGoParser.T__6)
                self.state = 406
                self.match(MiniGoParser.PAREN_OPEN)
                self.state = 407
                self.expr(0)
                self.state = 408
                self.match(MiniGoParser.PAREN_CLOSE)
                self.state = 409
                self.block()
                self.state = 416
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 411
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==MiniGoParser.NEWLINE:
                            self.state = 410
                            self.match(MiniGoParser.NEWLINE)


                        self.state = 413
                        self.elseifstmt() 
                    self.state = 418
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

                self.state = 423
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
                if la_ == 1:
                    self.state = 420
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==MiniGoParser.NEWLINE:
                        self.state = 419
                        self.match(MiniGoParser.NEWLINE)


                    self.state = 422
                    self.elsestmt()


                pass


            self.state = 427
            self.nl()
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
            self.state = 441
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 429
                self.match(MiniGoParser.T__7)
                self.state = 430
                self.match(MiniGoParser.T__6)
                self.state = 431
                self.expr(0)
                self.state = 432
                self.block()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 434
                self.match(MiniGoParser.T__7)
                self.state = 435
                self.match(MiniGoParser.T__6)
                self.state = 436
                self.match(MiniGoParser.PAREN_OPEN)
                self.state = 437
                self.expr(0)
                self.state = 438
                self.match(MiniGoParser.PAREN_CLOSE)
                self.state = 439
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
            self.state = 443
            self.match(MiniGoParser.T__7)
            self.state = 444
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


        def nl(self):
            return self.getTypedRuleContext(MiniGoParser.NlContext,0)


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
            self.state = 470
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 446
                self.match(MiniGoParser.T__8)
                self.state = 447
                self.expr(0)
                self.state = 448
                self.block()
                self.state = 449
                self.nl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 451
                self.match(MiniGoParser.T__8)
                self.state = 452
                self.forinit()
                self.state = 453
                self.match(MiniGoParser.SEPARATOR_SEMI)
                self.state = 454
                self.expr(0)
                self.state = 455
                self.match(MiniGoParser.SEPARATOR_SEMI)
                self.state = 456
                self.forupdate()
                self.state = 457
                self.block()
                self.state = 458
                self.nl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 460
                self.match(MiniGoParser.T__8)
                self.state = 461
                self.match(MiniGoParser.ID)
                self.state = 462
                self.match(MiniGoParser.SEPARATOR_COMMA)
                self.state = 463
                self.match(MiniGoParser.ID)
                self.state = 464
                self.match(MiniGoParser.OP_ASSEQ)
                self.state = 465
                self.match(MiniGoParser.T__9)
                self.state = 466
                self.match(MiniGoParser.ID)
                self.state = 467
                self.block()
                self.state = 468
                self.nl()
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

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def OP_ASSEQ(self):
            return self.getToken(MiniGoParser.OP_ASSEQ, 0)

        def OP_ASSIGN(self):
            return self.getToken(MiniGoParser.OP_ASSIGN, 0)

        def OP_EQUAL(self):
            return self.getToken(MiniGoParser.OP_EQUAL, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def struct_access(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_accessContext,0)


        def array_access(self):
            return self.getTypedRuleContext(MiniGoParser.Array_accessContext,0)


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
        self._la = 0 # Token type
        try:
            self.state = 480
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 475
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
                if la_ == 1:
                    self.state = 472
                    self.match(MiniGoParser.ID)
                    pass

                elif la_ == 2:
                    self.state = 473
                    self.struct_access()
                    pass

                elif la_ == 3:
                    self.state = 474
                    self.array_access()
                    pass


                self.state = 477
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.OP_ASSIGN) | (1 << MiniGoParser.OP_EQUAL) | (1 << MiniGoParser.OP_ASSEQ))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 478
                self.expr(0)
                pass
            elif token in [MiniGoParser.T__0]:
                self.enterOuterAlt(localctx, 2)
                self.state = 479
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

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def OP_ASSEQ(self):
            return self.getToken(MiniGoParser.OP_ASSEQ, 0)

        def OP_ASSIGN(self):
            return self.getToken(MiniGoParser.OP_ASSIGN, 0)

        def OP_EQUAL(self):
            return self.getToken(MiniGoParser.OP_EQUAL, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def struct_access(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_accessContext,0)


        def array_access(self):
            return self.getTypedRuleContext(MiniGoParser.Array_accessContext,0)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 485
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.state = 482
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.state = 483
                self.struct_access()
                pass

            elif la_ == 3:
                self.state = 484
                self.array_access()
                pass


            self.state = 487
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.OP_ASSIGN) | (1 << MiniGoParser.OP_EQUAL) | (1 << MiniGoParser.OP_ASSEQ))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 488
            self.expr(0)
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
            self.state = 490
            self.match(MiniGoParser.BREAK)
            self.state = 491
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
            self.state = 493
            self.match(MiniGoParser.CONTINUE)
            self.state = 494
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
            self.state = 496
            self.match(MiniGoParser.RETURN)
            self.state = 498
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.PAREN_OPEN) | (1 << MiniGoParser.BRACK_OPEN) | (1 << MiniGoParser.BOOLLIT) | (1 << MiniGoParser.NILLIT) | (1 << MiniGoParser.FLOATLIT) | (1 << MiniGoParser.INTLIT) | (1 << MiniGoParser.STRLIT) | (1 << MiniGoParser.ID))) != 0):
                self.state = 497
                self.expr(0)


            self.state = 500
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
            self.state = 502
            self.match(MiniGoParser.ID)
            self.state = 503
            self.match(MiniGoParser.PAREN_OPEN)
            self.state = 505
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.PAREN_OPEN) | (1 << MiniGoParser.BRACK_OPEN) | (1 << MiniGoParser.BOOLLIT) | (1 << MiniGoParser.NILLIT) | (1 << MiniGoParser.FLOATLIT) | (1 << MiniGoParser.INTLIT) | (1 << MiniGoParser.STRLIT) | (1 << MiniGoParser.ID))) != 0):
                self.state = 504
                self.arglist()


            self.state = 507
            self.match(MiniGoParser.PAREN_CLOSE)
            self.state = 508
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
            self.state = 510
            self.match(MiniGoParser.BRACE_OPEN)
            self.state = 514
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.T__0) | (1 << MiniGoParser.T__6) | (1 << MiniGoParser.T__8) | (1 << MiniGoParser.RETURN) | (1 << MiniGoParser.CONTINUE) | (1 << MiniGoParser.BREAK) | (1 << MiniGoParser.ID))) != 0):
                self.state = 511
                self.stmt()
                self.state = 516
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 517
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


        def struct_access(self):
            return self.getTypedRuleContext(MiniGoParser.Struct_accessContext,0)


        def array_access(self):
            return self.getTypedRuleContext(MiniGoParser.Array_accessContext,0)


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
            self.state = 537
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.state = 520
                self.match(MiniGoParser.PAREN_OPEN)
                self.state = 521
                self.expr(0)
                self.state = 522
                self.match(MiniGoParser.PAREN_CLOSE)
                pass

            elif la_ == 2:
                self.state = 524
                self.match(MiniGoParser.INTLIT)
                pass

            elif la_ == 3:
                self.state = 525
                self.match(MiniGoParser.FLOATLIT)
                pass

            elif la_ == 4:
                self.state = 526
                self.match(MiniGoParser.STRLIT)
                pass

            elif la_ == 5:
                self.state = 527
                self.match(MiniGoParser.BOOLLIT)
                pass

            elif la_ == 6:
                self.state = 528
                self.match(MiniGoParser.NILLIT)
                pass

            elif la_ == 7:
                self.state = 529
                self.methodcall()
                pass

            elif la_ == 8:
                self.state = 530
                self.funccall()
                pass

            elif la_ == 9:
                self.state = 531
                self.multi_array_literal()
                pass

            elif la_ == 10:
                self.state = 532
                self.array_literal()
                pass

            elif la_ == 11:
                self.state = 533
                self.struct_literal()
                pass

            elif la_ == 12:
                self.state = 534
                self.struct_access()
                pass

            elif la_ == 13:
                self.state = 535
                self.array_access()
                pass

            elif la_ == 14:
                self.state = 536
                self.match(MiniGoParser.ID)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 550
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,56,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 548
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 539
                        if not self.precpred(self._ctx, 17):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 17)")
                        self.state = 540
                        self.match(MiniGoParser.OP_ARITH)
                        self.state = 541
                        self.expr(18)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 542
                        if not self.precpred(self._ctx, 16):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 16)")
                        self.state = 543
                        self.match(MiniGoParser.OP_LOGIC)
                        self.state = 544
                        self.expr(17)
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 545
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 546
                        self.match(MiniGoParser.OP_COMPARE)
                        self.state = 547
                        self.expr(16)
                        pass

             
                self.state = 552
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,56,self._ctx)

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
            self.state = 555
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.SEPARATOR_SEMI, MiniGoParser.NEWLINE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 553
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.SEPARATOR_SEMI or _la==MiniGoParser.NEWLINE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [MiniGoParser.EOF]:
                self.enterOuterAlt(localctx, 2)
                self.state = 554
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
         




