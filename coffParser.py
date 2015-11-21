# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from __future__ import print_function
import sys, copy
from antlr4 import *
from cuboSemantico import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .coffListener import coffListener
else:
    from coffListener import coffListener
def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"\61\u0261\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write(u"\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t")
        buf.write(u"\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22")
        buf.write(u"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4")
        buf.write(u"\30\t\30\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35")
        buf.write(u"\t\35\4\36\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4")
        buf.write(u"$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t")
        buf.write(u",\4-\t-\4.\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63")
        buf.write(u"\t\63\4\64\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\4")
        buf.write(u"9\t9\4:\t:\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA")
        buf.write(u"\4B\tB\4C\tC\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\t")
        buf.write(u"J\4K\tK\4L\tL\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\3\2")
        buf.write(u"\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\5\3\u00ae\n\3\3\4\3")
        buf.write(u"\4\3\4\3\4\5\4\u00b4\n\4\3\5\3\5\3\5\3\5\5\5\u00ba\n")
        buf.write(u"\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\5\7\u00c6")
        buf.write(u"\n\7\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3")
        buf.write(u"\13\5\13\u00d4\n\13\3\f\3\f\3\f\3\f\5\f\u00da\n\f\3\r")
        buf.write(u"\3\r\3\r\3\r\3\r\5\r\u00e1\n\r\3\16\3\16\3\17\3\17\3")
        buf.write(u"\17\3\17\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write(u"\3\21\3\21\3\21\3\21\5\21\u00f6\n\21\3\22\3\22\3\22\3")
        buf.write(u"\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u0103\n\23")
        buf.write(u"\3\24\3\24\3\24\3\24\3\24\5\24\u010a\n\24\3\25\3\25\5")
        buf.write(u"\25\u010e\n\25\3\26\3\26\3\27\3\27\3\27\5\27\u0115\n")
        buf.write(u"\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\5\30")
        buf.write(u"\u0120\n\30\3\31\3\31\3\31\3\31\5\31\u0126\n\31\3\32")
        buf.write(u"\3\32\3\32\3\32\3\32\5\32\u012d\n\32\3\33\3\33\3\33\3")
        buf.write(u"\33\3\34\3\34\3\34\3\34\3\34\5\34\u0138\n\34\3\35\3\35")
        buf.write(u"\3\35\3\35\5\35\u013e\n\35\3\36\3\36\3\37\3\37\3\37\3")
        buf.write(u"\37\3 \3 \5 \u0148\n \3!\3!\3!\3!\3!\3\"\3\"\5\"\u0151")
        buf.write(u"\n\"\3#\3#\3#\5#\u0156\n#\3$\3$\3$\3$\3$\3$\3$\3%\3%")
        buf.write(u"\3%\5%\u0162\n%\3&\3&\3&\3&\5&\u0168\n&\3\'\3\'\3\'\3")
        buf.write(u"\'\3\'\5\'\u016f\n\'\3(\3(\3(\3)\3)\3)\3)\3)\5)\u0179")
        buf.write(u"\n)\3*\3*\3*\3+\3+\3+\3+\5+\u0182\n+\3,\3,\3-\3-\3-\3")
        buf.write(u".\3.\3.\3.\3.\5.\u018e\n.\3/\3/\3/\3\60\3\60\3\60\3\60")
        buf.write(u"\3\60\5\60\u0198\n\60\3\61\3\61\3\61\3\61\3\61\3\61\3")
        buf.write(u"\61\5\61\u01a1\n\61\3\62\3\62\3\62\5\62\u01a6\n\62\3")
        buf.write(u"\63\3\63\3\63\3\63\3\63\3\63\3\63\3\63\3\64\3\64\5\64")
        buf.write(u"\u01b2\n\64\3\65\3\65\3\66\3\66\3\67\3\67\3\67\3\67\3")
        buf.write(u"8\38\38\38\58\u01c0\n8\39\39\39\39\59\u01c6\n9\3:\3:")
        buf.write(u"\3:\3:\3:\5:\u01cd\n:\3;\3;\3;\3;\3<\3<\3<\3<\5<\u01d7")
        buf.write(u"\n<\3=\3=\3=\3=\3>\3>\3>\3>\5>\u01e1\n>\3?\3?\3?\3?\3")
        buf.write(u"?\3?\3?\3@\3@\3@\5@\u01ed\n@\3A\3A\3A\3A\3A\5A\u01f4")
        buf.write(u"\nA\3B\3B\3B\3B\3B\3B\3C\3C\3C\3C\3C\3C\3C\3C\5C\u0204")
        buf.write(u"\nC\3D\3D\3D\3D\3D\3D\3D\3D\5D\u020e\nD\3E\3E\3E\3E\3")
        buf.write(u"E\3E\3E\3F\3F\3F\3F\3F\5F\u021c\nF\3G\3G\3G\3G\3G\3G")
        buf.write(u"\3G\3G\3H\3H\3H\5H\u0229\nH\3I\3I\3I\3I\3I\5I\u0230\n")
        buf.write(u"I\3J\3J\3J\3J\3J\3J\3J\3K\3K\3K\5K\u023c\nK\3L\3L\3L")
        buf.write(u"\3L\3L\3M\3M\3M\5M\u0246\nM\3N\3N\3N\3N\3N\3O\3O\3O\3")
        buf.write(u"O\3P\3P\3P\3P\5P\u0255\nP\3Q\3Q\3Q\3Q\3R\3R\3R\3R\5R")
        buf.write(u"\u025f\nR\3R\2\2S\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write(u"\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjl")
        buf.write(u"nprtvxz|~\u0080\u0082\u0084\u0086\u0088\u008a\u008c\u008e")
        buf.write(u"\u0090\u0092\u0094\u0096\u0098\u009a\u009c\u009e\u00a0")
        buf.write(u"\u00a2\2\6\4\2\7\t--\3\2.\60\3\2\7\t\4\2\37\37!%\u024d")
        buf.write(u"\2\u00a4\3\2\2\2\4\u00ad\3\2\2\2\6\u00b3\3\2\2\2\b\u00b9")
        buf.write(u"\3\2\2\2\n\u00bb\3\2\2\2\f\u00c5\3\2\2\2\16\u00c7\3\2")
        buf.write(u"\2\2\20\u00c9\3\2\2\2\22\u00cb\3\2\2\2\24\u00d3\3\2\2")
        buf.write(u"\2\26\u00d9\3\2\2\2\30\u00e0\3\2\2\2\32\u00e2\3\2\2\2")
        buf.write(u"\34\u00e4\3\2\2\2\36\u00e8\3\2\2\2 \u00f5\3\2\2\2\"\u00f7")
        buf.write(u"\3\2\2\2$\u0102\3\2\2\2&\u0109\3\2\2\2(\u010d\3\2\2\2")
        buf.write(u"*\u010f\3\2\2\2,\u0114\3\2\2\2.\u011f\3\2\2\2\60\u0125")
        buf.write(u"\3\2\2\2\62\u012c\3\2\2\2\64\u012e\3\2\2\2\66\u0137\3")
        buf.write(u"\2\2\28\u013d\3\2\2\2:\u013f\3\2\2\2<\u0141\3\2\2\2>")
        buf.write(u"\u0147\3\2\2\2@\u0149\3\2\2\2B\u0150\3\2\2\2D\u0155\3")
        buf.write(u"\2\2\2F\u0157\3\2\2\2H\u0161\3\2\2\2J\u0167\3\2\2\2L")
        buf.write(u"\u016e\3\2\2\2N\u0170\3\2\2\2P\u0178\3\2\2\2R\u017a\3")
        buf.write(u"\2\2\2T\u0181\3\2\2\2V\u0183\3\2\2\2X\u0185\3\2\2\2Z")
        buf.write(u"\u018d\3\2\2\2\\\u018f\3\2\2\2^\u0197\3\2\2\2`\u01a0")
        buf.write(u"\3\2\2\2b\u01a5\3\2\2\2d\u01a7\3\2\2\2f\u01b1\3\2\2\2")
        buf.write(u"h\u01b3\3\2\2\2j\u01b5\3\2\2\2l\u01b7\3\2\2\2n\u01bf")
        buf.write(u"\3\2\2\2p\u01c5\3\2\2\2r\u01cc\3\2\2\2t\u01ce\3\2\2\2")
        buf.write(u"v\u01d6\3\2\2\2x\u01d8\3\2\2\2z\u01e0\3\2\2\2|\u01e2")
        buf.write(u"\3\2\2\2~\u01ec\3\2\2\2\u0080\u01f3\3\2\2\2\u0082\u01f5")
        buf.write(u"\3\2\2\2\u0084\u0203\3\2\2\2\u0086\u020d\3\2\2\2\u0088")
        buf.write(u"\u020f\3\2\2\2\u008a\u021b\3\2\2\2\u008c\u021d\3\2\2")
        buf.write(u"\2\u008e\u0228\3\2\2\2\u0090\u022f\3\2\2\2\u0092\u0231")
        buf.write(u"\3\2\2\2\u0094\u023b\3\2\2\2\u0096\u023d\3\2\2\2\u0098")
        buf.write(u"\u0245\3\2\2\2\u009a\u0247\3\2\2\2\u009c\u024c\3\2\2")
        buf.write(u"\2\u009e\u0254\3\2\2\2\u00a0\u0256\3\2\2\2\u00a2\u025e")
        buf.write(u"\3\2\2\2\u00a4\u00a5\5\4\3\2\u00a5\u00a6\5\6\4\2\u00a6")
        buf.write(u"\u00a7\5\b\5\2\u00a7\u00a8\5\n\6\2\u00a8\3\3\2\2\2\u00a9")
        buf.write(u"\u00aa\5\u0096L\2\u00aa\u00ab\5\4\3\2\u00ab\u00ae\3\2")
        buf.write(u"\2\2\u00ac\u00ae\3\2\2\2\u00ad\u00a9\3\2\2\2\u00ad\u00ac")
        buf.write(u"\3\2\2\2\u00ae\5\3\2\2\2\u00af\u00b0\5\34\17\2\u00b0")
        buf.write(u"\u00b1\5\6\4\2\u00b1\u00b4\3\2\2\2\u00b2\u00b4\3\2\2")
        buf.write(u"\2\u00b3\u00af\3\2\2\2\u00b3\u00b2\3\2\2\2\u00b4\7\3")
        buf.write(u"\2\2\2\u00b5\u00b6\5d\63\2\u00b6\u00b7\5\b\5\2\u00b7")
        buf.write(u"\u00ba\3\2\2\2\u00b8\u00ba\3\2\2\2\u00b9\u00b5\3\2\2")
        buf.write(u"\2\u00b9\u00b8\3\2\2\2\u00ba\t\3\2\2\2\u00bb\u00bc\7")
        buf.write(u"\20\2\2\u00bc\u00bd\5\f\7\2\u00bd\u00be\7-\2\2\u00be")
        buf.write(u"\u00bf\5<\37\2\u00bf\u00c0\7\27\2\2\u00c0\u00c1\5\22")
        buf.write(u"\n\2\u00c1\u00c2\7\30\2\2\u00c2\13\3\2\2\2\u00c3\u00c6")
        buf.write(u"\5\16\b\2\u00c4\u00c6\5\20\t\2\u00c5\u00c3\3\2\2\2\u00c5")
        buf.write(u"\u00c4\3\2\2\2\u00c6\r\3\2\2\2\u00c7\u00c8\5:\36\2\u00c8")
        buf.write(u"\17\3\2\2\2\u00c9\u00ca\7\5\2\2\u00ca\21\3\2\2\2\u00cb")
        buf.write(u"\u00cc\5\24\13\2\u00cc\u00cd\5\26\f\2\u00cd\u00ce\5\30")
        buf.write(u"\r\2\u00ce\23\3\2\2\2\u00cf\u00d0\5\34\17\2\u00d0\u00d1")
        buf.write(u"\5\24\13\2\u00d1\u00d4\3\2\2\2\u00d2\u00d4\3\2\2\2\u00d3")
        buf.write(u"\u00cf\3\2\2\2\u00d3\u00d2\3\2\2\2\u00d4\25\3\2\2\2\u00d5")
        buf.write(u"\u00d6\5\u0084C\2\u00d6\u00d7\5\26\f\2\u00d7\u00da\3")
        buf.write(u"\2\2\2\u00d8\u00da\3\2\2\2\u00d9\u00d5\3\2\2\2\u00d9")
        buf.write(u"\u00d8\3\2\2\2\u00da\27\3\2\2\2\u00db\u00dc\7\n\2\2\u00dc")
        buf.write(u"\u00dd\5N(\2\u00dd\u00de\7*\2\2\u00de\u00e1\3\2\2\2\u00df")
        buf.write(u"\u00e1\3\2\2\2\u00e0\u00db\3\2\2\2\u00e0\u00df\3\2\2")
        buf.write(u"\2\u00e1\31\3\2\2\2\u00e2\u00e3\t\2\2\2\u00e3\33\3\2")
        buf.write(u"\2\2\u00e4\u00e5\5\32\16\2\u00e5\u00e6\5\36\20\2\u00e6")
        buf.write(u"\u00e7\7*\2\2\u00e7\35\3\2\2\2\u00e8\u00e9\7-\2\2\u00e9")
        buf.write(u"\u00ea\5 \21\2\u00ea\37\3\2\2\2\u00eb\u00ec\7\31\2\2")
        buf.write(u"\u00ec\u00ed\7.\2\2\u00ed\u00ee\7\32\2\2\u00ee\u00f6")
        buf.write(u"\5$\23\2\u00ef\u00f0\7 \2\2\u00f0\u00f1\5*\26\2\u00f1")
        buf.write(u"\u00f2\5(\25\2\u00f2\u00f6\3\2\2\2\u00f3\u00f6\5\"\22")
        buf.write(u"\2\u00f4\u00f6\3\2\2\2\u00f5\u00eb\3\2\2\2\u00f5\u00ef")
        buf.write(u"\3\2\2\2\u00f5\u00f3\3\2\2\2\u00f5\u00f4\3\2\2\2\u00f6")
        buf.write(u"!\3\2\2\2\u00f7\u00f8\7)\2\2\u00f8\u00f9\5\36\20\2\u00f9")
        buf.write(u"#\3\2\2\2\u00fa\u0103\5(\25\2\u00fb\u00fc\7 \2\2\u00fc")
        buf.write(u"\u00fd\7\31\2\2\u00fd\u00fe\5*\26\2\u00fe\u00ff\5&\24")
        buf.write(u"\2\u00ff\u0100\7\32\2\2\u0100\u0101\5(\25\2\u0101\u0103")
        buf.write(u"\3\2\2\2\u0102\u00fa\3\2\2\2\u0102\u00fb\3\2\2\2\u0103")
        buf.write(u"%\3\2\2\2\u0104\u0105\7)\2\2\u0105\u0106\5*\26\2\u0106")
        buf.write(u"\u0107\5&\24\2\u0107\u010a\3\2\2\2\u0108\u010a\3\2\2")
        buf.write(u"\2\u0109\u0104\3\2\2\2\u0109\u0108\3\2\2\2\u010a\'\3")
        buf.write(u"\2\2\2\u010b\u010e\5\"\22\2\u010c\u010e\3\2\2\2\u010d")
        buf.write(u"\u010b\3\2\2\2\u010d\u010c\3\2\2\2\u010e)\3\2\2\2\u010f")
        buf.write(u"\u0110\t\3\2\2\u0110+\3\2\2\2\u0111\u0115\5*\26\2\u0112")
        buf.write(u"\u0113\7-\2\2\u0113\u0115\5.\30\2\u0114\u0111\3\2\2\2")
        buf.write(u"\u0114\u0112\3\2\2\2\u0115-\3\2\2\2\u0116\u0120\5\64")
        buf.write(u"\33\2\u0117\u0118\7\25\2\2\u0118\u0119\5\60\31\2\u0119")
        buf.write(u"\u011a\7\26\2\2\u011a\u0120\3\2\2\2\u011b\u011c\7\31")
        buf.write(u"\2\2\u011c\u011d\7.\2\2\u011d\u0120\7\32\2\2\u011e\u0120")
        buf.write(u"\3\2\2\2\u011f\u0116\3\2\2\2\u011f\u0117\3\2\2\2\u011f")
        buf.write(u"\u011b\3\2\2\2\u011f\u011e\3\2\2\2\u0120/\3\2\2\2\u0121")
        buf.write(u"\u0122\5N(\2\u0122\u0123\5\62\32\2\u0123\u0126\3\2\2")
        buf.write(u"\2\u0124\u0126\3\2\2\2\u0125\u0121\3\2\2\2\u0125\u0124")
        buf.write(u"\3\2\2\2\u0126\61\3\2\2\2\u0127\u0128\7)\2\2\u0128\u0129")
        buf.write(u"\5N(\2\u0129\u012a\5\62\32\2\u012a\u012d\3\2\2\2\u012b")
        buf.write(u"\u012d\3\2\2\2\u012c\u0127\3\2\2\2\u012c\u012b\3\2\2")
        buf.write(u"\2\u012d\63\3\2\2\2\u012e\u012f\7,\2\2\u012f\u0130\7")
        buf.write(u"-\2\2\u0130\u0131\5\66\34\2\u0131\65\3\2\2\2\u0132\u0133")
        buf.write(u"\7\25\2\2\u0133\u0134\58\35\2\u0134\u0135\7\26\2\2\u0135")
        buf.write(u"\u0138\3\2\2\2\u0136\u0138\3\2\2\2\u0137\u0132\3\2\2")
        buf.write(u"\2\u0137\u0136\3\2\2\2\u0138\67\3\2\2\2\u0139\u013a\5")
        buf.write(u"N(\2\u013a\u013b\5\62\32\2\u013b\u013e\3\2\2\2\u013c")
        buf.write(u"\u013e\3\2\2\2\u013d\u0139\3\2\2\2\u013d\u013c\3\2\2")
        buf.write(u"\2\u013e9\3\2\2\2\u013f\u0140\t\4\2\2\u0140;\3\2\2\2")
        buf.write(u"\u0141\u0142\7\25\2\2\u0142\u0143\5> \2\u0143\u0144\7")
        buf.write(u"\26\2\2\u0144=\3\2\2\2\u0145\u0148\5@!\2\u0146\u0148")
        buf.write(u"\3\2\2\2\u0147\u0145\3\2\2\2\u0147\u0146\3\2\2\2\u0148")
        buf.write(u"?\3\2\2\2\u0149\u014a\5:\36\2\u014a\u014b\5B\"\2\u014b")
        buf.write(u"\u014c\7-\2\2\u014c\u014d\5D#\2\u014dA\3\2\2\2\u014e")
        buf.write(u"\u0151\7(\2\2\u014f\u0151\3\2\2\2\u0150\u014e\3\2\2\2")
        buf.write(u"\u0150\u014f\3\2\2\2\u0151C\3\2\2\2\u0152\u0153\7)\2")
        buf.write(u"\2\u0153\u0156\5> \2\u0154\u0156\3\2\2\2\u0155\u0152")
        buf.write(u"\3\2\2\2\u0155\u0154\3\2\2\2\u0156E\3\2\2\2\u0157\u0158")
        buf.write(u"\7-\2\2\u0158\u0159\5H%\2\u0159\u015a\7\25\2\2\u015a")
        buf.write(u"\u015b\5J&\2\u015b\u015c\7\26\2\2\u015c\u015d\7*\2\2")
        buf.write(u"\u015dG\3\2\2\2\u015e\u015f\7,\2\2\u015f\u0162\7-\2\2")
        buf.write(u"\u0160\u0162\3\2\2\2\u0161\u015e\3\2\2\2\u0161\u0160")
        buf.write(u"\3\2\2\2\u0162I\3\2\2\2\u0163\u0164\5N(\2\u0164\u0165")
        buf.write(u"\5L\'\2\u0165\u0168\3\2\2\2\u0166\u0168\3\2\2\2\u0167")
        buf.write(u"\u0163\3\2\2\2\u0167\u0166\3\2\2\2\u0168K\3\2\2\2\u0169")
        buf.write(u"\u016a\7)\2\2\u016a\u016b\5N(\2\u016b\u016c\5L\'\2\u016c")
        buf.write(u"\u016f\3\2\2\2\u016d\u016f\3\2\2\2\u016e\u0169\3\2\2")
        buf.write(u"\2\u016e\u016d\3\2\2\2\u016fM\3\2\2\2\u0170\u0171\5R")
        buf.write(u"*\2\u0171\u0172\5P)\2\u0172O\3\2\2\2\u0173\u0174\7&\2")
        buf.write(u"\2\u0174\u0179\5N(\2\u0175\u0176\7\'\2\2\u0176\u0179")
        buf.write(u"\5N(\2\u0177\u0179\3\2\2\2\u0178\u0173\3\2\2\2\u0178")
        buf.write(u"\u0175\3\2\2\2\u0178\u0177\3\2\2\2\u0179Q\3\2\2\2\u017a")
        buf.write(u"\u017b\5X-\2\u017b\u017c\5T+\2\u017cS\3\2\2\2\u017d\u017e")
        buf.write(u"\5V,\2\u017e\u017f\5X-\2\u017f\u0182\3\2\2\2\u0180\u0182")
        buf.write(u"\3\2\2\2\u0181\u017d\3\2\2\2\u0181\u0180\3\2\2\2\u0182")
        buf.write(u"U\3\2\2\2\u0183\u0184\t\5\2\2\u0184W\3\2\2\2\u0185\u0186")
        buf.write(u"\5\\/\2\u0186\u0187\5Z.\2\u0187Y\3\2\2\2\u0188\u0189")
        buf.write(u"\7\34\2\2\u0189\u018e\5X-\2\u018a\u018b\7\33\2\2\u018b")
        buf.write(u"\u018e\5X-\2\u018c\u018e\3\2\2\2\u018d\u0188\3\2\2\2")
        buf.write(u"\u018d\u018a\3\2\2\2\u018d\u018c\3\2\2\2\u018e[\3\2\2")
        buf.write(u"\2\u018f\u0190\5`\61\2\u0190\u0191\5^\60\2\u0191]\3\2")
        buf.write(u"\2\2\u0192\u0193\7\35\2\2\u0193\u0198\5\\/\2\u0194\u0195")
        buf.write(u"\7\36\2\2\u0195\u0198\5\\/\2\u0196\u0198\3\2\2\2\u0197")
        buf.write(u"\u0192\3\2\2\2\u0197\u0194\3\2\2\2\u0197\u0196\3\2\2")
        buf.write(u"\2\u0198_\3\2\2\2\u0199\u019a\5b\62\2\u019a\u019b\5,")
        buf.write(u"\27\2\u019b\u01a1\3\2\2\2\u019c\u019d\7\25\2\2\u019d")
        buf.write(u"\u019e\5N(\2\u019e\u019f\7\26\2\2\u019f\u01a1\3\2\2\2")
        buf.write(u"\u01a0\u0199\3\2\2\2\u01a0\u019c\3\2\2\2\u01a1a\3\2\2")
        buf.write(u"\2\u01a2\u01a6\7\34\2\2\u01a3\u01a6\7\33\2\2\u01a4\u01a6")
        buf.write(u"\3\2\2\2\u01a5\u01a2\3\2\2\2\u01a5\u01a3\3\2\2\2\u01a5")
        buf.write(u"\u01a4\3\2\2\2\u01a6c\3\2\2\2\u01a7\u01a8\7\f\2\2\u01a8")
        buf.write(u"\u01a9\5f\64\2\u01a9\u01aa\7-\2\2\u01aa\u01ab\5<\37\2")
        buf.write(u"\u01ab\u01ac\7\27\2\2\u01ac\u01ad\5l\67\2\u01ad\u01ae")
        buf.write(u"\7\30\2\2\u01aee\3\2\2\2\u01af\u01b2\5h\65\2\u01b0\u01b2")
        buf.write(u"\5j\66\2\u01b1\u01af\3\2\2\2\u01b1\u01b0\3\2\2\2\u01b2")
        buf.write(u"g\3\2\2\2\u01b3\u01b4\5\32\16\2\u01b4i\3\2\2\2\u01b5")
        buf.write(u"\u01b6\7\5\2\2\u01b6k\3\2\2\2\u01b7\u01b8\5n8\2\u01b8")
        buf.write(u"\u01b9\5p9\2\u01b9\u01ba\5r:\2\u01bam\3\2\2\2\u01bb\u01bc")
        buf.write(u"\5\34\17\2\u01bc\u01bd\5n8\2\u01bd\u01c0\3\2\2\2\u01be")
        buf.write(u"\u01c0\3\2\2\2\u01bf\u01bb\3\2\2\2\u01bf\u01be\3\2\2")
        buf.write(u"\2\u01c0o\3\2\2\2\u01c1\u01c2\5\u0084C\2\u01c2\u01c3")
        buf.write(u"\5p9\2\u01c3\u01c6\3\2\2\2\u01c4\u01c6\3\2\2\2\u01c5")
        buf.write(u"\u01c1\3\2\2\2\u01c5\u01c4\3\2\2\2\u01c6q\3\2\2\2\u01c7")
        buf.write(u"\u01c8\7\n\2\2\u01c8\u01c9\5N(\2\u01c9\u01ca\7*\2\2\u01ca")
        buf.write(u"\u01cd\3\2\2\2\u01cb\u01cd\3\2\2\2\u01cc\u01c7\3\2\2")
        buf.write(u"\2\u01cc\u01cb\3\2\2\2\u01cds\3\2\2\2\u01ce\u01cf\7\27")
        buf.write(u"\2\2\u01cf\u01d0\5v<\2\u01d0\u01d1\7\30\2\2\u01d1u\3")
        buf.write(u"\2\2\2\u01d2\u01d3\5\u0084C\2\u01d3\u01d4\5v<\2\u01d4")
        buf.write(u"\u01d7\3\2\2\2\u01d5\u01d7\3\2\2\2\u01d6\u01d2\3\2\2")
        buf.write(u"\2\u01d6\u01d5\3\2\2\2\u01d7w\3\2\2\2\u01d8\u01d9\7\27")
        buf.write(u"\2\2\u01d9\u01da\5z>\2\u01da\u01db\7\30\2\2\u01dby\3")
        buf.write(u"\2\2\2\u01dc\u01dd\5\u0086D\2\u01dd\u01de\5v<\2\u01de")
        buf.write(u"\u01e1\3\2\2\2\u01df\u01e1\3\2\2\2\u01e0\u01dc\3\2\2")
        buf.write(u"\2\u01e0\u01df\3\2\2\2\u01e1{\3\2\2\2\u01e2\u01e3\7-")
        buf.write(u"\2\2\u01e3\u01e4\5~@\2\u01e4\u01e5\5\u0080A\2\u01e5\u01e6")
        buf.write(u"\7 \2\2\u01e6\u01e7\5N(\2\u01e7\u01e8\7*\2\2\u01e8}\3")
        buf.write(u"\2\2\2\u01e9\u01ea\7,\2\2\u01ea\u01ed\7-\2\2\u01eb\u01ed")
        buf.write(u"\3\2\2\2\u01ec\u01e9\3\2\2\2\u01ec\u01eb\3\2\2\2\u01ed")
        buf.write(u"\177\3\2\2\2\u01ee\u01ef\7\31\2\2\u01ef\u01f0\5N(\2\u01f0")
        buf.write(u"\u01f1\7\32\2\2\u01f1\u01f4\3\2\2\2\u01f2\u01f4\3\2\2")
        buf.write(u"\2\u01f3\u01ee\3\2\2\2\u01f3\u01f2\3\2\2\2\u01f4\u0081")
        buf.write(u"\3\2\2\2\u01f5\u01f6\7\6\2\2\u01f6\u01f7\7\25\2\2\u01f7")
        buf.write(u"\u01f8\5N(\2\u01f8\u01f9\7\26\2\2\u01f9\u01fa\5x=\2\u01fa")
        buf.write(u"\u0083\3\2\2\2\u01fb\u01fc\7\23\2\2\u01fc\u0204\5F$\2")
        buf.write(u"\u01fd\u01fe\7\24\2\2\u01fe\u0204\5|?\2\u01ff\u0204\5")
        buf.write(u"\u0082B\2\u0200\u0204\5\u0092J\2\u0201\u0204\5\u0088")
        buf.write(u"E\2\u0202\u0204\5\u008cG\2\u0203\u01fb\3\2\2\2\u0203")
        buf.write(u"\u01fd\3\2\2\2\u0203\u01ff\3\2\2\2\u0203\u0200\3\2\2")
        buf.write(u"\2\u0203\u0201\3\2\2\2\u0203\u0202\3\2\2\2\u0204\u0085")
        buf.write(u"\3\2\2\2\u0205\u0206\7\23\2\2\u0206\u020e\5F$\2\u0207")
        buf.write(u"\u0208\7\24\2\2\u0208\u020e\5|?\2\u0209\u020e\5\u0082")
        buf.write(u"B\2\u020a\u020e\5\u0092J\2\u020b\u020e\5\u0088E\2\u020c")
        buf.write(u"\u020e\5\u008cG\2\u020d\u0205\3\2\2\2\u020d\u0207\3\2")
        buf.write(u"\2\2\u020d\u0209\3\2\2\2\u020d\u020a\3\2\2\2\u020d\u020b")
        buf.write(u"\3\2\2\2\u020d\u020c\3\2\2\2\u020e\u0087\3\2\2\2\u020f")
        buf.write(u"\u0210\7\3\2\2\u0210\u0211\7\25\2\2\u0211\u0212\5N(\2")
        buf.write(u"\u0212\u0213\5\u008aF\2\u0213\u0214\7\26\2\2\u0214\u0215")
        buf.write(u"\7*\2\2\u0215\u0089\3\2\2\2\u0216\u0217\7)\2\2\u0217")
        buf.write(u"\u0218\5N(\2\u0218\u0219\5\u008aF\2\u0219\u021c\3\2\2")
        buf.write(u"\2\u021a\u021c\3\2\2\2\u021b\u0216\3\2\2\2\u021b\u021a")
        buf.write(u"\3\2\2\2\u021c\u008b\3\2\2\2\u021d\u021e\7\4\2\2\u021e")
        buf.write(u"\u021f\7\25\2\2\u021f\u0220\7-\2\2\u0220\u0221\5\u008e")
        buf.write(u"H\2\u0221\u0222\5\u0090I\2\u0222\u0223\7\26\2\2\u0223")
        buf.write(u"\u0224\7*\2\2\u0224\u008d\3\2\2\2\u0225\u0226\7,\2\2")
        buf.write(u"\u0226\u0229\7-\2\2\u0227\u0229\3\2\2\2\u0228\u0225\3")
        buf.write(u"\2\2\2\u0228\u0227\3\2\2\2\u0229\u008f\3\2\2\2\u022a")
        buf.write(u"\u022b\7\31\2\2\u022b\u022c\5N(\2\u022c\u022d\7\32\2")
        buf.write(u"\2\u022d\u0230\3\2\2\2\u022e\u0230\3\2\2\2\u022f\u022a")
        buf.write(u"\3\2\2\2\u022f\u022e\3\2\2\2\u0230\u0091\3\2\2\2\u0231")
        buf.write(u"\u0232\7\21\2\2\u0232\u0233\7\25\2\2\u0233\u0234\5N(")
        buf.write(u"\2\u0234\u0235\7\26\2\2\u0235\u0236\5t;\2\u0236\u0237")
        buf.write(u"\5\u0094K\2\u0237\u0093\3\2\2\2\u0238\u0239\7\22\2\2")
        buf.write(u"\u0239\u023c\5t;\2\u023a\u023c\3\2\2\2\u023b\u0238\3")
        buf.write(u"\2\2\2\u023b\u023a\3\2\2\2\u023c\u0095\3\2\2\2\u023d")
        buf.write(u"\u023e\7\13\2\2\u023e\u023f\7-\2\2\u023f\u0240\5\u0098")
        buf.write(u"M\2\u0240\u0241\5\u009aN\2\u0241\u0097\3\2\2\2\u0242")
        buf.write(u"\u0243\7\r\2\2\u0243\u0246\7-\2\2\u0244\u0246\3\2\2\2")
        buf.write(u"\u0245\u0242\3\2\2\2\u0245\u0244\3\2\2\2\u0246\u0099")
        buf.write(u"\3\2\2\2\u0247\u0248\7\27\2\2\u0248\u0249\5\u009cO\2")
        buf.write(u"\u0249\u024a\5\u00a0Q\2\u024a\u024b\7\30\2\2\u024b\u009b")
        buf.write(u"\3\2\2\2\u024c\u024d\7\16\2\2\u024d\u024e\7+\2\2\u024e")
        buf.write(u"\u024f\5\u009eP\2\u024f\u009d\3\2\2\2\u0250\u0251\5\34")
        buf.write(u"\17\2\u0251\u0252\5\u009eP\2\u0252\u0255\3\2\2\2\u0253")
        buf.write(u"\u0255\3\2\2\2\u0254\u0250\3\2\2\2\u0254\u0253\3\2\2")
        buf.write(u"\2\u0255\u009f\3\2\2\2\u0256\u0257\7\17\2\2\u0257\u0258")
        buf.write(u"\7+\2\2\u0258\u0259\5\u00a2R\2\u0259\u00a1\3\2\2\2\u025a")
        buf.write(u"\u025b\5d\63\2\u025b\u025c\5\u00a2R\2\u025c\u025f\3\2")
        buf.write(u"\2\2\u025d\u025f\3\2\2\2\u025e\u025a\3\2\2\2\u025e\u025d")
        buf.write(u"\3\2\2\2\u025f\u00a3\3\2\2\2\60\u00ad\u00b3\u00b9\u00c5")
        buf.write(u"\u00d3\u00d9\u00e0\u00f5\u0102\u0109\u010d\u0114\u011f")
        buf.write(u"\u0125\u012c\u0137\u013d\u0147\u0150\u0155\u0161\u0167")
        buf.write(u"\u016e\u0178\u0181\u018d\u0197\u01a0\u01a5\u01b1\u01bf")
        buf.write(u"\u01c5\u01cc\u01d6\u01e0\u01ec\u01f3\u0203\u020d\u021b")
        buf.write(u"\u0228\u022f\u023b\u0245\u0254\u025e")
        return buf.getvalue()


class coffParser ( Parser ):

    grammarFileName = "java-escape"

    tipoVariableActual = None

    idVariableActual = None

    tokenActual = None

    ejecToken = None

    tipoActualFuncion = None

    dirProcs = {}

    scopeProcs = 0

    metodoTof = 1

    claseScopeRef = 0

    globalTof = 0

    listaParametros = []

    tablaVariables = {}
    
    pilaParam = [] #pila que guada los cuadruplos de parametros para procesar despues

    parametrosAux = [] #variable usada guardar el procedimiento donde se agregaran parametros

    nComas = 0 #variable usada para hacer la validacion semantica simple entre encabezado y llamado de funcion
    nComasAux = 0 #ayuda a considerar el caso donde solo hay un parametro
    nComasAux2 = 0 #ayuda a considerar el caso donde solo hay un parametro
    funcionOmetodo = 0 #1 funcion 2 metodo


    atributosTof = 0 
    atributosClase = [] #variable usada para agregar los atributos de cada clase en el registro dirprocs(clase)
    metodosClase = [] #variable usada para agregar los metodos de cada clase en el registro dirprocs(clase)
    claseIDRef = None


    esTipoFuncionOMetodo = 0
    tipoActualFuncionOMetodo = None

    idFuncionActual = None

    valorDeclaracion = None #Valor de la delcaracion
    
    tipoDeclaracion = None #Tipo de la delcaracion

    terminacionProcs = None # para saber si estoy en principal o en una funcion

    esAtributo = 0

    pilaO = [] #Pila de operandos

    pOper = [] #Pila de operadores

    pTipos = [] #Pila de tipos de los operadores

    pSaltos = [] #Pila de saltos para los condicionales y los ciclos

    quadruplos = [] #Lista de cuadruplos

    contadorParametros = [] #Pila que guarda en que parametro se esta revisando

    contQuadTemporales = 1 #Para variables temporales

    quadOperadores = [['*','/'],['+','-'],['==','!=','>','>=','<','<='],['&&','||'],['=']]

    tofFactor = 0
    ################################################# revisar CAVAZOS
    memGlobalEntero = -1 #Contador para memoria virtual de variables globales enteras

    memGlobalDecimal = 2999 #Contador para memoria virtual de variables globales decimales

    memGlobalTexto = 5999 #Contador para memoria virtual de variables globales texto

    memLocalEntero = 8999 #Contador para memoria virtual de variables locales y temporales enteras

    memLocalDecimal = 14999 #Contador para memoria virtual de variables locales y temporales decimales

    memLocalTexto = 20999 #Contador para memoria virtual de variables locales y temporales texto
    ####################################################

    cuboSemantico = cuboSemantico() #Para hacer las validaciones semanticas


    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'imprimir'", u"'leer'", u"'vacio'", 
                     u"'mientras'", u"'entero'", u"'decimal'", u"'texto'", 
                     u"'retorna'", u"'clase'", u"'funcion'", u"'extiende'", 
                     u"'atributos'", u"'metodos'", u"'principal'", u"'si'", 
                     u"'o'", u"'ejec'", u"'asigna'", u"'('", u"')'", u"'{'", 
                     u"'}'", u"'['", u"']'", u"'+'", u"'-'", u"'/'", u"'*'", 
                     u"'=='", u"'='", u"'<'", u"'>'", u"'>='", u"'<='", 
                     u"'!='", u"'||'", u"'&&'", u"'&'", u"','", u"';'", 
                     u"':'", u"'.'" ]

    symbolicNames = [ u"<INVALID>", u"IMPRIMIR", u"LEER", u"VACIO", u"MIENTRAS", 
                      u"ENTERO", u"DECIMAL", u"TEXTO", u"RETORNA", u"CLASE", 
                      u"FUNCION", u"EXTIENDE", u"ATRIBUTOS", u"METODOS", 
                      u"PRINCIPAL", u"SI", u"O", u"EJEC", u"ASIGNA", u"PIZQ", 
                      u"PDER", u"BIZQ", u"BDER", u"CIZQ", u"CDER", u"SUMA", 
                      u"RESTA", u"DIV", u"MULT", u"IGUALQUE", u"IGUAL", 
                      u"MENQUE", u"MAYQUE", u"MAYIGUALQUE", u"MENIGUALQUE", 
                      u"DIF", u"CONDICIONO", u"CONDICIONY", u"AMP", u"COMA", 
                      u"PUNTOYCOMA", u"DOSPUNTOS", u"PUNTO", u"ID", u"CTEENT", 
                      u"CTEDEC", u"CTETEXTO", u"WS" ]

    RULE_programa = 0
    RULE_p1 = 1
    RULE_p2 = 2
    RULE_p3 = 3
    RULE_principal = 4
    RULE_pr1 = 5
    RULE_pr11 = 6
    RULE_pr12 = 7
    RULE_pr2 = 8
    RULE_pr23 = 9
    RULE_pr21 = 10
    RULE_pr22 = 11
    RULE_tipo = 12
    RULE_variables = 13
    RULE_v1 = 14
    RULE_v2 = 15
    RULE_v3 = 16
    RULE_v4 = 17
    RULE_v5 = 18
    RULE_v6 = 19
    RULE_valordeclaracion = 20
    RULE_valor = 21
    RULE_va1 = 22
    RULE_va2 = 23
    RULE_va3 = 24
    RULE_va4 = 25
    RULE_va5 = 26
    RULE_va6 = 27
    RULE_tiposimple = 28
    RULE_parametros = 29
    RULE_pa1 = 30
    RULE_pa11 = 31
    RULE_pa2 = 32
    RULE_pa3 = 33
    RULE_llamarfunmet = 34
    RULE_ll1 = 35
    RULE_ll2 = 36
    RULE_ll3 = 37
    RULE_expresion = 38
    RULE_ex1 = 39
    RULE_declaracion = 40
    RULE_de1 = 41
    RULE_de2 = 42
    RULE_exp = 43
    RULE_exp1 = 44
    RULE_termino = 45
    RULE_t1 = 46
    RULE_factor = 47
    RULE_f1 = 48
    RULE_funcion = 49
    RULE_fun1 = 50
    RULE_fun11 = 51
    RULE_fun12 = 52
    RULE_fun2 = 53
    RULE_fun23 = 54
    RULE_fun21 = 55
    RULE_fun22 = 56
    RULE_bloque = 57
    RULE_b1 = 58
    RULE_bloquesimple = 59
    RULE_bs1 = 60
    RULE_asignacion = 61
    RULE_a1 = 62
    RULE_a2 = 63
    RULE_mientras = 64
    RULE_estatuto = 65
    RULE_estatutosimple = 66
    RULE_escritura = 67
    RULE_e1 = 68
    RULE_lectura = 69
    RULE_l1 = 70
    RULE_l2 = 71
    RULE_si = 72
    RULE_si1 = 73
    RULE_clases = 74
    RULE_cl1 = 75
    RULE_cl2 = 76
    RULE_atributos = 77
    RULE_atr1 = 78
    RULE_metodos = 79
    RULE_met1 = 80

    ruleNames =  [ u"programa", u"p1", u"p2", u"p3", u"principal", u"pr1", 
                   u"pr11", u"pr12", u"pr2", u"pr23", u"pr21", u"pr22", 
                   u"tipo", u"variables", u"v1", u"v2", u"v3", u"v4", u"v5", 
                   u"v6", u"valordeclaracion", u"valor", u"va1", u"va2", 
                   u"va3", u"va4", u"va5", u"va6", u"tiposimple", u"parametros", 
                   u"pa1", u"pa11", u"pa2", u"pa3", u"llamarfunmet", u"ll1", 
                   u"ll2", u"ll3", u"expresion", u"ex1", u"declaracion", 
                   u"de1", u"de2", u"exp", u"exp1", u"termino", u"t1", u"factor", 
                   u"f1", u"funcion", u"fun1", u"fun11", u"fun12", u"fun2", 
                   u"fun23", u"fun21", u"fun22", u"bloque", u"b1", u"bloquesimple", 
                   u"bs1", u"asignacion", u"a1", u"a2", u"mientras", u"estatuto", 
                   u"estatutosimple", u"escritura", u"e1", u"lectura", u"l1", 
                   u"l2", u"si", u"si1", u"clases", u"cl1", u"cl2", u"atributos", 
                   u"atr1", u"metodos", u"met1" ]

    EOF = Token.EOF
    IMPRIMIR=1
    LEER=2
    VACIO=3
    MIENTRAS=4
    ENTERO=5
    DECIMAL=6
    TEXTO=7
    RETORNA=8
    CLASE=9
    FUNCION=10
    EXTIENDE=11
    ATRIBUTOS=12
    METODOS=13
    PRINCIPAL=14
    SI=15
    O=16
    EJEC=17
    ASIGNA=18
    PIZQ=19
    PDER=20
    BIZQ=21
    BDER=22
    CIZQ=23
    CDER=24
    SUMA=25
    RESTA=26
    DIV=27
    MULT=28
    IGUALQUE=29
    IGUAL=30
    MENQUE=31
    MAYQUE=32
    MAYIGUALQUE=33
    MENIGUALQUE=34
    DIF=35
    CONDICIONO=36
    CONDICIONY=37
    AMP=38
    COMA=39
    PUNTOYCOMA=40
    DOSPUNTOS=41
    PUNTO=42
    ID=43
    CTEENT=44
    CTEDEC=45
    CTETEXTO=46
    WS=47

    def __init__(self, input):
        super(coffParser, self).__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None

    def insertarVariableEnMemoria(self,variableActual):
        direccion = None
        isClase = False
        isGlobal = False
        dicAtributos = {}
        tipoVar = None

        #variables globales
        if self.globalTof: 
            tipoVar = self.tablaVariables[variableActual,0][0]
            if tipoVar == "entero":
                self.memGlobalEntero = self.memGlobalEntero + 1
                direccion = self.memGlobalEntero
            elif tipoVar == "decimal":
                self.memGlobalDecimal = self.memGlobalDecimal + 1
                direccion = self.memGlobalDecimal
            elif tipoVar == "texto":
                self.memGlobalTexto = self.memGlobalTexto + 1
                direccion = self.memGlobalTexto
            else:
                for atributo in self.dirProcs[tipoVar,0][2]:
                    tipoAtributo = self.tablaVariables[atributo[0],atributo[1]][0]
                    if tipoAtributo == "entero":
                        self.memGlobalEntero = self.memGlobalEntero + 1
                    elif tipoAtributo == "decimal":
                        self.memGlobalDecimal = self.memGlobalDecimal + 1
                    elif tipoAtributo == "texto":
                        self.memGlobalTexto = self.memGlobalTexto + 1


        #variables locales
        if self.globalTof == 0:
            tipoVar = self.tablaVariables[variableActual,self.scopeProcs][0]
            if tipoVar == "entero":
                self.memLocalEntero = self.memLocalEntero + 1
                direccion = self.memLocalEntero
            elif tipoVar == "decimal":
                self.memLocalDecimal = self.memLocalDecimal + 1
                direccion = self.memLocalDecimal
            elif tipoVar == "texto":
                self.memLocalTexto = self.memLocalTexto + 1
                direccion = self.memLocalTexto
            else:
                for atributo in self.dirProcs[tipoVar,0][2]:
                    tipoAtributo = self.tablaVariables[atributo[0],atributo[1]][0]
                    if tipoAtributo == "entero":
                        self.memLocalEntero = self.memLocalEntero + 1
                    elif tipoAtributo == "decimal":
                        self.memLocalDecimal = self.memLocalDecimal + 1
                    elif tipoAtributo == "texto":
                        self.memLocalTexto = self.memLocalTexto + 1
        #print("Variable:",variableActual)
        #self.imprimeMemoria()

    def imprimeMemoria(self):
        print("")
        print("Global")
        print("memGlobalEntero:",self.memGlobalEntero)
        print("memGlobalDecimal:",self.memGlobalDecimal)
        print("memGlobalTexto:",self.memGlobalTexto)
        print("Local")
        print("memLocalEntero:",self.memLocalEntero)
        print("memLocalDecimal:",self.memLocalDecimal)
        print("memLocalTexto:",self.memLocalTexto)
        print("")

    def resetearDireccionesLocales(self):
        self.memLocalEntero = 8999
        self.memLocalDecimal = 14999
        self.memLocalTexto = 20999


    def insertarValorTipo(self,op,tipoOp):
        self.pilaO.append(op)
        self.pTipos.append(tipoOp)

    def insertarOperador(self,op):
        self.pOper.append(op)


    def obtenerTipoDeAtributo(self, nombreAtributo, nombreClase):
        return self.tablaVariables[nombreAtributo,self.dirProcs[nombreClase,0][0]]   


    def crearCuadruploExpAsig(self,op,tipoCuadruplo):
        #OP = 0 - mult,div 1 - suma,resta 2 - relacionales 3 - logicos 4 - asignacion
        if self.pOper:
            oper = self.pOper.pop()
            if oper in self.quadOperadores[op]:
                if self.pilaO:
                    oDer = self.pilaO.pop()
                    oDerTipo = self.pTipos.pop()
                    if self.pilaO:
                        oIzq = self.pilaO.pop()
                        oIzqTipo = self.pTipos.pop()
                        res = self.cuboSemantico.checarSemanticaExp(oIzqTipo,oDerTipo,oper)
                        if res != None:
                            if tipoCuadruplo == 'expresion':
                                if res == "entero":
                                    self.memLocalEntero = self.memLocalEntero + 1
                                    auxDireccion = self.memLocalEntero
                                elif res == "decimal":
                                    self.memLocalDecimal = self.memLocalDecimal + 1
                                    auxDireccion = self.memLocalDecimal
                                elif res == "texto":
                                    self.memLocalTexto = self.memLocalTexto + 1
                                    auxDireccion = self.memLocalTexto

                                self.quadruplos.append([oper,oIzq,oDer,auxDireccion])
                                self.insertarValorTipo(auxDireccion,res)
                                self.contQuadTemporales = self.contQuadTemporales + 1
                            elif tipoCuadruplo == 'asignacion':
                                self.quadruplos.append([oper,oDer,None,oIzq])
                        else:
                            print ("Error semantico en la linea:" + str(self.getCurrentToken().line) + " Tipos de operandos no compatibles" )
                            sys.exit()
                            self._syntaxErrors = self._syntaxErrors + 1
                            return
                    else:
                        self.pilaO.append(oDer)
                        self.pTipos.append(oDerTipo)
                        self.pOper.append(oper)
            else:
                self.pOper.append(oper)


    def crearCuadruploEscritura(self):
        if self.pilaO:
            elemento = self.pilaO.pop()
            elementoTipo = self.pTipos.pop()
            elementoTipo = elementoTipo.split(',')
            if len(elementoTipo) == 1:
                self.quadruplos.append(['imprimir',None,None,elemento])
            else:
                #Para arreglos! CHECAR
                x = int(elementoTipo[2])
                while x > 0:
                    self.quadruplos.append(['imprimir',None,None,elemento])
                    elemento = elemento + 1
                    x = x - 1

    def crearCuadruploLectura(self,elemento):
        self.quadruplos.append(['leer',None,None,elemento])


    def crearCuadruploCondicion(self):
        condicion = self.pilaO.pop()
        tipoCondicion = self.pTipos.pop()
        if tipoCondicion != 'entero':
            print ("Error semantico en la linea:" + str(self.getCurrentToken().line) + " se esperaba una condicion" )
            self._syntaxErrors = self._syntaxErrors + 1
            sys.exit()
            return
        else:
            self.quadruplos.append(['gotof',condicion,None,None])
            cont = len(self.quadruplos)
            self.pSaltos.append(cont-1)

    def crearCuadruploCondicionFalso(self):
        falso = self.pSaltos.pop()
        self.quadruplos.append(['goto',None,None,None])
        cont = len(self.quadruplos)
        self.pSaltos.append(cont-1)
        self.quadruplos[falso][3] = cont

    def crearCuadruploCondicionSalida(self):
        salida = self.pSaltos.pop()
        cont = len(self.quadruplos)
        self.quadruplos[salida][3] = cont

    def crearCuadruploCondicionInicioCiclo(self):
        cont = len(self.quadruplos)
        self.pSaltos.append(cont)

    def crearCuadruploCondicionFinCiclo(self):
        falso = self.pSaltos.pop()
        retorno = self.pSaltos.pop()
        self.quadruplos.append(['goto',None,None,retorno])
        cont = len(self.quadruplos)
        self.quadruplos[falso][3] = cont



    def checkIfVariableExists(self):
        if (self.idVariableActual, self.scopeProcs)  not in self.tablaVariables:
            if (self.idVariableActual, 0)  not in self.tablaVariables:
                presente = 0
                if self.claseIDRef:
                    for variable in self.dirProcs[self.claseIDRef,0][2]:
                        if self.idVariableActual == variable[0]:
                            presente = variable
                if presente == 0:
                    print ("Error, la variable "+self.idVariableActual+" no ha sido declarada")
                    sys.exit()
                    return
                else:   
                    return self.tablaVariables[self.idVariableActual, presente[1]][0]
            else:
                return self.tablaVariables[self.idVariableActual, 0][0]
        else:
            return self.tablaVariables[self.idVariableActual,self.scopeProcs][0]

    def lookForMethodClass(self): 
        instanciaID = self.ejecToken
        metodoID = self.tokenActual
        tipoObjeto = self.tablaVariables[instanciaID,self.scopeProcs][0] #contiene el tipo del objeto
        try:
            claseID = self.dirProcs[tipoObjeto,0][0] #contiene el id de la clase
        except KeyError:
            print ("Error, "+self.ejecToken+" es una variable simple")
            sys.exit()
            return

        if(metodoID, claseID) not in self.dirProcs: #tokenActual contiene el nombre del metodo
            print("Error, el metodo "+metodoID+" no es compatible con la clase de "+instanciaID)
            sys.exit()


    def checkIfGlobalFunctionOrClassExists(self,fgcID):
        if (fgcID, 0) not in self.dirProcs:
            print("Error, la funcion global o clase "+fgcID+" no ha sido declarada")
            sys.exit()
            return


    def checkIfAttributeBelongs(self,nombreAtributo,nombreInstanciaClase):
        #idVariableActual contiene el atributo
        #ejecToken contiene el id de la instancia de la clase

        try:
            tipoAtributo = self.tablaVariables[nombreInstanciaClase,self.scopeProcs][0]
        except KeyError:
            print ("Error, la variable "+nombreInstanciaClase+" no ha sido declarada")
            sys.exit()
            return
        
        try:
            checkifAttributeBelongsClassID = self.dirProcs[tipoAtributo, 0][0] 
        except KeyError:
            print ("Error, "+nombreInstanciaClase+" es una variable simple")
            sys.exit()
            return

        if (nombreAtributo, checkifAttributeBelongsClassID)  not in self.tablaVariables:
                print("Error, el atributo "+nombreAtributo+" no pertenece a la clase de "+nombreInstanciaClase)
                sys.exit()
                return

    def checkForAttributeCollisionsInheritance(self,sonAttribute, fatherAttributes):
        for fatherAttribute in fatherAttributes:
            if sonAttribute[0] == fatherAttribute[0]:
                print("Error, atributo "+ sonAttribute[0]+" repetido")
                sys.exit()
                return

    def makeInheritance(self,sonID,fatherID):
        if sonID == fatherID:
            print("Error, la clase "+sonID+" esta heredando a si misma")
            sys.error()
            return
        self.dirProcs[sonID,0][2] = (self.dirProcs[fatherID,0][2]) 
        self.dirProcs[sonID,0][3] = (self.dirProcs[fatherID,0][3]) 

    def checkForMethodCollisionsInheritance(self,sonMethod, fatherMethods):

        for fatherMethod in fatherMethods:
            if sonMethod[0] == fatherMethod[0]:
                print("Error, metodo "+ sonMethod[0]+" repetido")
                sys.exit()
                return

    def crearCuadruploMain(self):
        self.quadruplos.append(['goto',None,None,None])


    def completarCuadruploMain(self):
        cont = len(self.quadruplos)
        self.quadruplos[0][3] = cont

    cuadruploFinVarsGlobales = 0
    def crearCuadruploVarsGlobales(self):
        self.cuadruploFinVarsGlobales = len(self.quadruplos)
        self.quadruplos.append(['goto',None,None,None])

    def completarCuadruploVarsGlobales(self):
        cont = len(self.quadruplos)
        self.quadruplos[self.cuadruploFinVarsGlobales][3] = cont

    def crearCuadruploTerminarProc(self):
        self.quadruplos.append([self.terminacionProc,None,None,None])


    def crearCuadruploRetornar(self):
        elemento = self.pilaO.pop()
        tipoElemento = self.pTipos.pop()
        self.quadruplos.append(['retornar',None,None,elemento])

    def idDeMetodo(self,nombreMetodo):
        if(self.metodoTof):
            for key, values in self.dirProcs.items():
                if key[0] == nombreMetodo and key[1] != 0:
                    return key[1]
        else:
            return 0

    def getNumberOfEDT(self,procTuple): #getNumberOfEnteroDecimalTexto
        nEnteros = 0
        nDecimales = 0
        nTexto = 0

        for keys,values in self.tablaVariables.items():

            if keys[1] == self.dirProcs[procTuple[0],procTuple[1]][0]: #si tienen el mismo id
                tipoVariable = values[0]
                if tipoVariable == "entero":
                    nEnteros = nEnteros + 1
                elif tipoVariable == "decimal":
                    nDecimales = nDecimales + 1
                elif tipoVariable == "texto":
                    nTexto = nTexto + 1
                else:
                    for atributo in self.dirProcs[tipoVariable,0][2]:
                        tipoAtributo = self.tablaVariables[atributo[0],atributo[1]][0]
                        if tipoAtributo == "entero":
                            nEnteros = nEnteros + 1
                        elif tipoAtributo == "decimal":
                            nDecimales = nDecimales + 1
                        elif tipoAtributo == "texto":
                            nTexto = nTexto + 1

        return([nEnteros,nDecimales,nTexto])

    def obtenerClaseDeUnaFuncionEra(self, nombreVariable, nombreFuncion):
        if nombreVariable == None:
            return None
        aux = self.tablaVariables[nombreVariable,self.scopeProcs][0]
        return aux

    def obtenerTipoDeUnMetodoEra(self, nombreVariable, nombreFuncion):
        clase = self.obtenerClaseDeUnaFuncionEra(nombreVariable,nombreFuncion)
        if clase == None:
            return None
        idClasePadre = self.dirProcs[clase,0][0]
        return self.dirProcs[nombreFuncion,idClasePadre][1]

    def obtenerTipoDeUnaFuncionEra(self, nombreFuncion):
        return self.dirProcs[nombreFuncion,0][1]


    def crearCuadruploEra(self, nombreVariable, nombreFuncion):
        clase = self.obtenerClaseDeUnaFuncionEra(nombreVariable, nombreFuncion)
        self.quadruplos.append(['era',None,clase,nombreFuncion])


    def obtenerCantidadParametrosFuncionOMetodo(self,nombreVariable,nombreFuncion):
        if nombreVariable == None:
            try:
                return len(self.dirProcs[nombreFuncion,0][2])
            except:
                print("Error, la funcion "+nombreFuncion+" no ha sido declarada")
                sys.exit()
                return
        else:   
            clase = self.obtenerClaseDeUnaFuncionEra(nombreVariable,nombreFuncion)
            idClasePadre = self.dirProcs[clase,0][0]
            return len(self.dirProcs[nombreFuncion,idClasePadre][2])

    def checaTipoExpresionConParametro(self,nombreVariable,nombreFuncion):
        tipoExpresion = self.pTipos[len(self.pTipos)-1]
        if nombreVariable == None:
            var = self.dirProcs[nombreFuncion,0][2][self.contadorParametros[len(self.contadorParametros)-1]][0]
            scope = self.dirProcs[nombreFuncion,0][2][self.contadorParametros[len(self.contadorParametros)-1]][1]
        else:
            clase = self.obtenerClaseDeUnaFuncionEra(nombreVariable,nombreFuncion)
            idClasePadre = self.dirProcs[clase,0][0]
            var = self.dirProcs[nombreFuncion,idClasePadre][2][self.contadorParametros[len(self.contadorParametros)-1]][0]
            scope = self.dirProcs[nombreFuncion,idClasePadre][2][self.contadorParametros[len(self.contadorParametros)-1]][1]


        tipoParametro = self.tablaVariables[var,scope][0]


        if tipoExpresion == tipoParametro:

            self.contadorParametros[len(self.contadorParametros)-1] = self.contadorParametros[len(self.contadorParametros)-1] + 1 
        else:

            print("Error en la linea " + str(self.getCurrentToken().line) +", tipos no coinciden con la funcion o metodo")
            sys.exit()
            return
        
    def crearCuadruploParam(self):
        while len(self.pilaParam) > 0:
            self.quadruplos.append(self.pilaParam[0])
            self.pilaParam.pop(0)


    def guardarCuadruploParam(self,direccionParametro):
        operando = self.pilaO.pop()
        self.pTipos.pop()
        self.pilaParam.append(['param',0,direccionParametro,operando])

    def obtenerCuadruploInicioFuncion(self,nombreVariable,nombreFuncion):
        if nombreVariable == None:
            return self.dirProcs[nombreFuncion,0][4]
        else:
            clase = self.obtenerClaseDeUnaFuncionEra(nombreVariable,nombreFuncion)
            idClasePadre = self.dirProcs[clase,0][0]
            return self.dirProcs[nombreFuncion,idClasePadre][4]

    def crearCuadruploGosub(self,nombreVariable,nombreFuncion):
        cuadruplo = self.obtenerCuadruploInicioFuncion(nombreVariable,nombreFuncion)
        self.quadruplos.append(['gosub',None,None,cuadruplo])


    def printTablaVariables(self):
        cuantos = 0
        print("###################TablaVars###################")
        for key,values in self.tablaVariables.items():
            print(cuantos, " ", key, values)
            cuantos = cuantos + 1
        print("")

    def printDirProcs(self):
        cuantos = 0
        print("###################DirProcs###################")
        for key,values in self.dirProcs.items():
            print(cuantos, " ", key, values)
            cuantos = cuantos + 1
        print("")

    def printCuadruplos(self):
        print("###################Cuadruplos###################")
        cuantos = 0
        while cuantos < len(self.quadruplos):
            print(str(cuantos), " " , self.quadruplos[cuantos])
            cuantos = cuantos + 1

        print("")
        print(self.pilaO)
        print("")
        print(self.pTipos)
        print("")
        print(self.pOper)
        print("###################Fin###################")


    def crearCuadruploAsignacionRetorno(self,elemento):
        self.quadruplos.append(['asignacionRetorno',None,None,elemento])


    #Regresa la direccion especifica de una variable
    def obtenerDireccionVariable(self,variable):
        for key,value in self.tablaVariables.items():
            if key[0] == variable and key[1] == self.scopeProcs:
                return value[2]
        for key,value in self.tablaVariables.items():
            if key[0] == variable and key[1] == 0:
                return value[2]

        
        print("Error en la linea " + str(self.getCurrentToken().line) + " no existe la variable")
        sys.exit()
        return
    
    #Regresa la direccion actual del tipo requerido
    def obtenerDireccionActualTipo(self,globalTof,tipo):
        if globalTof:
            if tipo == "entero":
                return self.memGlobalEntero + 1
            elif tipo == "decimal":
                return self.memGlobalDecimal + 1
            elif tipo == "texto":
                return self.memGlobalTexto + 1
            else:
                return None
        else:
            if tipo == "entero":
                return self.memLocalEntero + 1
            elif tipo == "decimal":
                return self.memLocalDecimal + 1
            elif tipo == "texto":
                return self.memLocalTexto + 1
            else:
                return None


    class ProgramaContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.ProgramaContext, self).__init__(parent, invokingState)
            self.parser = parser

        def p1(self):
            return self.getTypedRuleContext(coffParser.P1Context,0)


        def p2(self):
            return self.getTypedRuleContext(coffParser.P2Context,0)


        def p3(self):
            return self.getTypedRuleContext(coffParser.P3Context,0)


        def principal(self):
            return self.getTypedRuleContext(coffParser.PrincipalContext,0)


        def getRuleIndex(self):
            return coffParser.RULE_programa

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterPrograma(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitPrograma(self)




    def programa(self):

        localctx = coffParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.crearCuadruploMain()
            self.p1()
            self.idFuncionActual = None
            self.p2()
            self.state = 164
            self.p3()
            self.state = 165

            self.completarCuadruploVarsGlobales()

            self.principal()
            self.terminacionProc = 'end'
            self.dirProcs["inicio",0][3] = [self.memLocalEntero - 8999,self.memLocalDecimal - 14999,self.memLocalTexto - 20999]
            self.crearCuadruploTerminarProc()
            #self.printTablaVariables()
            #self.printDirProcs()
            self.printCuadruplos()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class P1Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.P1Context, self).__init__(parent, invokingState)
            self.parser = parser

        def clases(self):
            return self.getTypedRuleContext(coffParser.ClasesContext,0)


        def p1(self):
            return self.getTypedRuleContext(coffParser.P1Context,0)


        def getRuleIndex(self):
            return coffParser.RULE_p1

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterP1(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitP1(self)




    def p1(self):

        localctx = coffParser.P1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_p1)
        try:
            self.state = 171
            token = self._input.LA(1)
            if token in [coffParser.CLASE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.clases()
                self.state = 168
                self.p1()

            elif token in [coffParser.ENTERO, coffParser.DECIMAL, coffParser.TEXTO, coffParser.FUNCION, coffParser.PRINCIPAL, coffParser.ID]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class P2Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.P2Context, self).__init__(parent, invokingState)
            self.parser = parser

        def variables(self):
            return self.getTypedRuleContext(coffParser.VariablesContext,0)


        def p2(self):
            return self.getTypedRuleContext(coffParser.P2Context,0)


        def getRuleIndex(self):
            return coffParser.RULE_p2

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterP2(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitP2(self)




    def p2(self):

        localctx = coffParser.P2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_p2)
        try:
            self.state = 177
            token = self._input.LA(1)
            if token in [coffParser.ENTERO, coffParser.DECIMAL, coffParser.TEXTO, coffParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 173
                #####################################
                self.globalTof = 1
                self.completarCuadruploMain()
                self.variables()
                self.crearCuadruploVarsGlobales()
                self.globalTof = 0
                #####################################
                self.state = 174
                self.p2()

            elif token in [coffParser.FUNCION, coffParser.PRINCIPAL]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class P3Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.P3Context, self).__init__(parent, invokingState)
            self.parser = parser

        def funcion(self):
            return self.getTypedRuleContext(coffParser.FuncionContext,0)


        def p3(self):
            return self.getTypedRuleContext(coffParser.P3Context,0)


        def getRuleIndex(self):
            return coffParser.RULE_p3

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterP3(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitP3(self)




    def p3(self):

        localctx = coffParser.P3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_p3)
        try:
            self.state = 183
            token = self._input.LA(1)

            if token in [coffParser.FUNCION]:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                ##########################
                self.metodoTof = 0
                self.claseIDRef = None
                ##########################
                self.funcion()
                self.state = 180
                self.p3()

            elif token in [coffParser.PRINCIPAL]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PrincipalContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.PrincipalContext, self).__init__(parent, invokingState)
            self.parser = parser

        def PRINCIPAL(self):
            return self.getToken(coffParser.PRINCIPAL, 0)

        def pr1(self):
            return self.getTypedRuleContext(coffParser.Pr1Context,0)


        def ID(self):
            return self.getToken(coffParser.ID, 0)

        def parametros(self):
            return self.getTypedRuleContext(coffParser.ParametrosContext,0)


        def BIZQ(self):
            return self.getToken(coffParser.BIZQ, 0)

        def pr2(self):
            return self.getTypedRuleContext(coffParser.Pr2Context,0)


        def BDER(self):
            return self.getToken(coffParser.BDER, 0)

        def getRuleIndex(self):
            return coffParser.RULE_principal

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterPrincipal(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitPrincipal(self)




    def principal(self):

        localctx = coffParser.PrincipalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_principal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.match(coffParser.PRINCIPAL)
            self.state = 186
            self.pr1()
            self.state = 187
            ########################################
            self.resetearDireccionesLocales()
            self.idVariableActual = str(self.getCurrentToken().text)
            if (self.idVariableActual, 0) in self.dirProcs or (self.idVariableActual, True) in self.dirProcs:
                print("Error, ya habia una funcion declarada con el nombre: "+self.idVariableActual)
                sys.exit()
                return
            
            if self.idVariableActual != "inicio":
                print("Error, la funcion principal debe de nombrarse inicio")
                sys.exit()
                return


            self.scopeProcs = self.scopeProcs + 1
            self.dirProcs[self.idVariableActual,0] = [self.scopeProcs,self.tipoVariableActual,[]]




            ########################################
            self.match(coffParser.ID)
            self.state = 188
            self.listaParametros = []
            self.parametros()
            self.state = 189
            self.match(coffParser.BIZQ)
            self.state = 190
            self.pr2()
            self.state = 191
            self.match(coffParser.BDER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Pr1Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.Pr1Context, self).__init__(parent, invokingState)
            self.parser = parser

        def pr11(self):
            return self.getTypedRuleContext(coffParser.Pr11Context,0)


        def pr12(self):
            return self.getTypedRuleContext(coffParser.Pr12Context,0)


        def getRuleIndex(self):
            return coffParser.RULE_pr1

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterPr1(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitPr1(self)




    def pr1(self):

        localctx = coffParser.Pr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_pr1)
        try:
            self.state = 195
            token = self._input.LA(1)
            if token in [coffParser.ENTERO, coffParser.DECIMAL, coffParser.TEXTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.pr11()

            elif token in [coffParser.VACIO]:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
                self.pr12()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Pr11Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.Pr11Context, self).__init__(parent, invokingState)
            self.parser = parser

        def tiposimple(self):
            return self.getTypedRuleContext(coffParser.TiposimpleContext,0)


        def getRuleIndex(self):
            return coffParser.RULE_pr11

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterPr11(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitPr11(self)




    def pr11(self):

        localctx = coffParser.Pr11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_pr11)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.tiposimple()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Pr12Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.Pr12Context, self).__init__(parent, invokingState)
            self.parser = parser

        def VACIO(self):
            return self.getToken(coffParser.VACIO, 0)

        def getRuleIndex(self):
            return coffParser.RULE_pr12

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterPr12(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitPr12(self)




    def pr12(self):

        localctx = coffParser.Pr12Context(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_pr12)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            ########################################
            self.tipoVariableActual = str(self.getCurrentToken().text)
            #########################################
            self.match(coffParser.VACIO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Pr2Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.Pr2Context, self).__init__(parent, invokingState)
            self.parser = parser

        def pr23(self):
            return self.getTypedRuleContext(coffParser.Pr23Context,0)


        def pr21(self):
            return self.getTypedRuleContext(coffParser.Pr21Context,0)


        def pr22(self):
            return self.getTypedRuleContext(coffParser.Pr22Context,0)


        def getRuleIndex(self):
            return coffParser.RULE_pr2

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterPr2(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitPr2(self)




    def pr2(self):

        localctx = coffParser.Pr2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_pr2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.dirProcs["inicio",0].append([])
            self.dirProcs["inicio",0].append(len(self.quadruplos))
            self.pr23()
            self.dirProcs["inicio",0][3] = self.getNumberOfEDT(["inicio",0])
            
            self.state = 202
            self.pr21()
            self.state = 203
            self.pr22()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Pr23Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.Pr23Context, self).__init__(parent, invokingState)
            self.parser = parser

        def variables(self):
            return self.getTypedRuleContext(coffParser.VariablesContext,0)


        def pr23(self):
            return self.getTypedRuleContext(coffParser.Pr23Context,0)


        def getRuleIndex(self):
            return coffParser.RULE_pr23

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterPr23(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitPr23(self)




    def pr23(self):

        localctx = coffParser.Pr23Context(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_pr23)
        try:
            self.state = 209
            token = self._input.LA(1)
            if token in [coffParser.ENTERO, coffParser.DECIMAL, coffParser.TEXTO, coffParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 205
                self.variables()
                self.state = 206
                self.pr23()

            elif token in [coffParser.IMPRIMIR, coffParser.LEER, coffParser.MIENTRAS, coffParser.RETORNA, coffParser.SI, coffParser.EJEC, coffParser.ASIGNA, coffParser.BDER]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Pr21Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.Pr21Context, self).__init__(parent, invokingState)
            self.parser = parser

        def estatuto(self):
            return self.getTypedRuleContext(coffParser.EstatutoContext,0)


        def pr21(self):
            return self.getTypedRuleContext(coffParser.Pr21Context,0)


        def getRuleIndex(self):
            return coffParser.RULE_pr21

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterPr21(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitPr21(self)




    def pr21(self):

        localctx = coffParser.Pr21Context(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_pr21)
        try:
            self.state = 215
            token = self._input.LA(1)
            if token in [coffParser.IMPRIMIR, coffParser.LEER, coffParser.MIENTRAS, coffParser.SI, coffParser.EJEC, coffParser.ASIGNA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.estatuto()
                self.state = 212
                self.pr21()

            elif token in [coffParser.RETORNA, coffParser.BDER]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Pr22Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.Pr22Context, self).__init__(parent, invokingState)
            self.parser = parser

        def RETORNA(self):
            return self.getToken(coffParser.RETORNA, 0)

        def expresion(self):
            return self.getTypedRuleContext(coffParser.ExpresionContext,0)


        def PUNTOYCOMA(self):
            return self.getToken(coffParser.PUNTOYCOMA, 0)

        def getRuleIndex(self):
            return coffParser.RULE_pr22

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterPr22(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitPr22(self)




    def pr22(self):

        localctx = coffParser.Pr22Context(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_pr22)
        try:
            self.state = 222
            token = self._input.LA(1)
            if token in [coffParser.RETORNA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 217
                self.match(coffParser.RETORNA)
                self.state = 218
                self.expresion()
                self.state = 219
                self.match(coffParser.PUNTOYCOMA)

            elif token in [coffParser.BDER]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TipoContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.TipoContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ENTERO(self):
            return self.getToken(coffParser.ENTERO, 0)

        def DECIMAL(self):
            return self.getToken(coffParser.DECIMAL, 0)

        def TEXTO(self):
            return self.getToken(coffParser.TEXTO, 0)

        def ID(self):
            return self.getToken(coffParser.ID, 0)

        def getRuleIndex(self):
            return coffParser.RULE_tipo

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterTipo(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitTipo(self)




    def tipo(self):

        localctx = coffParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            ############################################
            self.tipoVariableActual = str(self.getCurrentToken().text)
            if self.esTipoFuncionOMetodo == 1:
                self.tipoActualFuncionOMetodo = self.tipoVariableActual
            self.esTipoFuncionOMetodo = 0
            if not((self.tipoVariableActual, False) in self.dirProcs) and not(self.tipoVariableActual == "entero" or self.tipoVariableActual == "decimal" or self.tipoVariableActual == "texto"):
                print("Error, en la linea " + str(self.getCurrentToken().line) +", el tipo "+self.tipoVariableActual+" no existe")
                sys.exit()
                return


            ############################################
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << coffParser.ENTERO) | (1 << coffParser.DECIMAL) | (1 << coffParser.TEXTO) | (1 << coffParser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VariablesContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.VariablesContext, self).__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(coffParser.TipoContext,0)


        def v1(self):
            return self.getTypedRuleContext(coffParser.V1Context,0)


        def PUNTOYCOMA(self):
            return self.getToken(coffParser.PUNTOYCOMA, 0)

        def getRuleIndex(self):
            return coffParser.RULE_variables

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterVariables(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitVariables(self)




    def variables(self):

        localctx = coffParser.VariablesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_variables)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.tipo()
            self.state = 227
            self.v1()
            self.state = 228
            self.match(coffParser.PUNTOYCOMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class V1Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.V1Context, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(coffParser.ID, 0)

        def v2(self):
            return self.getTypedRuleContext(coffParser.V2Context,0)


        def getRuleIndex(self):
            return coffParser.RULE_v1

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterV1(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitV1(self)

    def v1(self):

        localctx = coffParser.V1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_v1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            ########################################################
            self.idVariableActual = str(self.getCurrentToken().text)
            if self.atributosTof:
                self.atributosClase.append([self.idVariableActual,self.scopeProcs])

    
            if self.globalTof:
                if (self.idVariableActual, 0) in self.tablaVariables:
                    print("Error, la variable "+ self.idVariableActual+" ya habia sido declarada")
                    sys.exit()
                    return
                else:
                    self.tablaVariables[self.idVariableActual,0] = [self.tipoVariableActual,1,self.obtenerDireccionActualTipo(1,self.tipoVariableActual)]
            else:
                if (self.idVariableActual, self.scopeProcs) in self.tablaVariables:
                    print("Error, la variable "+ self.idVariableActual+" ya habia sido declarada")
                    sys.exit()
                    return
                else:
                    self.tablaVariables[self.idVariableActual,self.scopeProcs] = [self.tipoVariableActual,1,self.obtenerDireccionActualTipo(0,self.tipoVariableActual)]
            

            self.insertarVariableEnMemoria(self.idVariableActual)
            self.insertarValorTipo(self.obtenerDireccionVariable(self.idVariableActual),self.tipoVariableActual)

           
            ########################################################
            self.match(coffParser.ID)
            self.state = 231
            self.v2()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class V2Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.V2Context, self).__init__(parent, invokingState)
            self.parser = parser

        def CIZQ(self):
            return self.getToken(coffParser.CIZQ, 0)

        def CTEENT(self):
            return self.getToken(coffParser.CTEENT, 0)

        def CDER(self):
            return self.getToken(coffParser.CDER, 0)

        def v4(self):
            return self.getTypedRuleContext(coffParser.V4Context,0)


        def IGUAL(self):
            return self.getToken(coffParser.IGUAL, 0)

        def valordeclaracion(self):
            return self.getTypedRuleContext(coffParser.ValordeclaracionContext,0)


        def v6(self):
            return self.getTypedRuleContext(coffParser.V6Context,0)


        def v3(self):
            return self.getTypedRuleContext(coffParser.V3Context,0)


        def getRuleIndex(self):
            return coffParser.RULE_v2

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterV2(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitV2(self)




    def v2(self):

        localctx = coffParser.V2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_v2)
        try:
            self.state = 243
            token = self._input.LA(1)
            if token in [coffParser.CIZQ]:
                self.enterOuterAlt(localctx, 1)
                self.state = 233
                self.match(coffParser.CIZQ)
                self.state = 234
                self.match(coffParser.CTEENT)
                self.state = 235
                self.match(coffParser.CDER)
                self.state = 236
                self.v4()

            elif token in [coffParser.IGUAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 237
                self.insertarOperador("=")
                self.match(coffParser.IGUAL)
                self.state = 238
                self.valordeclaracion()
                self.state = 239

                
                if self.tipoDeclaracion == 'entero':
                    self.insertarValorTipo([int(self.valorDeclaracion)], self.tipoDeclaracion)
                elif self.tipoDeclaracion == 'decimal':
                    self.insertarValorTipo([float(self.valorDeclaracion)], self.tipoDeclaracion)
                elif self.tipoDeclaracion == 'texto':
                    self.insertarValorTipo([self.valorDeclaracion.replace('"',"")], self.tipoDeclaracion)
                
                self.tipoDeclaracion = None


                self.crearCuadruploExpAsig(4,"asignacion")
                self.v6()

            elif token in [coffParser.COMA]:
                self.enterOuterAlt(localctx, 3)
                self.state = 241
                self.v3()

            elif token in [coffParser.PUNTOYCOMA]:
                self.enterOuterAlt(localctx, 4)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class V3Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.V3Context, self).__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(coffParser.COMA, 0)

        def v1(self):
            return self.getTypedRuleContext(coffParser.V1Context,0)


        def getRuleIndex(self):
            return coffParser.RULE_v3

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterV3(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitV3(self)




    def v3(self):

        localctx = coffParser.V3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_v3)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(coffParser.COMA)
            self.state = 246
            self.v1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class V4Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.V4Context, self).__init__(parent, invokingState)
            self.parser = parser

        def v6(self):
            return self.getTypedRuleContext(coffParser.V6Context,0)


        def IGUAL(self):
            return self.getToken(coffParser.IGUAL, 0)

        def CIZQ(self):
            return self.getToken(coffParser.CIZQ, 0)

        def valordeclaracion(self):
            return self.getTypedRuleContext(coffParser.ValordeclaracionContext,0)


        def v5(self):
            return self.getTypedRuleContext(coffParser.V5Context,0)


        def CDER(self):
            return self.getToken(coffParser.CDER, 0)

        def getRuleIndex(self):
            return coffParser.RULE_v4

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterV4(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitV4(self)




    def v4(self):

        localctx = coffParser.V4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_v4)
        try:
            self.state = 256
            token = self._input.LA(1)
            if token in [coffParser.COMA, coffParser.PUNTOYCOMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 248
                self.v6()

            elif token in [coffParser.IGUAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 249
                self.match(coffParser.IGUAL)
                self.state = 250
                self.match(coffParser.CIZQ)
                self.state = 251
                self.valordeclaracion()
                self.state = 252
                self.v5()
                self.state = 253
                self.match(coffParser.CDER)
                self.state = 254
                self.v6()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class V5Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.V5Context, self).__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(coffParser.COMA, 0)

        def valordeclaracion(self):
            return self.getTypedRuleContext(coffParser.ValordeclaracionContext,0)


        def v5(self):
            return self.getTypedRuleContext(coffParser.V5Context,0)


        def getRuleIndex(self):
            return coffParser.RULE_v5

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterV5(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitV5(self)




    def v5(self):

        localctx = coffParser.V5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_v5)
        try:
            self.state = 263
            token = self._input.LA(1)
            if token in [coffParser.COMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 258
                self.match(coffParser.COMA)
                self.state = 259
                self.valordeclaracion()
                self.state = 260
                self.v5()

            elif token in [coffParser.CDER]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class V6Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.V6Context, self).__init__(parent, invokingState)
            self.parser = parser

        def v3(self):
            return self.getTypedRuleContext(coffParser.V3Context,0)


        def getRuleIndex(self):
            return coffParser.RULE_v6

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterV6(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitV6(self)




    def v6(self):

        localctx = coffParser.V6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_v6)
        try:
            self.state = 267
            token = self._input.LA(1)
            if token in [coffParser.COMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 265
                self.v3()

            elif token in [coffParser.PUNTOYCOMA]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ValordeclaracionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.ValordeclaracionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def CTEENT(self):
            return self.getToken(coffParser.CTEENT, 0)

        def CTEDEC(self):
            return self.getToken(coffParser.CTEDEC, 0)

        def CTETEXTO(self):
            return self.getToken(coffParser.CTETEXTO, 0)

        def getRuleIndex(self):
            return coffParser.RULE_valordeclaracion

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterValordeclaracion(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitValordeclaracion(self)




    def valordeclaracion(self):

        localctx = coffParser.ValordeclaracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_valordeclaracion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << coffParser.CTEENT) | (1 << coffParser.CTEDEC) | (1 << coffParser.CTETEXTO))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                
                constante = self.getCurrentToken().text


                if _la in [coffParser.CTEENT]:
                    self.valorDeclaracion = constante
                    self.tipoDeclaracion = 'entero'

                if _la in [coffParser.CTEDEC]:
                    self.valorDeclaracion = constante
                    self.tipoDeclaracion = 'decimal'
                
                if _la in [coffParser.CTETEXTO]:
                    self.valorDeclaracion = constante
                    self.tipoDeclaracion = 'texto'

                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ValorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.ValorContext, self).__init__(parent, invokingState)
            self.parser = parser

        def valordeclaracion(self):
            return self.getTypedRuleContext(coffParser.ValordeclaracionContext,0)


        def ID(self):
            return self.getToken(coffParser.ID, 0)

        def va1(self):
            return self.getTypedRuleContext(coffParser.Va1Context,0)


        def getRuleIndex(self):
            return coffParser.RULE_valor

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterValor(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitValor(self)


    valorMetodoOFuncion = [] #Variable que revisa si fue un metodo o una funcion dentro de valor
    valorEntraaMetodoOFuncion = [] #Variable que revisa si es una variable simple o una funcion o metodo dentro de valor
    valorIdClaseActual = [] #Variable que guarda el id del objeto para luego revisar su metodo dentro de valor
    valorIdFuncionMetodoActual = [] #Variable que guarda el nombre de la funcion o metodo para revisar dentro de valor

    def valor(self):

        localctx = coffParser.ValorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_valor)
        try:
            self.state = 274
            token = self._input.LA(1)

            if token in [coffParser.CTEENT, coffParser.CTEDEC, coffParser.CTETEXTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 271
                self.valordeclaracion()

                ###############################################
                #Inserto el valor constante y su tipo a la pila de operadores y de tipos

                if self.tipoDeclaracion == 'entero':
                    self.insertarValorTipo([int(self.valorDeclaracion)], self.tipoDeclaracion)
                elif self.tipoDeclaracion == 'decimal':
                    self.insertarValorTipo([float(self.valorDeclaracion)], self.tipoDeclaracion)
                elif self.tipoDeclaracion == 'texto':
                    self.insertarValorTipo([self.valorDeclaracion.replace('"',"")], self.tipoDeclaracion)
                self.tipoDeclaracion = None
                ###############################################

            elif token in [coffParser.ID]:

                self.enterOuterAlt(localctx, 2)
                self.state = 272

                ###############################################
                #Inicializo pila de contador de parametros
                self.contadorParametros.append(0)
                #Para saber si es un metodo o una funcion
                self.valorMetodoOFuncion.append(0)
                #Para saber si es un metodo, funcion o si es una variable simple
                self.valorEntraaMetodoOFuncion.append(0)
                #Almacena el objeto del que se llama su metodo
                self.valorIdClaseActual.append(str(self.getCurrentToken().text))
                #Almacena el nombre de la funcion o del metodo
                self.valorIdFuncionMetodoActual.append(str(self.getCurrentToken().text))

                self.ejecToken = str(self.getCurrentToken().text) 

                #Si inicia la expresion con un negativo se multiplica por -1
                if self.tofFactor:
                    self.insertarValorTipo(-1,'entero')
                ################################################


                self.match(coffParser.ID)
                self.state = 273
                self.insertarOperador("(")
                self.va1()

                self.pOper.pop()


                ###############################################
                #Checo si fue una funcion o metodo o si fue una variable simple
                if self.valorEntraaMetodoOFuncion[len(self.valorEntraaMetodoOFuncion)-1] == 0:
                    #Buscar dentro del mismo scope
                    if (self.ejecToken, self.scopeProcs) in self.tablaVariables:
                        self.insertarValorTipo(self.obtenerDireccionVariable(self.ejecToken),self.tablaVariables[self.ejecToken,self.scopeProcs][0])
                    #si no se encuentra buscar en la def de la clase
                    elif (self.ejecToken, self.claseScopeRef) in self.tablaVariables:
                        self.insertarValorTipo(self.obtenerDireccionVariable(self.ejecToken),self.tablaVariables[self.ejecToken, self.claseScopeRef][0])
                    #buscar en vars globales
                    elif (self.ejecToken, 0) in self.tablaVariables:
                        self.insertarValorTipo(self.obtenerDireccionVariable(self.ejecToken),self.tablaVariables[self.ejecToken,0][0]) 
                        
                elif self.esAtributo == 0:

                    #si fue una funcion o metodo genero el cuadruplo de gosub
                    #Saco el tipo de la funcion o metodo
                    if self.valorMetodoOFuncion[len(self.valorMetodoOFuncion)-1]:
                        self.crearCuadruploEra(self.valorIdClaseActual[len(self.valorIdClaseActual)-1],self.valorIdFuncionMetodoActual[len(self.valorIdFuncionMetodoActual)-1])
                        self.crearCuadruploParam()
                        
                        tipoMetFunc = self.obtenerTipoDeUnMetodoEra(self.valorIdClaseActual[len(self.valorIdClaseActual)-1],self.valorIdFuncionMetodoActual[len(self.valorIdFuncionMetodoActual)-1])
                    else:        
                        self.crearCuadruploEra(None,self.valorIdFuncionMetodoActual[len(self.valorIdFuncionMetodoActual)-1])
                        self.crearCuadruploParam()            
                        tipoMetFunc = self.obtenerTipoDeUnaFuncionEra(self.valorIdFuncionMetodoActual[len(self.valorIdFuncionMetodoActual)-1])

                    if tipoMetFunc == "entero":
                        self.memLocalEntero = self.memLocalEntero + 1
                        auxDireccion = self.memLocalEntero
                    elif tipoMetFunc == "decimal":
                        self.memLocalDecimal = self.memLocalDecimal + 1
                        auxDireccion = self.memLocalDecimal
                    elif tipoMetFunc == "texto":
                        self.memLocalTexto = self.memLocalTexto + 1
                        auxDireccion = self.memLocalTexto

                    #creo el cuadruplo donde se va a tener el retorno
                    self.crearCuadruploAsignacionRetorno(auxDireccion)

                    if self.valorMetodoOFuncion[len(self.valorMetodoOFuncion)-1]:
                        self.crearCuadruploGosub(self.valorIdClaseActual[len(self.valorIdClaseActual)-1],self.valorIdFuncionMetodoActual[len(self.valorIdFuncionMetodoActual)-1])
                    else:
                        self.crearCuadruploGosub(None,self.valorIdFuncionMetodoActual[len(self.valorIdFuncionMetodoActual)-1])

                    #Inserto el tipo y nombre de la funcion a la pila de tipos y operandos para procesar con el cubo semantico despues
                    self.insertarValorTipo(auxDireccion,tipoMetFunc)
                
                #Saco el contador de parametros ya que ya se termino esta expresion
                self.contadorParametros.pop()
                self.valorMetodoOFuncion.pop()
                self.valorEntraaMetodoOFuncion.pop()
                self.valorIdClaseActual.pop()
                self.valorIdFuncionMetodoActual.pop()

                if self.tofFactor:
                    self.tofFactor = 0
                    self.insertarOperador('*')

                self.crearCuadruploExpAsig(0,'expresion')
                ###############################################
                self.esAtributo = 0
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Va1Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.Va1Context, self).__init__(parent, invokingState)
            self.parser = parser

        def va4(self):
            return self.getTypedRuleContext(coffParser.Va4Context,0)


        def PIZQ(self):
            return self.getToken(coffParser.PIZQ, 0)

        def va2(self):
            return self.getTypedRuleContext(coffParser.Va2Context,0)


        def PDER(self):
            return self.getToken(coffParser.PDER, 0)

        def CIZQ(self):
            return self.getToken(coffParser.CIZQ, 0)

        def CTEENT(self):
            return self.getToken(coffParser.CTEENT, 0)

        def CDER(self):
            return self.getToken(coffParser.CDER, 0)

        def getRuleIndex(self):
            return coffParser.RULE_va1

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterVa1(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitVa1(self)




    def va1(self):

        localctx = coffParser.Va1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_va1)
        try:
            self.state = 285
            token = self._input.LA(1)
            if token in [coffParser.PUNTO]:
                #Metodo de una clase o un atributo de una clase
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                self.va4()

            elif token in [coffParser.PIZQ]:
                ###############################################
                #Una funcion
                self.valorMetodoOFuncion[len(self.valorMetodoOFuncion)-1] = 0
                self.valorEntraaMetodoOFuncion[len(self.valorEntraaMetodoOFuncion)-1] = 1
                
                self.funcionOmetodo = 1	
                self.nComasAux2 = 1
                ###############################################

                self.enterOuterAlt(localctx, 2)
                self.state = 277
                self.match(coffParser.PIZQ)
                self.state = 278
                self.va2()
                self.state = 279

                ###############################################
                if self.contadorParametros[len(self.contadorParametros)-1] != self.obtenerCantidadParametrosFuncionOMetodo(None,self.valorIdFuncionMetodoActual[len(self.valorIdFuncionMetodoActual)-1]):
                    print("Error en la linea " + str(self.getCurrentToken().line) + ", cantidad incorrecta de parametros")
                    sys.exit()
                    return
                ###############################################
                
                self.match(coffParser.PDER)

            elif token in [coffParser.CIZQ]:
                #Arreglos simples o arreglos de atributos de clase###########################################################################################IMPLEMENTAR ARREGLO
                self.enterOuterAlt(localctx, 3)
                self.state = 281
                self.match(coffParser.CIZQ)
                self.state = 282
                self.match(coffParser.CTEENT)
                self.state = 283
                self.match(coffParser.CDER)

            elif token in [coffParser.PDER, coffParser.CDER, coffParser.SUMA, coffParser.RESTA, coffParser.DIV, coffParser.MULT, coffParser.IGUALQUE, coffParser.MENQUE, coffParser.MAYQUE, coffParser.MAYIGUALQUE, coffParser.MENIGUALQUE, coffParser.DIF, coffParser.CONDICIONO, coffParser.CONDICIONY, coffParser.COMA, coffParser.PUNTOYCOMA]:
                self.enterOuterAlt(localctx, 4)

                ###############################################
                #se checa si la variable simple existe en la tabla de variables
                self.idVariableActual = self.ejecToken
                self.checkIfVariableExists()
                ###############################################

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Va2Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.Va2Context, self).__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(coffParser.ExpresionContext,0)


        def va3(self):
            return self.getTypedRuleContext(coffParser.Va3Context,0)


        def getRuleIndex(self):
            return coffParser.RULE_va2

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterVa2(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitVa2(self)




    def va2(self):

        localctx = coffParser.Va2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_va2)
        try:
            self.state = 291
            token = self._input.LA(1)
            if token in [coffParser.PIZQ, coffParser.SUMA, coffParser.RESTA, coffParser.ID, coffParser.CTEENT, coffParser.CTEDEC, coffParser.CTETEXTO]:
                self.enterOuterAlt(localctx, 1)

                ######################################
                self.idFuncionActual = self.ejecToken  
                self.checkIfGlobalFunctionOrClassExists(self.ejecToken)
                ######################################
                
                self.state = 287
                self.expresion()

                ######################################
                cParametros = self.obtenerCantidadParametrosFuncionOMetodo(None,self.idFuncionActual)

                if cParametros < self.contadorParametros[len(self.contadorParametros) - 1]+1:
                    print("Error en la linea " + str(self.getCurrentToken().line) + ", cantidad incorrecta de parametros")
                    sys.exit()
                    return


                self.checaTipoExpresionConParametro(None,self.valorIdFuncionMetodoActual[len(self.valorIdFuncionMetodoActual)-1])

                #Obtengo la direccion del parametro actual
                numeroParametroActual = self.contadorParametros[len(self.contadorParametros)-1]-1
                variableParametro = self.dirProcs[self.valorIdFuncionMetodoActual[len(self.valorIdFuncionMetodoActual)-1],0][2][numeroParametroActual]
                dirParametroActual = self.tablaVariables[variableParametro[0],variableParametro[1]][2]

                self.guardarCuadruploParam(dirParametroActual)
                ######################################

                self.state = 288
                self.va3()

            elif token in [coffParser.PDER]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Va3Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.Va3Context, self).__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(coffParser.COMA, 0)

        def expresion(self):
            return self.getTypedRuleContext(coffParser.ExpresionContext,0)


        def va3(self):
            return self.getTypedRuleContext(coffParser.Va3Context,0)


        def getRuleIndex(self):
            return coffParser.RULE_va3

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterVa3(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitVa3(self)




    def va3(self):

        localctx = coffParser.Va3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_va3)
        try:
            self.state = 298
            token = self._input.LA(1)
            if token in [coffParser.COMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 293
                self.nComas = self.nComas + 1
                self.match(coffParser.COMA)
                self.state = 294
                self.expresion()

                ###################################################################
                if self.valorMetodoOFuncion[len(self.valorMetodoOFuncion)-1] == 0:
                    cParametros = self.obtenerCantidadParametrosFuncionOMetodo(None,self.valorIdFuncionMetodoActual[len(self.valorIdFuncionMetodoActual)-1])
                    if cParametros < self.contadorParametros[len(self.contadorParametros) - 1] + 1:
                        print("Error en la linea " + str(self.getCurrentToken().line) + ", cantidad incorrecta de parametros")
                        sys.exit()
                        return
                    self.checaTipoExpresionConParametro(None,self.valorIdFuncionMetodoActual[len(self.valorIdFuncionMetodoActual)-1])

                    #Obtengo la direccion del parametro actual
                    numeroParametroActual = self.contadorParametros[len(self.contadorParametros)-1]-1
                    variableParametro = self.dirProcs[self.valorIdFuncionMetodoActual[len(self.valorIdFuncionMetodoActual)-1],0][2][numeroParametroActual]
                    dirParametroActual = self.tablaVariables[variableParametro[0],variableParametro[1]][2]
                    self.guardarCuadruploParam(dirParametroActual)

                else:
                    cParametros = self.obtenerCantidadParametrosFuncionOMetodo(self.valorIdClaseActual[len(self.valorIdClaseActual)-1],self.valorIdFuncionMetodoActual[len(self.valorIdFuncionMetodoActual)-1])
                    if cParametros < self.contadorParametros[len(self.contadorParametros) - 1] + 1:
                        print("Error en la linea " + str(self.getCurrentToken().line) + ", cantidad incorrecta de parametros")
                        sys.exit()
                        return


                    self.checaTipoExpresionConParametro(self.valorIdClaseActual[len(self.valorIdClaseActual)-1],self.valorIdFuncionMetodoActual[len(self.valorIdFuncionMetodoActual)-1])
                    
                    #Obtengo la direccion del parametro actual
                    numeroParametroActual = self.contadorParametros[len(self.contadorParametros)-1]-1
                    #variableParametro = self.dirProcs[self.valorIdFuncionMetodoActual[len(self.valorIdFuncionMetodoActual)-1],self.valorIdClaseActual[len(self.valorIdClaseActual)-1]][2][numeroParametroActual]
                    claseDeMetodoActual = self.obtenerClaseDeUnaFuncionEra(self.valorIdClaseActual[len(self.valorIdClaseActual)-1],self.valorIdFuncionMetodoActual[len(self.valorIdFuncionMetodoActual)-1])
                    variableParametro = self.dirProcs[self.valorIdFuncionMetodoActual[len(self.valorIdFuncionMetodoActual)-1],self.dirProcs[claseDeMetodoActual,0][0]][2][numeroParametroActual]
                
                    dirParametroActual = self.tablaVariables[variableParametro[0],variableParametro[1]][2]
                    self.guardarCuadruploParam(dirParametroActual)
                ###################################################################

                self.state = 295
                self.va3()

            elif token in [coffParser.PDER]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Va4Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.Va4Context, self).__init__(parent, invokingState)
            self.parser = parser

        def PUNTO(self):
            return self.getToken(coffParser.PUNTO, 0)

        def ID(self):
            return self.getToken(coffParser.ID, 0)

        def va5(self):
            return self.getTypedRuleContext(coffParser.Va5Context,0)


        def getRuleIndex(self):
            return coffParser.RULE_va4

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterVa4(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitVa4(self)




    def va4(self):

        localctx = coffParser.Va4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_va4)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(coffParser.PUNTO)
            self.state = 301
            ######################################
            self.valorMetodoOFuncion[len(self.valorMetodoOFuncion)-1] = 1
            self.valorEntraaMetodoOFuncion[len(self.valorEntraaMetodoOFuncion)-1] = 1
            self.valorIdFuncionMetodoActual[len(self.valorIdFuncionMetodoActual)-1] = str(self.getCurrentToken().text)
            self.funcionOmetodo = 2
            self.tokenActual = str(self.getCurrentToken().text)
            
            ######################################

            self.match(coffParser.ID)
            self.state = 302
            self.va5()

            #####################################

           
          
            #####################################
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Va5Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.Va5Context, self).__init__(parent, invokingState)
            self.parser = parser

        def PIZQ(self):
            return self.getToken(coffParser.PIZQ, 0)

        def va6(self):
            return self.getTypedRuleContext(coffParser.Va6Context,0)


        def PDER(self):
            return self.getToken(coffParser.PDER, 0)

        def getRuleIndex(self):
            return coffParser.RULE_va5

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterVa5(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitVa5(self)




    def va5(self):

        localctx = coffParser.Va5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_va5)
        try:
            self.state = 309
            token = self._input.LA(1)
            if token in [coffParser.PIZQ]:
                
                self.nComasAux2 = 1
                self.enterOuterAlt(localctx, 1)
                self.state = 304
                
                ############################################
                self.idFuncionActual = self.tokenActual
                self.funcionOmetodo = 2
                self.lookForMethodClass()
                ############################################
                
                self.match(coffParser.PIZQ)
                self.state = 305                
                self.va6()
                self.state = 306
                    
                if self.contadorParametros[len(self.contadorParametros)-1] != self.obtenerCantidadParametrosFuncionOMetodo(self.valorIdClaseActual[len(self.valorIdClaseActual)-1],self.valorIdFuncionMetodoActual[len(self.valorIdFuncionMetodoActual)-1]):
                    print("Error en la linea " + str(self.getCurrentToken().line) + ", cantidad incorrecta de parametros")
                    sys.exit()
                    return
                ####cambie esto en la ultima vez

                #self.checaTipoExpresionConParametro(self.valorIdClaseActual[len(self.valorIdClaseActual)-1],self.valorIdFuncionMetodoActual[len(self.valorIdFuncionMetodoActual)-1])
                self.crearCuadruploParam()
                self.match(coffParser.PDER)

            elif token in [coffParser.PDER, coffParser.CDER, coffParser.SUMA, coffParser.RESTA, coffParser.DIV, coffParser.MULT, coffParser.IGUALQUE, coffParser.MENQUE, coffParser.MAYQUE, coffParser.MAYIGUALQUE, coffParser.MENIGUALQUE, coffParser.DIF, coffParser.CONDICIONO, coffParser.CONDICIONY, coffParser.COMA, coffParser.PUNTOYCOMA]:
                self.enterOuterAlt(localctx, 2)
                self.esAtributo = 1
                atributo = self.valorIdFuncionMetodoActual[len(self.valorIdFuncionMetodoActual)-1]

                try:
                    tipoAtributo = self.tablaVariables[atributo,self.dirProcs[self.claseIDRef,0][0] ][0]

                    
                except KeyError:
                    print ("Error, el atributo "+atributo+" no ha sido declarado")
                    sys.exit()
                    return


                self.insertarValorTipo(atributo,tipoAtributo)  
                if (str(self.getCurrentToken().text) == ";" or str(self.getCurrentToken().text) == ","):                 
                    self.idVariableActual = self.tokenActual
                    self.checkIfAttributeBelongs(self.idVariableActual, self.ejecToken)
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Va6Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.Va6Context, self).__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(coffParser.ExpresionContext,0)


        def va3(self):
            return self.getTypedRuleContext(coffParser.Va3Context,0)


        def getRuleIndex(self):
            return coffParser.RULE_va6

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterVa6(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitVa6(self)




    def va6(self):

        localctx = coffParser.Va6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_va6)
        try:
            self.state = 315
            token = self._input.LA(1)
            if token in [coffParser.PIZQ, coffParser.SUMA, coffParser.RESTA, coffParser.ID, coffParser.CTEENT, coffParser.CTEDEC, coffParser.CTETEXTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 311
                self.expresion()
                

                ################nombre variable luego nombre funcion###################
                ######################################


                cParametros = self.obtenerCantidadParametrosFuncionOMetodo(self.valorIdClaseActual[len(self.valorIdClaseActual)-1],self.valorIdFuncionMetodoActual[len(self.valorIdFuncionMetodoActual) - 1])


                if cParametros < self.contadorParametros[len(self.contadorParametros) - 1]+1:
                    print("Error en la linea " + str(self.getCurrentToken().line) + ", cantidad incorrecta de parametros")
                    sys.exit()
                    return

                self.checaTipoExpresionConParametro(self.valorIdClaseActual[len(self.valorIdClaseActual)-1],self.valorIdFuncionMetodoActual[len(self.valorIdFuncionMetodoActual)-1])
                
                #Obtengo la direccion del parametro actual
                numeroParametroActual = self.contadorParametros[len(self.contadorParametros)-1]-1
                claseDeMetodoActual = self.obtenerClaseDeUnaFuncionEra(self.valorIdClaseActual[len(self.valorIdClaseActual)-1],self.valorIdFuncionMetodoActual[len(self.valorIdFuncionMetodoActual)-1])
                variableParametro = self.dirProcs[self.valorIdFuncionMetodoActual[len(self.valorIdFuncionMetodoActual)-1],self.dirProcs[claseDeMetodoActual,0][0]][2][numeroParametroActual]
                dirParametroActual = self.tablaVariables[variableParametro[0],variableParametro[1]][2]
                self.guardarCuadruploParam(dirParametroActual)

                ###################################

                
                self.state = 312
                self.va3()

            elif token in [coffParser.PDER]:
                self.enterOuterAlt(localctx, 2)
                ###################################
                
                ###################################

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TiposimpleContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.TiposimpleContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ENTERO(self):
            return self.getToken(coffParser.ENTERO, 0)

        def DECIMAL(self):
            return self.getToken(coffParser.DECIMAL, 0)

        def TEXTO(self):
            return self.getToken(coffParser.TEXTO, 0)

        def getRuleIndex(self):
            return coffParser.RULE_tiposimple

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterTiposimple(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitTiposimple(self)




    def tiposimple(self):

        localctx = coffParser.TiposimpleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_tiposimple)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << coffParser.ENTERO) | (1 << coffParser.DECIMAL) | (1 << coffParser.TEXTO))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                
                ############################################################
                self.tipoVariableActual = str(self.getCurrentToken().text)
                #############################################################

                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParametrosContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.ParametrosContext, self).__init__(parent, invokingState)
            self.parser = parser

        def PIZQ(self):
            return self.getToken(coffParser.PIZQ, 0)

        def pa1(self):
            return self.getTypedRuleContext(coffParser.Pa1Context,0)


        def PDER(self):
            return self.getToken(coffParser.PDER, 0)

        def getRuleIndex(self):
            return coffParser.RULE_parametros

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterParametros(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitParametros(self)




    def parametros(self):

        localctx = coffParser.ParametrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_parametros)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(coffParser.PIZQ)
            self.state = 320
            self.pa1()
            self.state = 321
            self.match(coffParser.PDER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Pa1Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.Pa1Context, self).__init__(parent, invokingState)
            self.parser = parser

        def pa11(self):
            return self.getTypedRuleContext(coffParser.Pa11Context,0)


        def getRuleIndex(self):
            return coffParser.RULE_pa1

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterPa1(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitPa1(self)




    def pa1(self):

        localctx = coffParser.Pa1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_pa1)
        try:
            self.state = 325
            token = self._input.LA(1)
            if token in [coffParser.ENTERO, coffParser.DECIMAL, coffParser.TEXTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 323
                self.pa11()

            elif token in [coffParser.PDER]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Pa11Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.Pa11Context, self).__init__(parent, invokingState)
            self.parser = parser

        def tiposimple(self):
            return self.getTypedRuleContext(coffParser.TiposimpleContext,0)


        def pa2(self):
            return self.getTypedRuleContext(coffParser.Pa2Context,0)


        def ID(self):
            return self.getToken(coffParser.ID, 0)

        def pa3(self):
            return self.getTypedRuleContext(coffParser.Pa3Context,0)


        def getRuleIndex(self):
            return coffParser.RULE_pa11

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterPa11(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitPa11(self)




    def pa11(self):

        localctx = coffParser.Pa11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_pa11)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self.tiposimple()
            self.state = 328
            self.pa2()
            self.state = 329
            ##########################################################
            self.idVariableActual = str(self.getCurrentToken().text)
            self.listaParametros.append([self.idVariableActual,self.scopeProcs])

            
            self.dirProcs[self.parametrosAux[0], self.parametrosAux[1]][2] = self.listaParametros
            


            if self.globalTof:
                if (self.idVariableActual, 0) in self.tablaVariables:
                    print("Error, la variable "+ self.idVariableActual+" ya habia sido declarada")
                    sys.exit()
                    return
                else:
                    self.tablaVariables[self.idVariableActual,0] = [self.tipoVariableActual,1,self.obtenerDireccionActualTipo(1,self.tipoVariableActual)]
            else:
                if (self.idVariableActual, self.scopeProcs) in self.tablaVariables:
                    print("Error, la variable "+ self.idVariableActual+" ya habia sido declarada")
                    sys.exit()
                    return
                else:
                    self.tablaVariables[self.idVariableActual,self.scopeProcs] = [self.tipoVariableActual,1,self.obtenerDireccionActualTipo(0,self.tipoVariableActual)]


            self.insertarVariableEnMemoria(self.idVariableActual)
            ########################################################
            self.match(coffParser.ID)
            self.state = 330
            self.pa3()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Pa2Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.Pa2Context, self).__init__(parent, invokingState)
            self.parser = parser

        def AMP(self):
            return self.getToken(coffParser.AMP, 0)

        def getRuleIndex(self):
            return coffParser.RULE_pa2

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterPa2(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitPa2(self)




    def pa2(self):

        localctx = coffParser.Pa2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_pa2)
        try:
            self.state = 334
            token = self._input.LA(1)
            if token in [coffParser.AMP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 332
                self.match(coffParser.AMP)

            elif token in [coffParser.ID]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Pa3Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.Pa3Context, self).__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(coffParser.COMA, 0)

        def pa1(self):
            return self.getTypedRuleContext(coffParser.Pa1Context,0)


        def getRuleIndex(self):
            return coffParser.RULE_pa3

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterPa3(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitPa3(self)




    def pa3(self):

        localctx = coffParser.Pa3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_pa3)
        try:
            self.state = 339
            token = self._input.LA(1)
            if token in [coffParser.COMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 336
                self.match(coffParser.COMA)
                self.state = 337
                self.pa1()

            elif token in [coffParser.PDER]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LlamarfunmetContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.LlamarfunmetContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(coffParser.ID, 0)

        def ll1(self):
            return self.getTypedRuleContext(coffParser.Ll1Context,0)


        def PIZQ(self):
            return self.getToken(coffParser.PIZQ, 0)

        def ll2(self):
            return self.getTypedRuleContext(coffParser.Ll2Context,0)


        def PDER(self):
            return self.getToken(coffParser.PDER, 0)

        def PUNTOYCOMA(self):
            return self.getToken(coffParser.PUNTOYCOMA, 0)

        def getRuleIndex(self):
            return coffParser.RULE_llamarfunmet

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterLlamarfunmet(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitLlamarfunmet(self)


    llamarfunmetMetodoOFuncion = [] #Variable que revisa si fue un metodo o una funcion dentro de valor
    llamarfunmetIdClaseActual = [] #Variable que guarda el id del objeto para luego revisar su metodo dentro de valor
    llamarfunmetIdFuncionMetodoActual = [] #Variable que guarda el nombre de la funcion o metodo para revisar dentro de valor

    def llamarfunmet(self):

        localctx = coffParser.LlamarfunmetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_llamarfunmet)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341

            #######################################
            self.contadorParametros.append(0)
            self.llamarfunmetMetodoOFuncion.append(0)
            self.llamarfunmetIdClaseActual.append(str(self.getCurrentToken().text))
            self.llamarfunmetIdFuncionMetodoActual.append(str(self.getCurrentToken().text))


            #No lo borro para no romper nada
            self.ejecToken = self.llamarfunmetIdClaseActual[len(self.llamarfunmetIdClaseActual)-1]
            self.idFuncionActual = self.llamarfunmetIdClaseActual[len(self.llamarfunmetIdClaseActual)-1]
            #######################################

            self.match(coffParser.ID)
            self.state = 342
            self.ll1()
            self.state = 343
            self.match(coffParser.PIZQ)
            self.state = 344
            self.ll2()
            self.state = 345

            self.match(coffParser.PDER)

            #######################################
            if self.llamarfunmetMetodoOFuncion[len(self.llamarfunmetMetodoOFuncion)-1]:
                if self.contadorParametros[len(self.contadorParametros)-1] != self.obtenerCantidadParametrosFuncionOMetodo(self.llamarfunmetIdClaseActual[len(self.llamarfunmetIdClaseActual)-1],self.llamarfunmetIdFuncionMetodoActual[len(self.llamarfunmetIdFuncionMetodoActual)-1]):
                    print("Error en la linea " + str(self.getCurrentToken().line) + ", cantidad de parametros no coincide con el metodo")
                    sys.exit()
                    return
                self.crearCuadruploEra(self.llamarfunmetIdClaseActual[len(self.llamarfunmetIdClaseActual)-1],self.llamarfunmetIdFuncionMetodoActual[len(self.llamarfunmetIdFuncionMetodoActual)-1])
                self.crearCuadruploParam()
                self.crearCuadruploGosub(self.llamarfunmetIdClaseActual[len(self.llamarfunmetIdClaseActual)-1],self.llamarfunmetIdFuncionMetodoActual[len(self.llamarfunmetIdFuncionMetodoActual)-1])

            else:
                if self.contadorParametros[len(self.contadorParametros)-1] != self.obtenerCantidadParametrosFuncionOMetodo(None,self.llamarfunmetIdFuncionMetodoActual[len(self.llamarfunmetIdFuncionMetodoActual)-1]): 
                    print("Error en la linea " + str(self.getCurrentToken().line) + ", cantidad de parametros no coincide con la funcion")
                    sys.exit()
                    return
                self.crearCuadruploEra(None,self.llamarfunmetIdFuncionMetodoActual[len(self.llamarfunmetIdFuncionMetodoActual)-1])
                self.crearCuadruploParam()
                self.crearCuadruploGosub(None,self.llamarfunmetIdFuncionMetodoActual[len(self.llamarfunmetIdFuncionMetodoActual)-1])

            self.contadorParametros.pop()
            self.llamarfunmetMetodoOFuncion.pop()
            self.llamarfunmetIdClaseActual.pop()
            self.llamarfunmetIdFuncionMetodoActual.pop()

            #######################################

            self.state = 346
            self.match(coffParser.PUNTOYCOMA)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Ll1Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.Ll1Context, self).__init__(parent, invokingState)
            self.parser = parser

        def PUNTO(self):
            return self.getToken(coffParser.PUNTO, 0)

        def ID(self):
            return self.getToken(coffParser.ID, 0)

        def getRuleIndex(self):
            return coffParser.RULE_ll1

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterLl1(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitLl1(self)




    def ll1(self):

        localctx = coffParser.Ll1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_ll1)
        try:
            self.state = 351
            self.tokenActual = str(self.getCurrentToken().text)
            token = self._input.LA(1)
            if token in [coffParser.PUNTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 348
                self.match(coffParser.PUNTO)
                self.state = 349

                #######################

                self.llamarfunmetMetodoOFuncion[len(self.llamarfunmetMetodoOFuncion)-1] = 1
                self.llamarfunmetIdFuncionMetodoActual[len(self.llamarfunmetMetodoOFuncion)-1] = str(self.getCurrentToken().text)


                self.funcionOmetodo = self.llamarfunmetMetodoOFuncion[len(self.llamarfunmetMetodoOFuncion)-1] + 1
                self.idVariableActual = self.llamarfunmetIdClaseActual[len(self.llamarfunmetIdClaseActual)-1]
                self.checkIfVariableExists()

                self.tokenActual = str(self.getCurrentToken().text)
                self.idFuncionActual = self.llamarfunmetIdFuncionMetodoActual[len(self.llamarfunmetIdFuncionMetodoActual)-1]
                self.lookForMethodClass()
                #######################

                self.match(coffParser.ID)

            elif token in [coffParser.PIZQ]:
                self.enterOuterAlt(localctx, 2)

                #######################
                self.llamarfunmetMetodoOFuncion[len(self.llamarfunmetMetodoOFuncion)-1] = 0
                self.funcionOmetodo = self.llamarfunmetMetodoOFuncion[len(self.llamarfunmetMetodoOFuncion)-1] + 1
                self.checkIfGlobalFunctionOrClassExists(self.llamarfunmetIdFuncionMetodoActual[len(self.llamarfunmetMetodoOFuncion)-1])
                #######################

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Ll2Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.Ll2Context, self).__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(coffParser.ExpresionContext,0)


        def ll3(self):
            return self.getTypedRuleContext(coffParser.Ll3Context,0)


        def getRuleIndex(self):
            return coffParser.RULE_ll2

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterLl2(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitLl2(self)

    def idDeMetodo2(self,nombreMetodo):
        for key, values in self.dirProcs.items():
            if key[0] == nombreMetodo and key[1] != 0:
                return key[1]



    def ll2(self):

        localctx = coffParser.Ll2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_ll2)
        try:
            self.state = 357
            token = self._input.LA(1)
            if token in [coffParser.PIZQ, coffParser.SUMA, coffParser.RESTA, coffParser.ID, coffParser.CTEENT, coffParser.CTEDEC, coffParser.CTETEXTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 353
                self.expresion()
                self.state = 354
                
                ##########################################
                #Metodo
                if self.llamarfunmetMetodoOFuncion[len(self.llamarfunmetMetodoOFuncion)-1]:

                    cParametros = self.obtenerCantidadParametrosFuncionOMetodo(self.llamarfunmetIdClaseActual[len(self.llamarfunmetIdClaseActual)-1],self.llamarfunmetIdFuncionMetodoActual[len(self.llamarfunmetIdFuncionMetodoActual)-1])
                    if cParametros < self.contadorParametros[len(self.contadorParametros) - 1]+1:
                        print("Error en la linea " + str(self.getCurrentToken().line) + ", cantidad incorrecta de parametros")
                        sys.exit()
                        return

                    self.checaTipoExpresionConParametro(self.llamarfunmetIdClaseActual[len(self.llamarfunmetIdClaseActual)-1],self.llamarfunmetIdFuncionMetodoActual[len(self.llamarfunmetIdFuncionMetodoActual)-1])
                    
                    #Obtengo la direccion del parametro actual
                    numeroParametroActual = self.contadorParametros[len(self.contadorParametros)-1]-1

                    par1 = self.llamarfunmetIdFuncionMetodoActual[len(self.llamarfunmetIdFuncionMetodoActual)-1]
                    par2 = self.idDeMetodo2(self.llamarfunmetIdFuncionMetodoActual[len(self.llamarfunmetIdFuncionMetodoActual)-1])
                    variableParametro = self.dirProcs[par1,par2][2][numeroParametroActual]
                    dirParametroActual = self.tablaVariables[variableParametro[0],variableParametro[1]][2]

                #Funcion
                else:
                    cParametros = self.obtenerCantidadParametrosFuncionOMetodo(None,self.llamarfunmetIdFuncionMetodoActual[len(self.llamarfunmetIdFuncionMetodoActual)-1])
                    if cParametros < self.contadorParametros[len(self.contadorParametros) - 1]+1:
                        print("Error en la linea " + str(self.getCurrentToken().line) + ", cantidad incorrecta de parametros")
                        sys.exit()
                        return

                    self.checaTipoExpresionConParametro(None,self.llamarfunmetIdFuncionMetodoActual[len(self.llamarfunmetIdFuncionMetodoActual)-1])
                    
                    #Obtengo la direccion del parametro actual
                    numeroParametroActual = self.contadorParametros[len(self.contadorParametros)-1]-1
                    variableParametro = self.dirProcs[self.llamarfunmetIdFuncionMetodoActual[len(self.llamarfunmetIdFuncionMetodoActual)-1],0][2][numeroParametroActual]
                    dirParametroActual = self.tablaVariables[variableParametro[0],variableParametro[1]][2]

                self.guardarCuadruploParam(dirParametroActual)
                ##########################################

                self.ll3()

            elif token in [coffParser.PDER]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Ll3Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.Ll3Context, self).__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(coffParser.COMA, 0)

        def expresion(self):
            return self.getTypedRuleContext(coffParser.ExpresionContext,0)


        def ll3(self):
            return self.getTypedRuleContext(coffParser.Ll3Context,0)


        def getRuleIndex(self):
            return coffParser.RULE_ll3

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterLl3(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitLl3(self)


    def ll3(self):

        localctx = coffParser.Ll3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_ll3)
        try:
            self.state = 364
            token = self._input.LA(1)
            if token in [coffParser.COMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 359

                self.match(coffParser.COMA)
                self.state = 360
                self.expresion()

                ##########################################
                #Metodo
                if self.llamarfunmetMetodoOFuncion[len(self.llamarfunmetMetodoOFuncion)-1]:
                    cParametros = self.obtenerCantidadParametrosFuncionOMetodo(self.llamarfunmetIdClaseActual[len(self.llamarfunmetIdClaseActual)-1],self.llamarfunmetIdFuncionMetodoActual[len(self.llamarfunmetIdFuncionMetodoActual)-1])
                    if cParametros < self.contadorParametros[len(self.contadorParametros) - 1]+1:
                        print("Error en la linea " + str(self.getCurrentToken().line) + ", cantidad incorrecta de parametros")
                        sys.exit()
                        return

                    self.checaTipoExpresionConParametro(self.llamarfunmetIdClaseActual[len(self.llamarfunmetIdClaseActual)-1],self.llamarfunmetIdFuncionMetodoActual[len(self.llamarfunmetIdFuncionMetodoActual)-1])
                    #Obtengo la direccion del parametro actual
                    numeroParametroActual = self.contadorParametros[len(self.contadorParametros)-1]-1


                    par1 = self.llamarfunmetIdFuncionMetodoActual[len(self.llamarfunmetIdFuncionMetodoActual)-1]
                    par2 = self.idDeMetodo2(self.llamarfunmetIdFuncionMetodoActual[len(self.llamarfunmetIdFuncionMetodoActual)-1])

                    variableParametro = self.dirProcs[par1,par2][2][numeroParametroActual]
                    dirParametroActual = self.tablaVariables[variableParametro[0],variableParametro[1]][2]
                #Funcion
                else:
                    cParametros = self.obtenerCantidadParametrosFuncionOMetodo(None,self.llamarfunmetIdFuncionMetodoActual[len(self.llamarfunmetIdFuncionMetodoActual)-1])
                    if cParametros < self.contadorParametros[len(self.contadorParametros) - 1]+1:
                        print("Error en la linea " + str(self.getCurrentToken().line) + ", cantidad incorrecta de parametros")
                        sys.exit()
                        return

                    self.checaTipoExpresionConParametro(None,self.llamarfunmetIdFuncionMetodoActual[len(self.llamarfunmetIdFuncionMetodoActual)-1])
                    #Obtengo la direccion del parametro actual
                    numeroParametroActual = self.contadorParametros[len(self.contadorParametros)-1]-1
                    variableParametro = self.dirProcs[self.llamarfunmetIdFuncionMetodoActual[len(self.llamarfunmetIdFuncionMetodoActual)-1],0][2][numeroParametroActual]
                    dirParametroActual = self.tablaVariables[variableParametro[0],variableParametro[1]][2]

                self.guardarCuadruploParam(dirParametroActual)
                ##########################################

                self.state = 361
                self.ll3()

            elif token in [coffParser.PDER]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpresionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.ExpresionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def declaracion(self):
            return self.getTypedRuleContext(coffParser.DeclaracionContext,0)


        def ex1(self):
            return self.getTypedRuleContext(coffParser.Ex1Context,0)


        def getRuleIndex(self):
            return coffParser.RULE_expresion

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterExpresion(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitExpresion(self)




    def expresion(self):

        localctx = coffParser.ExpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_expresion)
        try:
            if self.nComasAux2 == 1 and str(self.getCurrentToken().text) != ")":                
                self.nComasAux = 1
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.declaracion()
            self.crearCuadruploExpAsig(3,'expresion')
            self.state = 367
            self.ex1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Ex1Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.Ex1Context, self).__init__(parent, invokingState)
            self.parser = parser

        def CONDICIONO(self):
            return self.getToken(coffParser.CONDICIONO, 0)

        def expresion(self):
            return self.getTypedRuleContext(coffParser.ExpresionContext,0)


        def CONDICIONY(self):
            return self.getToken(coffParser.CONDICIONY, 0)

        def getRuleIndex(self):
            return coffParser.RULE_ex1

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterEx1(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitEx1(self)




    def ex1(self):

        localctx = coffParser.Ex1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_ex1)
        try:
            self.state = 374
            token = self._input.LA(1)
            if token in [coffParser.CONDICIONO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 369
                self.insertarOperador('||')
                self.match(coffParser.CONDICIONO)
                self.state = 370
                self.expresion()

            elif token in [coffParser.CONDICIONY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 371
                self.insertarOperador('&&')
                self.match(coffParser.CONDICIONY)
                self.state = 372
                self.expresion()

            elif token in [coffParser.PDER, coffParser.CDER, coffParser.COMA, coffParser.PUNTOYCOMA]:
                self.enterOuterAlt(localctx, 3)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclaracionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.DeclaracionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def exp(self):
            return self.getTypedRuleContext(coffParser.ExpContext,0)


        def de1(self):
            return self.getTypedRuleContext(coffParser.De1Context,0)


        def getRuleIndex(self):
            return coffParser.RULE_declaracion

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterDeclaracion(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitDeclaracion(self)




    def declaracion(self):

        localctx = coffParser.DeclaracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_declaracion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.exp()
            self.state = 377
            self.de1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class De1Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.De1Context, self).__init__(parent, invokingState)
            self.parser = parser

        def de2(self):
            return self.getTypedRuleContext(coffParser.De2Context,0)


        def exp(self):
            return self.getTypedRuleContext(coffParser.ExpContext,0)


        def getRuleIndex(self):
            return coffParser.RULE_de1

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterDe1(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitDe1(self)




    def de1(self):

        localctx = coffParser.De1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_de1)
        try:
            self.state = 383
            token = self._input.LA(1)
            if token in [coffParser.IGUALQUE, coffParser.MENQUE, coffParser.MAYQUE, coffParser.MAYIGUALQUE, coffParser.MENIGUALQUE, coffParser.DIF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 379
                if token == coffParser.IGUALQUE:
                    self.insertarOperador('==')
                elif token == coffParser.MENQUE:
                    self.insertarOperador('<')
                elif token == coffParser.MAYQUE:
                    self.insertarOperador('>')
                elif token == coffParser.MAYIGUALQUE:
                    self.insertarOperador('>=')
                elif token == coffParser.MENIGUALQUE:
                    self.insertarOperador('<=')
                elif token == coffParser.DIF:
                    self.insertarOperador('!=')
                self.de2()
                self.state = 380
                self.exp()
                self.crearCuadruploExpAsig(2,'expresion')

            elif token in [coffParser.PDER, coffParser.CDER, coffParser.CONDICIONO, coffParser.CONDICIONY, coffParser.COMA, coffParser.PUNTOYCOMA]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class De2Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.De2Context, self).__init__(parent, invokingState)
            self.parser = parser

        def MAYQUE(self):
            return self.getToken(coffParser.MAYQUE, 0)

        def MENQUE(self):
            return self.getToken(coffParser.MENQUE, 0)

        def IGUALQUE(self):
            return self.getToken(coffParser.IGUALQUE, 0)

        def DIF(self):
            return self.getToken(coffParser.DIF, 0)

        def MAYIGUALQUE(self):
            return self.getToken(coffParser.MAYIGUALQUE, 0)

        def MENIGUALQUE(self):
            return self.getToken(coffParser.MENIGUALQUE, 0)

        def getRuleIndex(self):
            return coffParser.RULE_de2

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterDe2(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitDe2(self)




    def de2(self):

        localctx = coffParser.De2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_de2)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 385
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << coffParser.IGUALQUE) | (1 << coffParser.MENQUE) | (1 << coffParser.MAYQUE) | (1 << coffParser.MAYIGUALQUE) | (1 << coffParser.MENIGUALQUE) | (1 << coffParser.DIF))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.ExpContext, self).__init__(parent, invokingState)
            self.parser = parser

        def termino(self):
            return self.getTypedRuleContext(coffParser.TerminoContext,0)


        def exp1(self):
            return self.getTypedRuleContext(coffParser.Exp1Context,0)


        def getRuleIndex(self):
            return coffParser.RULE_exp

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterExp(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitExp(self)




    def exp(self):

        localctx = coffParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.termino()
            self.crearCuadruploExpAsig(1,'expresion')
            self.state = 388
            self.exp1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Exp1Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.Exp1Context, self).__init__(parent, invokingState)
            self.parser = parser

        def RESTA(self):
            return self.getToken(coffParser.RESTA, 0)

        def exp(self):
            return self.getTypedRuleContext(coffParser.ExpContext,0)


        def SUMA(self):
            return self.getToken(coffParser.SUMA, 0)

        def getRuleIndex(self):
            return coffParser.RULE_exp1

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterExp1(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitExp1(self)




    def exp1(self):

        localctx = coffParser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_exp1)
        try:
            self.state = 395
            token = self._input.LA(1)
            if token in [coffParser.RESTA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 390
                #Meter resta a la pila de operadores
                self.insertarOperador('-')
                self.match(coffParser.RESTA)
                self.state = 391
                self.exp()

            elif token in [coffParser.SUMA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 392
                #Meter suma a la pila de operadores
                self.insertarOperador('+')
                self.match(coffParser.SUMA)
                self.state = 393
                self.exp()

            elif token in [coffParser.PDER, coffParser.CDER, coffParser.IGUALQUE, coffParser.MENQUE, coffParser.MAYQUE, coffParser.MAYIGUALQUE, coffParser.MENIGUALQUE, coffParser.DIF, coffParser.CONDICIONO, coffParser.CONDICIONY, coffParser.COMA, coffParser.PUNTOYCOMA]:
                self.enterOuterAlt(localctx, 3)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TerminoContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.TerminoContext, self).__init__(parent, invokingState)
            self.parser = parser

        def factor(self):
            return self.getTypedRuleContext(coffParser.FactorContext,0)


        def t1(self):
            return self.getTypedRuleContext(coffParser.T1Context,0)


        def getRuleIndex(self):
            return coffParser.RULE_termino

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterTermino(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitTermino(self)




    def termino(self):

        localctx = coffParser.TerminoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_termino)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 397
            self.factor()
            self.crearCuadruploExpAsig(0,'expresion')
            self.state = 398
            self.t1()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class T1Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.T1Context, self).__init__(parent, invokingState)
            self.parser = parser

        def DIV(self):
            return self.getToken(coffParser.DIV, 0)

        def termino(self):
            return self.getTypedRuleContext(coffParser.TerminoContext,0)


        def MULT(self):
            return self.getToken(coffParser.MULT, 0)

        def getRuleIndex(self):
            return coffParser.RULE_t1

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterT1(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitT1(self)




    def t1(self):

        localctx = coffParser.T1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_t1)
        try:
            self.state = 405
            token = self._input.LA(1)
            if token in [coffParser.DIV]:
                self.enterOuterAlt(localctx, 1)
                self.state = 400
                #Meter division a la pila de operadores
                self.insertarOperador('/')
                self.match(coffParser.DIV)
                self.state = 401
                self.termino()

            elif token in [coffParser.MULT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 402
                #Meter multiplicacion a la pila de operadores
                self.insertarOperador('*')
                self.match(coffParser.MULT)
                self.state = 403
                self.termino()

            elif token in [coffParser.PDER, coffParser.CDER, coffParser.SUMA, coffParser.RESTA, coffParser.IGUALQUE, coffParser.MENQUE, coffParser.MAYQUE, coffParser.MAYIGUALQUE, coffParser.MENIGUALQUE, coffParser.DIF, coffParser.CONDICIONO, coffParser.CONDICIONY, coffParser.COMA, coffParser.PUNTOYCOMA]:
                self.enterOuterAlt(localctx, 3)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FactorContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.FactorContext, self).__init__(parent, invokingState)
            self.parser = parser

        def f1(self):
            return self.getTypedRuleContext(coffParser.F1Context,0)


        def valor(self):
            return self.getTypedRuleContext(coffParser.ValorContext,0)


        def PIZQ(self):
            return self.getToken(coffParser.PIZQ, 0)

        def expresion(self):
            return self.getTypedRuleContext(coffParser.ExpresionContext,0)


        def PDER(self):
            return self.getToken(coffParser.PDER, 0)

        def getRuleIndex(self):
            return coffParser.RULE_factor

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterFactor(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitFactor(self)




    def factor(self):

        localctx = coffParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_factor)
        try:
            self.state = 414
            token = self._input.LA(1)
            if token in [coffParser.SUMA, coffParser.RESTA, coffParser.ID, coffParser.CTEENT, coffParser.CTEDEC, coffParser.CTETEXTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 407
                self.f1()
                self.state = 408
                self.valor()

            elif token in [coffParser.PIZQ]:
                self.enterOuterAlt(localctx, 2)
                self.state = 410
                self.match(coffParser.PIZQ)
                self.state = 411
                self.insertarOperador('(')
                self.expresion()
                self.state = 412
                self.match(coffParser.PDER)
                self.pOper.pop()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class F1Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.F1Context, self).__init__(parent, invokingState)
            self.parser = parser

        def RESTA(self):
            return self.getToken(coffParser.RESTA, 0)

        def SUMA(self):
            return self.getToken(coffParser.SUMA, 0)

        def getRuleIndex(self):
            return coffParser.RULE_f1

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterF1(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitF1(self)




    def f1(self):

        localctx = coffParser.F1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_f1)
        try:
            self.state = 419
            token = self._input.LA(1)
            if token in [coffParser.RESTA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 416
                self.match(coffParser.RESTA)
                #Si entra por primera vez la expresion y es negativo
                tofFactor = 1

            elif token in [coffParser.SUMA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 417
                self.match(coffParser.SUMA)

            elif token in [coffParser.ID, coffParser.CTEENT, coffParser.CTEDEC, coffParser.CTETEXTO]:
                self.enterOuterAlt(localctx, 3)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.FuncionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def FUNCION(self):
            return self.getToken(coffParser.FUNCION, 0)

        def fun1(self):
            return self.getTypedRuleContext(coffParser.Fun1Context,0)


        def ID(self):
            return self.getToken(coffParser.ID, 0)

        def parametros(self):
            return self.getTypedRuleContext(coffParser.ParametrosContext,0)


        def BIZQ(self):
            return self.getToken(coffParser.BIZQ, 0)

        def fun2(self):
            return self.getTypedRuleContext(coffParser.Fun2Context,0)


        def BDER(self):
            return self.getToken(coffParser.BDER, 0)

        def getRuleIndex(self):
            return coffParser.RULE_funcion

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterFuncion(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitFuncion(self)




    def funcion(self):

        localctx = coffParser.FuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_funcion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 421
            self.match(coffParser.FUNCION)
            self.state = 422
            self.fun1()
            self.state = 423
            ########################################
            self.resetearDireccionesLocales()
            self.terminacionProc = 'endproc'
            self.scopeProcs = self.scopeProcs + 1
            self.idVariableActual = str(self.getCurrentToken().text)
            self.idFuncionActual  = str(self.getCurrentToken().text)
            if self.metodoTof:

                self.dirProcs[self.idVariableActual,self.claseScopeRef] = [self.scopeProcs,self.tipoVariableActual,[]]
                self.metodosClase.append([self.idVariableActual,self.claseScopeRef])
                self.parametrosAux.append(self.idVariableActual)
                self.parametrosAux.append(self.claseScopeRef)

            else:
                self.dirProcs[self.idVariableActual,0] = [self.scopeProcs,self.tipoVariableActual,[]]
                self.parametrosAux.append(self.idVariableActual)
                self.parametrosAux.append(0)

            #########################################
            self.match(coffParser.ID)
            self.state = 424
            self.listaParametros = []
            self.parametros()
            self.parametrosAux = []
            self.state = 425
            self.match(coffParser.BIZQ)
            self.state = 426
            self.fun2()

            ##########################################
            if self.metodoTof:
                self.dirProcs[self.idFuncionActual,self.claseScopeRef][3] = [self.memLocalEntero - 8999,self.memLocalDecimal - 14999,self.memLocalTexto - 20999]
            else:
                self.dirProcs[self.idFuncionActual,0][3] = [self.memLocalEntero - 8999,self.memLocalDecimal - 14999,self.memLocalTexto - 20999]
            ###########################################

            self.crearCuadruploTerminarProc()
            self.state = 427
            self.match(coffParser.BDER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Fun1Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.Fun1Context, self).__init__(parent, invokingState)
            self.parser = parser

        def fun11(self):
            return self.getTypedRuleContext(coffParser.Fun11Context,0)


        def fun12(self):
            return self.getTypedRuleContext(coffParser.Fun12Context,0)


        def getRuleIndex(self):
            return coffParser.RULE_fun1

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterFun1(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitFun1(self)




    def fun1(self):

        localctx = coffParser.Fun1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_fun1)
        try:
            self.state = 431
            token = self._input.LA(1)
            if token in [coffParser.ENTERO, coffParser.DECIMAL, coffParser.TEXTO, coffParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 429
                self.fun11()

            elif token in [coffParser.VACIO]:
                self.enterOuterAlt(localctx, 2)
                self.state = 430
                self.fun12()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Fun11Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.Fun11Context, self).__init__(parent, invokingState)
            self.parser = parser

        def tipo(self):
            return self.getTypedRuleContext(coffParser.TipoContext,0)


        def getRuleIndex(self):
            return coffParser.RULE_fun11

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterFun11(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitFun11(self)




    def fun11(self):

        localctx = coffParser.Fun11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_fun11)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 433
            self.esTipoFuncionOMetodo = 1
            self.tipo()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Fun12Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.Fun12Context, self).__init__(parent, invokingState)
            self.parser = parser

        def VACIO(self):
            return self.getToken(coffParser.VACIO, 0)

        def getRuleIndex(self):
            return coffParser.RULE_fun12

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterFun12(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitFun12(self)




    def fun12(self):

        localctx = coffParser.Fun12Context(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_fun12)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
            ########################################
            self.tipoVariableActual = str(self.getCurrentToken().text)
            self.tipoActualFuncionOMetodo = str(self.getCurrentToken().text)
            #########################################
            self.match(coffParser.VACIO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Fun2Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.Fun2Context, self).__init__(parent, invokingState)
            self.parser = parser

        def fun23(self):
            return self.getTypedRuleContext(coffParser.Fun23Context,0)


        def fun21(self):
            return self.getTypedRuleContext(coffParser.Fun21Context,0)


        def fun22(self):
            return self.getTypedRuleContext(coffParser.Fun22Context,0)


        def getRuleIndex(self):
            return coffParser.RULE_fun2

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterFun2(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitFun2(self)




    def fun2(self):

        localctx = coffParser.Fun2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_fun2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437

            ###########Cuadruplo inicio de funcion###############
            idClasePadre = self.idDeMetodo(self.idFuncionActual)
            self.dirProcs[self.idFuncionActual,idClasePadre].append([])
            self.dirProcs[self.idFuncionActual,idClasePadre].append(len(self.quadruplos))

            self.fun23()
            self.state = 438
            self.dirProcs[self.idFuncionActual,idClasePadre][3] = self.getNumberOfEDT([self.idFuncionActual,idClasePadre])           
            #####################################################
            self.fun21()
            self.state = 439
            self.fun22()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Fun23Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.Fun23Context, self).__init__(parent, invokingState)
            self.parser = parser

        def variables(self):
            return self.getTypedRuleContext(coffParser.VariablesContext,0)


        def fun23(self):
            return self.getTypedRuleContext(coffParser.Fun23Context,0)


        def getRuleIndex(self):
            return coffParser.RULE_fun23

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterFun23(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitFun23(self)




    def fun23(self):

        localctx = coffParser.Fun23Context(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_fun23)
        try:
            self.state = 445
            token = self._input.LA(1)
            if token in [coffParser.ENTERO, coffParser.DECIMAL, coffParser.TEXTO, coffParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 441
                self.variables()
                self.state = 442
                self.fun23()

            elif token in [coffParser.IMPRIMIR, coffParser.LEER, coffParser.MIENTRAS, coffParser.RETORNA, coffParser.SI, coffParser.EJEC, coffParser.ASIGNA, coffParser.BDER]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Fun21Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.Fun21Context, self).__init__(parent, invokingState)
            self.parser = parser

        def estatuto(self):
            return self.getTypedRuleContext(coffParser.EstatutoContext,0)


        def fun21(self):
            return self.getTypedRuleContext(coffParser.Fun21Context,0)


        def getRuleIndex(self):
            return coffParser.RULE_fun21

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterFun21(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitFun21(self)




    def fun21(self):

        localctx = coffParser.Fun21Context(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_fun21)
        try:
            self.state = 451
            token = self._input.LA(1)
            if token in [coffParser.IMPRIMIR, coffParser.LEER, coffParser.MIENTRAS, coffParser.SI, coffParser.EJEC, coffParser.ASIGNA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 447
                self.estatuto()
                self.state = 448
                self.fun21()

            elif token in [coffParser.RETORNA, coffParser.BDER]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Fun22Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.Fun22Context, self).__init__(parent, invokingState)
            self.parser = parser

        def RETORNA(self):
            return self.getToken(coffParser.RETORNA, 0)

        def expresion(self):
            return self.getTypedRuleContext(coffParser.ExpresionContext,0)


        def PUNTOYCOMA(self):
            return self.getToken(coffParser.PUNTOYCOMA, 0)

        def getRuleIndex(self):
            return coffParser.RULE_fun22

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterFun22(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitFun22(self)




    def fun22(self):

        localctx = coffParser.Fun22Context(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_fun22)
        try:
            self.state = 458
            token = self._input.LA(1)
            if token in [coffParser.RETORNA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 453
                self.match(coffParser.RETORNA)
                self.state = 454
                self.expresion()
                self.state = 455
                if self.tipoActualFuncionOMetodo == "vacio":
                    print("Error, retorno existente en funcion tipo vacio")
                    sys.exit()
                    return

                if self.tipoActualFuncionOMetodo != self.pTipos[len(self.pTipos) - 1]:
                    print("Error, tipo de retorno "+ self.pTipos[len(self.pTipos) - 1]+" no coincide con definicion")
                    sys.exit()
                    return
                self.tipoActualFuncionOMetodo = None
                self.crearCuadruploRetornar()
                self.match(coffParser.PUNTOYCOMA)

            elif token in [coffParser.BDER]:
                if self.tipoActualFuncionOMetodo != "vacio":
                    print("Error, falta retorno en funcion de tipo "+ self.tipoActualFuncionOMetodo)
                    sys.exit()
                    return
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BloqueContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.BloqueContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BIZQ(self):
            return self.getToken(coffParser.BIZQ, 0)

        def b1(self):
            return self.getTypedRuleContext(coffParser.B1Context,0)


        def BDER(self):
            return self.getToken(coffParser.BDER, 0)

        def getRuleIndex(self):
            return coffParser.RULE_bloque

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterBloque(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitBloque(self)




    def bloque(self):

        localctx = coffParser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_bloque)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 460
            self.match(coffParser.BIZQ)
            self.state = 461
            self.b1()
            self.state = 462
            self.match(coffParser.BDER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class B1Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.B1Context, self).__init__(parent, invokingState)
            self.parser = parser

        def estatuto(self):
            return self.getTypedRuleContext(coffParser.EstatutoContext,0)


        def b1(self):
            return self.getTypedRuleContext(coffParser.B1Context,0)


        def getRuleIndex(self):
            return coffParser.RULE_b1

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterB1(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitB1(self)




    def b1(self):

        localctx = coffParser.B1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_b1)
        try:
            self.state = 468
            token = self._input.LA(1)
            if token in [coffParser.IMPRIMIR, coffParser.LEER, coffParser.MIENTRAS, coffParser.SI, coffParser.EJEC, coffParser.ASIGNA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 464
                self.estatuto()
                self.state = 465
                self.b1()

            elif token in [coffParser.BDER]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BloquesimpleContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.BloquesimpleContext, self).__init__(parent, invokingState)
            self.parser = parser

        def BIZQ(self):
            return self.getToken(coffParser.BIZQ, 0)

        def bs1(self):
            return self.getTypedRuleContext(coffParser.Bs1Context,0)


        def BDER(self):
            return self.getToken(coffParser.BDER, 0)

        def getRuleIndex(self):
            return coffParser.RULE_bloquesimple

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterBloquesimple(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitBloquesimple(self)




    def bloquesimple(self):

        localctx = coffParser.BloquesimpleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_bloquesimple)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 470
            self.match(coffParser.BIZQ)
            self.state = 471
            self.bs1()
            self.state = 472
            self.match(coffParser.BDER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Bs1Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.Bs1Context, self).__init__(parent, invokingState)
            self.parser = parser

        def estatutosimple(self):
            return self.getTypedRuleContext(coffParser.EstatutosimpleContext,0)


        def b1(self):
            return self.getTypedRuleContext(coffParser.B1Context,0)


        def getRuleIndex(self):
            return coffParser.RULE_bs1

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterBs1(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitBs1(self)




    def bs1(self):

        localctx = coffParser.Bs1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_bs1)
        try:
            self.state = 478
            token = self._input.LA(1)
            if token in [coffParser.IMPRIMIR, coffParser.LEER, coffParser.MIENTRAS, coffParser.SI, coffParser.EJEC, coffParser.ASIGNA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 474
                self.estatutosimple()
                self.state = 475
                self.b1()

            elif token in [coffParser.BDER]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AsignacionContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.AsignacionContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(coffParser.ID, 0)

        def a1(self):
            return self.getTypedRuleContext(coffParser.A1Context,0)


        def a2(self):
            return self.getTypedRuleContext(coffParser.A2Context,0)


        def IGUAL(self):
            return self.getToken(coffParser.IGUAL, 0)

        def expresion(self):
            return self.getTypedRuleContext(coffParser.ExpresionContext,0)


        def PUNTOYCOMA(self):
            return self.getToken(coffParser.PUNTOYCOMA, 0)

        def getRuleIndex(self):
            return coffParser.RULE_asignacion

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterAsignacion(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitAsignacion(self)




    def asignacion(self):

        localctx = coffParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 480
            self.idVariableActual = str(self.getCurrentToken().text)
            self.ejecToken = self.idVariableActual
            

            tipoVar = self.checkIfVariableExists()

            self.match(coffParser.ID)

            self.state = 481
            self.a1()
            self.state = 482
            self.a2()
            self.state = 483
            self.match(coffParser.IGUAL)
            self.insertarOperador('=')
            self.state = 484
            self.expresion()
            self.state = 485
            self.match(coffParser.PUNTOYCOMA)

            self.crearCuadruploExpAsig(4,'asignacion')
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class A1Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.A1Context, self).__init__(parent, invokingState)
            self.parser = parser

        def PUNTO(self):
            return self.getToken(coffParser.PUNTO, 0)

        def ID(self):
            return self.getToken(coffParser.ID, 0)

        def getRuleIndex(self):
            return coffParser.RULE_a1

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterA1(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitA1(self)


        

    def a1(self):

        localctx = coffParser.A1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_a1)
        try:
            self.state = 490
            token = self._input.LA(1)
            if token in [coffParser.PUNTO]:
                
                self.enterOuterAlt(localctx, 1)
                self.state = 487
                self.claseIDRef = self.tablaVariables[self.idVariableActual,self.scopeProcs][0]
                




                self.match(coffParser.PUNTO)
                self.state = 488
                self.idVariableActual = str(self.getCurrentToken().text)

                
                #Cuadruplo de asignacion
                #self.insertarValorTipo(self.idVariableActual,tipoVar)
                self.checkIfAttributeBelongs(self.idVariableActual,self.ejecToken)
              #########################################################  
                tipoVar = self.obtenerTipoDeAtributo(self.idVariableActual,self.claseIDRef)

                self.insertarValorTipo(self.obtenerDireccionVariable(self.idVariableActual),tipoVar)

                self.match(coffParser.ID)

            elif token in [coffParser.CIZQ, coffParser.IGUAL]:
                tipoVar = self.checkIfVariableExists()
                 #Cuadruplo de asignacion
                self.insertarValorTipo(self.obtenerDireccionVariable(self.idVariableActual),tipoVar)
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class A2Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.A2Context, self).__init__(parent, invokingState)
            self.parser = parser

        def CIZQ(self):
            return self.getToken(coffParser.CIZQ, 0)

        def expresion(self):
            return self.getTypedRuleContext(coffParser.ExpresionContext,0)


        def CDER(self):
            return self.getToken(coffParser.CDER, 0)

        def getRuleIndex(self):
            return coffParser.RULE_a2

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterA2(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitA2(self)




    def a2(self):

        localctx = coffParser.A2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_a2)
        try:
            self.state = 497
            token = self._input.LA(1)
            if token in [coffParser.CIZQ]:
                self.enterOuterAlt(localctx, 1)
                self.state = 492
                self.tokenActual = str(self.getCurrentToken().text)
                self.match(coffParser.CIZQ)
                self.state = 493
                self.expresion()
                self.state = 494
                self.match(coffParser.CDER)

            elif token in [coffParser.IGUAL]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MientrasContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.MientrasContext, self).__init__(parent, invokingState)
            self.parser = parser

        def MIENTRAS(self):
            return self.getToken(coffParser.MIENTRAS, 0)

        def PIZQ(self):
            return self.getToken(coffParser.PIZQ, 0)

        def expresion(self):
            return self.getTypedRuleContext(coffParser.ExpresionContext,0)


        def PDER(self):
            return self.getToken(coffParser.PDER, 0)

        def bloquesimple(self):
            return self.getTypedRuleContext(coffParser.BloquesimpleContext,0)


        def getRuleIndex(self):
            return coffParser.RULE_mientras

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterMientras(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitMientras(self)




    def mientras(self):

        localctx = coffParser.MientrasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_mientras)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 499
            self.match(coffParser.MIENTRAS)
            self.crearCuadruploCondicionInicioCiclo()
            self.state = 500
            self.match(coffParser.PIZQ)
            self.state = 501
            self.expresion()
            self.state = 502
            self.match(coffParser.PDER)
            self.crearCuadruploCondicion()
            self.state = 503
            self.bloquesimple()
            self.crearCuadruploCondicionFinCiclo()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EstatutoContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.EstatutoContext, self).__init__(parent, invokingState)
            self.parser = parser

        def EJEC(self):
            return self.getToken(coffParser.EJEC, 0)

        def llamarfunmet(self):
            return self.getTypedRuleContext(coffParser.LlamarfunmetContext,0)


        def ASIGNA(self):
            return self.getToken(coffParser.ASIGNA, 0)

        def asignacion(self):
            return self.getTypedRuleContext(coffParser.AsignacionContext,0)


        def mientras(self):
            return self.getTypedRuleContext(coffParser.MientrasContext,0)


        def si(self):
            return self.getTypedRuleContext(coffParser.SiContext,0)


        def escritura(self):
            return self.getTypedRuleContext(coffParser.EscrituraContext,0)


        def lectura(self):
            return self.getTypedRuleContext(coffParser.LecturaContext,0)


        def getRuleIndex(self):
            return coffParser.RULE_estatuto

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterEstatuto(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitEstatuto(self)




    def estatuto(self):

        localctx = coffParser.EstatutoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_estatuto)
        try:
            self.state = 513
            token = self._input.LA(1)
            if token in [coffParser.EJEC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 505
                self.match(coffParser.EJEC)
                self.state = 506
                self.llamarfunmet()

            elif token in [coffParser.ASIGNA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 507
                self.match(coffParser.ASIGNA)
                self.state = 508
                self.asignacion()

            elif token in [coffParser.MIENTRAS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 509
                self.mientras()

            elif token in [coffParser.SI]:
                self.enterOuterAlt(localctx, 4)
                self.state = 510
                self.si()

            elif token in [coffParser.IMPRIMIR]:
                self.enterOuterAlt(localctx, 5)
                self.state = 511
                self.escritura()

            elif token in [coffParser.LEER]:
                self.enterOuterAlt(localctx, 6)
                self.state = 512
                self.lectura()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EstatutosimpleContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.EstatutosimpleContext, self).__init__(parent, invokingState)
            self.parser = parser

        def EJEC(self):
            return self.getToken(coffParser.EJEC, 0)

        def llamarfunmet(self):
            return self.getTypedRuleContext(coffParser.LlamarfunmetContext,0)


        def ASIGNA(self):
            return self.getToken(coffParser.ASIGNA, 0)

        def asignacion(self):
            return self.getTypedRuleContext(coffParser.AsignacionContext,0)


        def mientras(self):
            return self.getTypedRuleContext(coffParser.MientrasContext,0)


        def si(self):
            return self.getTypedRuleContext(coffParser.SiContext,0)


        def escritura(self):
            return self.getTypedRuleContext(coffParser.EscrituraContext,0)


        def lectura(self):
            return self.getTypedRuleContext(coffParser.LecturaContext,0)


        def getRuleIndex(self):
            return coffParser.RULE_estatutosimple

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterEstatutosimple(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitEstatutosimple(self)




    def estatutosimple(self):

        localctx = coffParser.EstatutosimpleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_estatutosimple)
        try:
            self.state = 523
            token = self._input.LA(1)
            if token in [coffParser.EJEC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 515
                self.match(coffParser.EJEC)
                self.state = 516
                self.llamarfunmet()

            elif token in [coffParser.ASIGNA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 517
                self.match(coffParser.ASIGNA)
                self.state = 518
                self.asignacion()

            elif token in [coffParser.MIENTRAS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 519
                self.mientras()

            elif token in [coffParser.SI]:
                self.enterOuterAlt(localctx, 4)
                self.state = 520
                self.si()

            elif token in [coffParser.IMPRIMIR]:
                self.enterOuterAlt(localctx, 5)
                self.state = 521
                self.escritura()

            elif token in [coffParser.LEER]:
                self.enterOuterAlt(localctx, 6)
                self.state = 522
                self.lectura()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EscrituraContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.EscrituraContext, self).__init__(parent, invokingState)
            self.parser = parser

        def IMPRIMIR(self):
            return self.getToken(coffParser.IMPRIMIR, 0)

        def PIZQ(self):
            return self.getToken(coffParser.PIZQ, 0)

        def expresion(self):
            return self.getTypedRuleContext(coffParser.ExpresionContext,0)


        def e1(self):
            return self.getTypedRuleContext(coffParser.E1Context,0)


        def PDER(self):
            return self.getToken(coffParser.PDER, 0)

        def PUNTOYCOMA(self):
            return self.getToken(coffParser.PUNTOYCOMA, 0)

        def getRuleIndex(self):
            return coffParser.RULE_escritura

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterEscritura(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitEscritura(self)




    def escritura(self):

        localctx = coffParser.EscrituraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_escritura)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 525
            self.match(coffParser.IMPRIMIR)
            self.state = 526
            self.match(coffParser.PIZQ)
            self.state = 527
            self.expresion()
            self.state = 528
            #Para crear los cuadruplos de escritura
            self.crearCuadruploEscritura()
            self.e1()
            self.state = 529
            self.match(coffParser.PDER)
            self.state = 530
            self.match(coffParser.PUNTOYCOMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class E1Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.E1Context, self).__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(coffParser.COMA, 0)

        def expresion(self):
            return self.getTypedRuleContext(coffParser.ExpresionContext,0)


        def e1(self):
            return self.getTypedRuleContext(coffParser.E1Context,0)


        def getRuleIndex(self):
            return coffParser.RULE_e1

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterE1(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitE1(self)




    def e1(self):

        localctx = coffParser.E1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_e1)
        try:
            self.state = 537
            token = self._input.LA(1)
            if token in [coffParser.COMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 532
                self.match(coffParser.COMA)
                self.state = 533
                self.expresion()
                self.state = 534
                self.crearCuadruploEscritura()
                self.e1()

            elif token in [coffParser.PDER]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LecturaContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.LecturaContext, self).__init__(parent, invokingState)
            self.parser = parser

        def LEER(self):
            return self.getToken(coffParser.LEER, 0)

        def PIZQ(self):
            return self.getToken(coffParser.PIZQ, 0)

        def ID(self):
            return self.getToken(coffParser.ID, 0)

        def l1(self):
            return self.getTypedRuleContext(coffParser.L1Context,0)


        def l2(self):
            return self.getTypedRuleContext(coffParser.L2Context,0)


        def PDER(self):
            return self.getToken(coffParser.PDER, 0)

        def PUNTOYCOMA(self):
            return self.getToken(coffParser.PUNTOYCOMA, 0)

        def getRuleIndex(self):
            return coffParser.RULE_lectura

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterLectura(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitLectura(self)




    def lectura(self):

        localctx = coffParser.LecturaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_lectura)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 539
            self.match(coffParser.LEER)
            self.state = 540
            self.match(coffParser.PIZQ)
            self.state = 541
            self.idVariableActual = str(self.getCurrentToken().text)
            self.checkIfVariableExists()

            self.crearCuadruploLectura(self.obtenerDireccionVariable(self.idVariableActual))
            self.match(coffParser.ID)
            self.state = 542
            self.l1()
            self.state = 543
            self.l2()
            self.state = 544
            self.match(coffParser.PDER)
            self.state = 545
            self.match(coffParser.PUNTOYCOMA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class L1Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.L1Context, self).__init__(parent, invokingState)
            self.parser = parser

        def PUNTO(self):
            return self.getToken(coffParser.PUNTO, 0)

        def ID(self):
            return self.getToken(coffParser.ID, 0)

        def getRuleIndex(self):
            return coffParser.RULE_l1

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterL1(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitL1(self)




    def l1(self):

        localctx = coffParser.L1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_l1)
        try:
            self.state = 550
            token = self._input.LA(1)
            if token in [coffParser.PUNTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 547
                self.match(coffParser.PUNTO)
                self.state = 548
                self.match(coffParser.ID)

            elif token in [coffParser.PDER, coffParser.CIZQ]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class L2Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.L2Context, self).__init__(parent, invokingState)
            self.parser = parser

        def CIZQ(self):
            return self.getToken(coffParser.CIZQ, 0)

        def expresion(self):
            return self.getTypedRuleContext(coffParser.ExpresionContext,0)


        def CDER(self):
            return self.getToken(coffParser.CDER, 0)

        def getRuleIndex(self):
            return coffParser.RULE_l2

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterL2(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitL2(self)




    def l2(self):

        localctx = coffParser.L2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_l2)
        try:
            self.state = 557
            token = self._input.LA(1)
            if token in [coffParser.CIZQ]:
                self.enterOuterAlt(localctx, 1)
                self.state = 552
                self.match(coffParser.CIZQ)
                self.state = 553
                self.expresion()
                self.state = 554
                self.match(coffParser.CDER)

            elif token in [coffParser.PDER]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SiContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.SiContext, self).__init__(parent, invokingState)
            self.parser = parser

        def SI(self):
            return self.getToken(coffParser.SI, 0)

        def PIZQ(self):
            return self.getToken(coffParser.PIZQ, 0)

        def expresion(self):
            return self.getTypedRuleContext(coffParser.ExpresionContext,0)


        def PDER(self):
            return self.getToken(coffParser.PDER, 0)

        def bloque(self):
            return self.getTypedRuleContext(coffParser.BloqueContext,0)


        def si1(self):
            return self.getTypedRuleContext(coffParser.Si1Context,0)


        def getRuleIndex(self):
            return coffParser.RULE_si

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterSi(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitSi(self)




    def si(self):

        localctx = coffParser.SiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_si)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 559
            self.match(coffParser.SI)
            self.state = 560
            self.match(coffParser.PIZQ)
            self.state = 561
            self.expresion()
            self.state = 562
            self.match(coffParser.PDER)
            self.crearCuadruploCondicion()
            self.state = 563
            self.bloque()
            self.state = 564
            self.si1()
            self.crearCuadruploCondicionSalida()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Si1Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.Si1Context, self).__init__(parent, invokingState)
            self.parser = parser

        def O(self):
            return self.getToken(coffParser.O, 0)

        def bloque(self):
            return self.getTypedRuleContext(coffParser.BloqueContext,0)


        def getRuleIndex(self):
            return coffParser.RULE_si1

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterSi1(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitSi1(self)




    def si1(self):

        localctx = coffParser.Si1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 146, self.RULE_si1)
        try:
            self.state = 569
            token = self._input.LA(1)
            if token in [coffParser.O]:
                self.enterOuterAlt(localctx, 1)
                self.state = 566
                self.match(coffParser.O)
                self.state = 567
                self.crearCuadruploCondicionFalso()
                self.bloque()

            elif token in [coffParser.IMPRIMIR, coffParser.LEER, coffParser.MIENTRAS, coffParser.RETORNA, coffParser.SI, coffParser.EJEC, coffParser.ASIGNA, coffParser.BDER]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ClasesContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.ClasesContext, self).__init__(parent, invokingState)
            self.parser = parser

        def CLASE(self):
            return self.getToken(coffParser.CLASE, 0)

        def ID(self):
            return self.getToken(coffParser.ID, 0)

        def cl1(self):
            return self.getTypedRuleContext(coffParser.Cl1Context,0)


        def cl2(self):
            return self.getTypedRuleContext(coffParser.Cl2Context,0)


        def getRuleIndex(self):
            return coffParser.RULE_clases

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterClases(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitClases(self)




    def clases(self):

        localctx = coffParser.ClasesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 148, self.RULE_clases)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 571
            self.match(coffParser.CLASE)
            self.state = 572
            ########################################
            self.scopeProcs = self.scopeProcs + 1
            self.claseScopeRef = self.scopeProcs
            self.claseIDRef = str(self.getCurrentToken().text)
            self.dirProcs[self.claseIDRef,0] = [self.scopeProcs,"",[],[]]
            #########################################
            self.match(coffParser.ID)
            self.state = 573
            self.cl1()
            self.state = 574
            self.cl2()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Cl1Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.Cl1Context, self).__init__(parent, invokingState)
            self.parser = parser

        def EXTIENDE(self):
            return self.getToken(coffParser.EXTIENDE, 0)

        def ID(self):
            return self.getToken(coffParser.ID, 0)

        def getRuleIndex(self):
            return coffParser.RULE_cl1

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterCl1(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitCl1(self)




    def cl1(self):

        localctx = coffParser.Cl1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_cl1)
        try:
            self.state = 579
            token = self._input.LA(1)
            if token in [coffParser.EXTIENDE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 576
                self.match(coffParser.EXTIENDE)
                self.state = 577
                self.checkIfGlobalFunctionOrClassExists(str(self.getCurrentToken().text))


                self.makeInheritance(self.claseIDRef,str(self.getCurrentToken().text))
                self.match(coffParser.ID)

            elif token in [coffParser.BIZQ]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Cl2Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.Cl2Context, self).__init__(parent, invokingState)
            self.parser = parser

        def BIZQ(self):
            return self.getToken(coffParser.BIZQ, 0)

        def atributos(self):
            return self.getTypedRuleContext(coffParser.AtributosContext,0)


        def metodos(self):
            return self.getTypedRuleContext(coffParser.MetodosContext,0)


        def BDER(self):
            return self.getToken(coffParser.BDER, 0)

        def getRuleIndex(self):
            return coffParser.RULE_cl2

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterCl2(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitCl2(self)




    def cl2(self):

        localctx = coffParser.Cl2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_cl2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 581
            self.match(coffParser.BIZQ)
            self.state = 582
            self.atributos()
            self.state = 583
            self.metodos()
            self.state = 584
            self.match(coffParser.BDER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AtributosContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.AtributosContext, self).__init__(parent, invokingState)
            self.parser = parser

        def ATRIBUTOS(self):
            return self.getToken(coffParser.ATRIBUTOS, 0)

        def DOSPUNTOS(self):
            return self.getToken(coffParser.DOSPUNTOS, 0)

        def atr1(self):
            return self.getTypedRuleContext(coffParser.Atr1Context,0)


        def getRuleIndex(self):
            return coffParser.RULE_atributos

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterAtributos(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitAtributos(self)




    def atributos(self):

        localctx = coffParser.AtributosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 154, self.RULE_atributos)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 586
            self.match(coffParser.ATRIBUTOS)
            self.state = 587
            self.match(coffParser.DOSPUNTOS)
            self.state = 588
            self.atributosClase = []
            self.atr1()
            for atributo in self.atributosClase: 
                self.dirProcs[self.claseIDRef,0][2] = copy.copy(self.dirProcs[self.claseIDRef,0][2])
                self.checkForAttributeCollisionsInheritance(atributo,self.dirProcs[self.claseIDRef,0][2])
                self.dirProcs[self.claseIDRef,0][2].append(atributo)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Atr1Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.Atr1Context, self).__init__(parent, invokingState)
            self.parser = parser

        def variables(self):
            return self.getTypedRuleContext(coffParser.VariablesContext,0)


        def atr1(self):
            return self.getTypedRuleContext(coffParser.Atr1Context,0)


        def getRuleIndex(self):
            return coffParser.RULE_atr1

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterAtr1(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitAtr1(self)




    def atr1(self):

        localctx = coffParser.Atr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 156, self.RULE_atr1)
        try:
            self.state = 594
            token = self._input.LA(1)
            if token in [coffParser.ENTERO, coffParser.DECIMAL, coffParser.TEXTO, coffParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 590
                self.atributosTof = 1
                self.variables()
                self.state = 591
                self.atributosTof = 0
                self.atr1()

            elif token in [coffParser.METODOS]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MetodosContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.MetodosContext, self).__init__(parent, invokingState)
            self.parser = parser

        def METODOS(self):
            return self.getToken(coffParser.METODOS, 0)

        def DOSPUNTOS(self):
            return self.getToken(coffParser.DOSPUNTOS, 0)

        def met1(self):
            return self.getTypedRuleContext(coffParser.Met1Context,0)


        def getRuleIndex(self):
            return coffParser.RULE_metodos

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterMetodos(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitMetodos(self)




    def metodos(self):

        localctx = coffParser.MetodosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 158, self.RULE_metodos)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 596
            self.match(coffParser.METODOS)
            self.state = 597
            self.match(coffParser.DOSPUNTOS)
            self.state = 598
            self.metodosClase = []
            self.met1()
            
            for metodo in self.metodosClase:
               self.dirProcs[self.claseIDRef,0][3] = copy.copy(self.dirProcs[self.claseIDRef,0][3])
               self.checkForMethodCollisionsInheritance(metodo,self.dirProcs[self.claseIDRef,0][3])
               self.dirProcs[self.claseIDRef,0][3].append(metodo)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Met1Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.Met1Context, self).__init__(parent, invokingState)
            self.parser = parser

        def funcion(self):
            return self.getTypedRuleContext(coffParser.FuncionContext,0)


        def met1(self):
            return self.getTypedRuleContext(coffParser.Met1Context,0)


        def getRuleIndex(self):
            return coffParser.RULE_met1

        def enterRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.enterMet1(self)

        def exitRule(self, listener):
            if isinstance( listener, coffListener ):
                listener.exitMet1(self)




    def met1(self):

        localctx = coffParser.Met1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 160, self.RULE_met1)
        try:
            self.state = 604
            token = self._input.LA(1)
            if token in [coffParser.FUNCION]:
                self.enterOuterAlt(localctx, 1)
                self.state = 600
                self.funcion()
                self.state = 601
                self.met1()

            elif token in [coffParser.BDER]:
                self.enterOuterAlt(localctx, 2)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx




