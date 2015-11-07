# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from __future__ import print_function
import sys
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
        buf.write(u"\61\u0249\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write(u"J\4K\tK\4L\tL\4M\tM\4N\tN\4O\tO\3\2\3\2\3\2\3\2\3\2\3")
        buf.write(u"\3\3\3\3\3\3\3\5\3\u00a8\n\3\3\4\3\4\3\4\3\4\5\4\u00ae")
        buf.write(u"\n\4\3\5\3\5\3\5\3\5\5\5\u00b4\n\5\3\6\3\6\3\6\3\6\3")
        buf.write(u"\6\3\6\3\6\3\6\3\7\3\7\5\7\u00c0\n\7\3\b\3\b\3\t\3\t")
        buf.write(u"\3\n\3\n\3\n\3\13\3\13\3\13\3\13\5\13\u00cd\n\13\3\f")
        buf.write(u"\3\f\3\f\3\f\3\f\5\f\u00d4\n\f\3\r\3\r\3\16\3\16\3\16")
        buf.write(u"\3\16\3\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3")
        buf.write(u"\20\3\20\3\20\3\20\5\20\u00e9\n\20\3\21\3\21\3\21\3\22")
        buf.write(u"\3\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u00f6\n\22\3")
        buf.write(u"\23\3\23\3\23\3\23\3\23\5\23\u00fd\n\23\3\24\3\24\5\24")
        buf.write(u"\u0101\n\24\3\25\3\25\3\26\3\26\3\26\5\26\u0108\n\26")
        buf.write(u"\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3")
        buf.write(u"\27\5\27\u0115\n\27\3\30\3\30\3\30\3\30\3\30\5\30\u011c")
        buf.write(u"\n\30\3\31\3\31\5\31\u0120\n\31\3\32\3\32\3\32\3\32\3")
        buf.write(u"\33\3\33\3\33\3\33\3\33\3\33\5\33\u012c\n\33\3\34\3\34")
        buf.write(u"\3\35\3\35\3\35\3\35\3\36\3\36\5\36\u0136\n\36\3\37\3")
        buf.write(u"\37\3\37\3\37\3\37\3 \3 \5 \u013f\n \3!\3!\3!\5!\u0144")
        buf.write(u"\n!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\5#\u0150\n#")
        buf.write(u"\3$\3$\3$\3$\5$\u0156\n$\3%\3%\3%\3%\3%\5%\u015d\n%\3")
        buf.write(u"&\3&\3&\3\'\3\'\3\'\3\'\3\'\5\'\u0167\n\'\3(\3(\3(\3")
        buf.write(u")\3)\3)\3)\5)\u0170\n)\3*\3*\3+\3+\3+\3,\3,\3,\3,\3,")
        buf.write(u"\5,\u017c\n,\3-\3-\3-\3.\3.\3.\3.\3.\5.\u0186\n.\3/\3")
        buf.write(u"/\3/\3/\3/\3/\3/\5/\u018f\n/\3\60\3\60\3\60\5\60\u0194")
        buf.write(u"\n\60\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\61\3\62\3")
        buf.write(u"\62\5\62\u01a0\n\62\3\63\3\63\3\64\3\64\3\65\3\65\3\65")
        buf.write(u"\3\66\3\66\3\66\3\66\5\66\u01ad\n\66\3\67\3\67\3\67\3")
        buf.write(u"\67\3\67\5\67\u01b4\n\67\38\38\38\38\39\39\39\39\59\u01be")
        buf.write(u"\n9\3:\3:\3:\3:\3;\3;\3;\3;\5;\u01c8\n;\3<\3<\3<\3<\3")
        buf.write(u"<\3<\3<\3=\3=\3=\5=\u01d4\n=\3>\3>\3>\3>\3>\5>\u01db")
        buf.write(u"\n>\3?\3?\3?\3?\3?\3?\3@\3@\3@\3@\3@\3@\3@\3@\3@\5@\u01ec")
        buf.write(u"\n@\3A\3A\3A\3A\3A\3A\3A\3A\5A\u01f6\nA\3B\3B\3B\3B\3")
        buf.write(u"B\3B\3B\3C\3C\3C\3C\3C\5C\u0204\nC\3D\3D\3D\3D\3D\3D")
        buf.write(u"\3D\3D\3E\3E\3E\5E\u0211\nE\3F\3F\3F\3F\3F\5F\u0218\n")
        buf.write(u"F\3G\3G\3G\3G\3G\3G\3G\3H\3H\3H\5H\u0224\nH\3I\3I\3I")
        buf.write(u"\3I\3I\3J\3J\3J\5J\u022e\nJ\3K\3K\3K\3K\3K\3L\3L\3L\3")
        buf.write(u"L\3M\3M\3M\3M\5M\u023d\nM\3N\3N\3N\3N\3O\3O\3O\3O\5O")
        buf.write(u"\u0247\nO\3O\2\2P\2\4\6\b\n\f\16\20\22\24\26\30\32\34")
        buf.write(u"\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjl")
        buf.write(u"nprtvxz|~\u0080\u0082\u0084\u0086\u0088\u008a\u008c\u008e")
        buf.write(u"\u0090\u0092\u0094\u0096\u0098\u009a\u009c\2\6\4\2\7")
        buf.write(u"\t--\3\2.\60\3\2\7\t\4\2\37\37!%\u0236\2\u009e\3\2\2")
        buf.write(u"\2\4\u00a7\3\2\2\2\6\u00ad\3\2\2\2\b\u00b3\3\2\2\2\n")
        buf.write(u"\u00b5\3\2\2\2\f\u00bf\3\2\2\2\16\u00c1\3\2\2\2\20\u00c3")
        buf.write(u"\3\2\2\2\22\u00c5\3\2\2\2\24\u00cc\3\2\2\2\26\u00d3\3")
        buf.write(u"\2\2\2\30\u00d5\3\2\2\2\32\u00d7\3\2\2\2\34\u00db\3\2")
        buf.write(u"\2\2\36\u00e8\3\2\2\2 \u00ea\3\2\2\2\"\u00f5\3\2\2\2")
        buf.write(u"$\u00fc\3\2\2\2&\u0100\3\2\2\2(\u0102\3\2\2\2*\u0107")
        buf.write(u"\3\2\2\2,\u0114\3\2\2\2.\u011b\3\2\2\2\60\u011f\3\2\2")
        buf.write(u"\2\62\u0121\3\2\2\2\64\u012b\3\2\2\2\66\u012d\3\2\2\2")
        buf.write(u"8\u012f\3\2\2\2:\u0135\3\2\2\2<\u0137\3\2\2\2>\u013e")
        buf.write(u"\3\2\2\2@\u0143\3\2\2\2B\u0145\3\2\2\2D\u014f\3\2\2\2")
        buf.write(u"F\u0155\3\2\2\2H\u015c\3\2\2\2J\u015e\3\2\2\2L\u0166")
        buf.write(u"\3\2\2\2N\u0168\3\2\2\2P\u016f\3\2\2\2R\u0171\3\2\2\2")
        buf.write(u"T\u0173\3\2\2\2V\u017b\3\2\2\2X\u017d\3\2\2\2Z\u0185")
        buf.write(u"\3\2\2\2\\\u018e\3\2\2\2^\u0193\3\2\2\2`\u0195\3\2\2")
        buf.write(u"\2b\u019f\3\2\2\2d\u01a1\3\2\2\2f\u01a3\3\2\2\2h\u01a5")
        buf.write(u"\3\2\2\2j\u01ac\3\2\2\2l\u01b3\3\2\2\2n\u01b5\3\2\2\2")
        buf.write(u"p\u01bd\3\2\2\2r\u01bf\3\2\2\2t\u01c7\3\2\2\2v\u01c9")
        buf.write(u"\3\2\2\2x\u01d3\3\2\2\2z\u01da\3\2\2\2|\u01dc\3\2\2\2")
        buf.write(u"~\u01eb\3\2\2\2\u0080\u01f5\3\2\2\2\u0082\u01f7\3\2\2")
        buf.write(u"\2\u0084\u0203\3\2\2\2\u0086\u0205\3\2\2\2\u0088\u0210")
        buf.write(u"\3\2\2\2\u008a\u0217\3\2\2\2\u008c\u0219\3\2\2\2\u008e")
        buf.write(u"\u0223\3\2\2\2\u0090\u0225\3\2\2\2\u0092\u022d\3\2\2")
        buf.write(u"\2\u0094\u022f\3\2\2\2\u0096\u0234\3\2\2\2\u0098\u023c")
        buf.write(u"\3\2\2\2\u009a\u023e\3\2\2\2\u009c\u0246\3\2\2\2\u009e")
        buf.write(u"\u009f\5\4\3\2\u009f\u00a0\5\6\4\2\u00a0\u00a1\5\b\5")
        buf.write(u"\2\u00a1\u00a2\5\n\6\2\u00a2\3\3\2\2\2\u00a3\u00a4\5")
        buf.write(u"\u0090I\2\u00a4\u00a5\5\4\3\2\u00a5\u00a8\3\2\2\2\u00a6")
        buf.write(u"\u00a8\3\2\2\2\u00a7\u00a3\3\2\2\2\u00a7\u00a6\3\2\2")
        buf.write(u"\2\u00a8\5\3\2\2\2\u00a9\u00aa\5`\61\2\u00aa\u00ab\5")
        buf.write(u"\6\4\2\u00ab\u00ae\3\2\2\2\u00ac\u00ae\3\2\2\2\u00ad")
        buf.write(u"\u00a9\3\2\2\2\u00ad\u00ac\3\2\2\2\u00ae\7\3\2\2\2\u00af")
        buf.write(u"\u00b0\5\32\16\2\u00b0\u00b1\5\b\5\2\u00b1\u00b4\3\2")
        buf.write(u"\2\2\u00b2\u00b4\3\2\2\2\u00b3\u00af\3\2\2\2\u00b3\u00b2")
        buf.write(u"\3\2\2\2\u00b4\t\3\2\2\2\u00b5\u00b6\7\20\2\2\u00b6\u00b7")
        buf.write(u"\5\f\7\2\u00b7\u00b8\7-\2\2\u00b8\u00b9\58\35\2\u00b9")
        buf.write(u"\u00ba\7\27\2\2\u00ba\u00bb\5\22\n\2\u00bb\u00bc\7\30")
        buf.write(u"\2\2\u00bc\13\3\2\2\2\u00bd\u00c0\5\16\b\2\u00be\u00c0")
        buf.write(u"\5\20\t\2\u00bf\u00bd\3\2\2\2\u00bf\u00be\3\2\2\2\u00c0")
        buf.write(u"\r\3\2\2\2\u00c1\u00c2\5\66\34\2\u00c2\17\3\2\2\2\u00c3")
        buf.write(u"\u00c4\7\5\2\2\u00c4\21\3\2\2\2\u00c5\u00c6\5\24\13\2")
        buf.write(u"\u00c6\u00c7\5\26\f\2\u00c7\23\3\2\2\2\u00c8\u00c9\5")
        buf.write(u"~@\2\u00c9\u00ca\5\24\13\2\u00ca\u00cd\3\2\2\2\u00cb")
        buf.write(u"\u00cd\3\2\2\2\u00cc\u00c8\3\2\2\2\u00cc\u00cb\3\2\2")
        buf.write(u"\2\u00cd\25\3\2\2\2\u00ce\u00cf\7\n\2\2\u00cf\u00d0\5")
        buf.write(u"J&\2\u00d0\u00d1\7*\2\2\u00d1\u00d4\3\2\2\2\u00d2\u00d4")
        buf.write(u"\3\2\2\2\u00d3\u00ce\3\2\2\2\u00d3\u00d2\3\2\2\2\u00d4")
        buf.write(u"\27\3\2\2\2\u00d5\u00d6\t\2\2\2\u00d6\31\3\2\2\2\u00d7")
        buf.write(u"\u00d8\5\30\r\2\u00d8\u00d9\5\34\17\2\u00d9\u00da\7*")
        buf.write(u"\2\2\u00da\33\3\2\2\2\u00db\u00dc\7-\2\2\u00dc\u00dd")
        buf.write(u"\5\36\20\2\u00dd\35\3\2\2\2\u00de\u00df\7\31\2\2\u00df")
        buf.write(u"\u00e0\7.\2\2\u00e0\u00e1\7\32\2\2\u00e1\u00e9\5\"\22")
        buf.write(u"\2\u00e2\u00e3\7 \2\2\u00e3\u00e4\5(\25\2\u00e4\u00e5")
        buf.write(u"\5&\24\2\u00e5\u00e9\3\2\2\2\u00e6\u00e9\5 \21\2\u00e7")
        buf.write(u"\u00e9\3\2\2\2\u00e8\u00de\3\2\2\2\u00e8\u00e2\3\2\2")
        buf.write(u"\2\u00e8\u00e6\3\2\2\2\u00e8\u00e7\3\2\2\2\u00e9\37\3")
        buf.write(u"\2\2\2\u00ea\u00eb\7)\2\2\u00eb\u00ec\5\34\17\2\u00ec")
        buf.write(u"!\3\2\2\2\u00ed\u00f6\5&\24\2\u00ee\u00ef\7 \2\2\u00ef")
        buf.write(u"\u00f0\7\31\2\2\u00f0\u00f1\5(\25\2\u00f1\u00f2\5$\23")
        buf.write(u"\2\u00f2\u00f3\7\32\2\2\u00f3\u00f4\5&\24\2\u00f4\u00f6")
        buf.write(u"\3\2\2\2\u00f5\u00ed\3\2\2\2\u00f5\u00ee\3\2\2\2\u00f6")
        buf.write(u"#\3\2\2\2\u00f7\u00f8\7)\2\2\u00f8\u00f9\5(\25\2\u00f9")
        buf.write(u"\u00fa\5$\23\2\u00fa\u00fd\3\2\2\2\u00fb\u00fd\3\2\2")
        buf.write(u"\2\u00fc\u00f7\3\2\2\2\u00fc\u00fb\3\2\2\2\u00fd%\3\2")
        buf.write(u"\2\2\u00fe\u0101\5 \21\2\u00ff\u0101\3\2\2\2\u0100\u00fe")
        buf.write(u"\3\2\2\2\u0100\u00ff\3\2\2\2\u0101\'\3\2\2\2\u0102\u0103")
        buf.write(u"\t\3\2\2\u0103)\3\2\2\2\u0104\u0108\5(\25\2\u0105\u0106")
        buf.write(u"\7-\2\2\u0106\u0108\5,\27\2\u0107\u0104\3\2\2\2\u0107")
        buf.write(u"\u0105\3\2\2\2\u0108+\3\2\2\2\u0109\u0115\5\62\32\2\u010a")
        buf.write(u"\u010b\7\25\2\2\u010b\u010c\5J&\2\u010c\u010d\5.\30\2")
        buf.write(u"\u010d\u010e\7\26\2\2\u010e\u0115\3\2\2\2\u010f\u0110")
        buf.write(u"\7\31\2\2\u0110\u0111\7.\2\2\u0111\u0112\7\32\2\2\u0112")
        buf.write(u"\u0115\5\60\31\2\u0113\u0115\3\2\2\2\u0114\u0109\3\2")
        buf.write(u"\2\2\u0114\u010a\3\2\2\2\u0114\u010f\3\2\2\2\u0114\u0113")
        buf.write(u"\3\2\2\2\u0115-\3\2\2\2\u0116\u0117\7)\2\2\u0117\u0118")
        buf.write(u"\5J&\2\u0118\u0119\5.\30\2\u0119\u011c\3\2\2\2\u011a")
        buf.write(u"\u011c\3\2\2\2\u011b\u0116\3\2\2\2\u011b\u011a\3\2\2")
        buf.write(u"\2\u011c/\3\2\2\2\u011d\u0120\5\62\32\2\u011e\u0120\3")
        buf.write(u"\2\2\2\u011f\u011d\3\2\2\2\u011f\u011e\3\2\2\2\u0120")
        buf.write(u"\61\3\2\2\2\u0121\u0122\7,\2\2\u0122\u0123\7-\2\2\u0123")
        buf.write(u"\u0124\5\64\33\2\u0124\63\3\2\2\2\u0125\u0126\7\25\2")
        buf.write(u"\2\u0126\u0127\5J&\2\u0127\u0128\5.\30\2\u0128\u0129")
        buf.write(u"\7\26\2\2\u0129\u012c\3\2\2\2\u012a\u012c\3\2\2\2\u012b")
        buf.write(u"\u0125\3\2\2\2\u012b\u012a\3\2\2\2\u012c\65\3\2\2\2\u012d")
        buf.write(u"\u012e\t\4\2\2\u012e\67\3\2\2\2\u012f\u0130\7\25\2\2")
        buf.write(u"\u0130\u0131\5:\36\2\u0131\u0132\7\26\2\2\u01329\3\2")
        buf.write(u"\2\2\u0133\u0136\5<\37\2\u0134\u0136\3\2\2\2\u0135\u0133")
        buf.write(u"\3\2\2\2\u0135\u0134\3\2\2\2\u0136;\3\2\2\2\u0137\u0138")
        buf.write(u"\5\66\34\2\u0138\u0139\5> \2\u0139\u013a\7-\2\2\u013a")
        buf.write(u"\u013b\5@!\2\u013b=\3\2\2\2\u013c\u013f\7(\2\2\u013d")
        buf.write(u"\u013f\3\2\2\2\u013e\u013c\3\2\2\2\u013e\u013d\3\2\2")
        buf.write(u"\2\u013f?\3\2\2\2\u0140\u0141\7)\2\2\u0141\u0144\5:\36")
        buf.write(u"\2\u0142\u0144\3\2\2\2\u0143\u0140\3\2\2\2\u0143\u0142")
        buf.write(u"\3\2\2\2\u0144A\3\2\2\2\u0145\u0146\7-\2\2\u0146\u0147")
        buf.write(u"\5D#\2\u0147\u0148\7\25\2\2\u0148\u0149\5F$\2\u0149\u014a")
        buf.write(u"\7\26\2\2\u014a\u014b\7*\2\2\u014bC\3\2\2\2\u014c\u014d")
        buf.write(u"\7,\2\2\u014d\u0150\7-\2\2\u014e\u0150\3\2\2\2\u014f")
        buf.write(u"\u014c\3\2\2\2\u014f\u014e\3\2\2\2\u0150E\3\2\2\2\u0151")
        buf.write(u"\u0152\5J&\2\u0152\u0153\5H%\2\u0153\u0156\3\2\2\2\u0154")
        buf.write(u"\u0156\3\2\2\2\u0155\u0151\3\2\2\2\u0155\u0154\3\2\2")
        buf.write(u"\2\u0156G\3\2\2\2\u0157\u0158\7)\2\2\u0158\u0159\5J&")
        buf.write(u"\2\u0159\u015a\5H%\2\u015a\u015d\3\2\2\2\u015b\u015d")
        buf.write(u"\3\2\2\2\u015c\u0157\3\2\2\2\u015c\u015b\3\2\2\2\u015d")
        buf.write(u"I\3\2\2\2\u015e\u015f\5N(\2\u015f\u0160\5L\'\2\u0160")
        buf.write(u"K\3\2\2\2\u0161\u0162\7&\2\2\u0162\u0167\5J&\2\u0163")
        buf.write(u"\u0164\7\'\2\2\u0164\u0167\5J&\2\u0165\u0167\3\2\2\2")
        buf.write(u"\u0166\u0161\3\2\2\2\u0166\u0163\3\2\2\2\u0166\u0165")
        buf.write(u"\3\2\2\2\u0167M\3\2\2\2\u0168\u0169\5T+\2\u0169\u016a")
        buf.write(u"\5P)\2\u016aO\3\2\2\2\u016b\u016c\5R*\2\u016c\u016d\5")
        buf.write(u"T+\2\u016d\u0170\3\2\2\2\u016e\u0170\3\2\2\2\u016f\u016b")
        buf.write(u"\3\2\2\2\u016f\u016e\3\2\2\2\u0170Q\3\2\2\2\u0171\u0172")
        buf.write(u"\t\5\2\2\u0172S\3\2\2\2\u0173\u0174\5X-\2\u0174\u0175")
        buf.write(u"\5V,\2\u0175U\3\2\2\2\u0176\u0177\7\34\2\2\u0177\u017c")
        buf.write(u"\5T+\2\u0178\u0179\7\33\2\2\u0179\u017c\5T+\2\u017a\u017c")
        buf.write(u"\3\2\2\2\u017b\u0176\3\2\2\2\u017b\u0178\3\2\2\2\u017b")
        buf.write(u"\u017a\3\2\2\2\u017cW\3\2\2\2\u017d\u017e\5\\/\2\u017e")
        buf.write(u"\u017f\5Z.\2\u017fY\3\2\2\2\u0180\u0181\7\35\2\2\u0181")
        buf.write(u"\u0186\5X-\2\u0182\u0183\7\36\2\2\u0183\u0186\5X-\2\u0184")
        buf.write(u"\u0186\3\2\2\2\u0185\u0180\3\2\2\2\u0185\u0182\3\2\2")
        buf.write(u"\2\u0185\u0184\3\2\2\2\u0186[\3\2\2\2\u0187\u0188\5^")
        buf.write(u"\60\2\u0188\u0189\5*\26\2\u0189\u018f\3\2\2\2\u018a\u018b")
        buf.write(u"\7\25\2\2\u018b\u018c\5J&\2\u018c\u018d\7\26\2\2\u018d")
        buf.write(u"\u018f\3\2\2\2\u018e\u0187\3\2\2\2\u018e\u018a\3\2\2")
        buf.write(u"\2\u018f]\3\2\2\2\u0190\u0194\7\34\2\2\u0191\u0194\7")
        buf.write(u"\33\2\2\u0192\u0194\3\2\2\2\u0193\u0190\3\2\2\2\u0193")
        buf.write(u"\u0191\3\2\2\2\u0193\u0192\3\2\2\2\u0194_\3\2\2\2\u0195")
        buf.write(u"\u0196\7\f\2\2\u0196\u0197\5b\62\2\u0197\u0198\7-\2\2")
        buf.write(u"\u0198\u0199\58\35\2\u0199\u019a\7\27\2\2\u019a\u019b")
        buf.write(u"\5h\65\2\u019b\u019c\7\30\2\2\u019ca\3\2\2\2\u019d\u01a0")
        buf.write(u"\5d\63\2\u019e\u01a0\5f\64\2\u019f\u019d\3\2\2\2\u019f")
        buf.write(u"\u019e\3\2\2\2\u01a0c\3\2\2\2\u01a1\u01a2\5\30\r\2\u01a2")
        buf.write(u"e\3\2\2\2\u01a3\u01a4\7\5\2\2\u01a4g\3\2\2\2\u01a5\u01a6")
        buf.write(u"\5j\66\2\u01a6\u01a7\5l\67\2\u01a7i\3\2\2\2\u01a8\u01a9")
        buf.write(u"\5~@\2\u01a9\u01aa\5j\66\2\u01aa\u01ad\3\2\2\2\u01ab")
        buf.write(u"\u01ad\3\2\2\2\u01ac\u01a8\3\2\2\2\u01ac\u01ab\3\2\2")
        buf.write(u"\2\u01adk\3\2\2\2\u01ae\u01af\7\n\2\2\u01af\u01b0\5J")
        buf.write(u"&\2\u01b0\u01b1\7*\2\2\u01b1\u01b4\3\2\2\2\u01b2\u01b4")
        buf.write(u"\3\2\2\2\u01b3\u01ae\3\2\2\2\u01b3\u01b2\3\2\2\2\u01b4")
        buf.write(u"m\3\2\2\2\u01b5\u01b6\7\27\2\2\u01b6\u01b7\5p9\2\u01b7")
        buf.write(u"\u01b8\7\30\2\2\u01b8o\3\2\2\2\u01b9\u01ba\5~@\2\u01ba")
        buf.write(u"\u01bb\5p9\2\u01bb\u01be\3\2\2\2\u01bc\u01be\3\2\2\2")
        buf.write(u"\u01bd\u01b9\3\2\2\2\u01bd\u01bc\3\2\2\2\u01beq\3\2\2")
        buf.write(u"\2\u01bf\u01c0\7\27\2\2\u01c0\u01c1\5t;\2\u01c1\u01c2")
        buf.write(u"\7\30\2\2\u01c2s\3\2\2\2\u01c3\u01c4\5\u0080A\2\u01c4")
        buf.write(u"\u01c5\5p9\2\u01c5\u01c8\3\2\2\2\u01c6\u01c8\3\2\2\2")
        buf.write(u"\u01c7\u01c3\3\2\2\2\u01c7\u01c6\3\2\2\2\u01c8u\3\2\2")
        buf.write(u"\2\u01c9\u01ca\7-\2\2\u01ca\u01cb\5x=\2\u01cb\u01cc\5")
        buf.write(u"z>\2\u01cc\u01cd\7 \2\2\u01cd\u01ce\5J&\2\u01ce\u01cf")
        buf.write(u"\7*\2\2\u01cfw\3\2\2\2\u01d0\u01d1\7,\2\2\u01d1\u01d4")
        buf.write(u"\7-\2\2\u01d2\u01d4\3\2\2\2\u01d3\u01d0\3\2\2\2\u01d3")
        buf.write(u"\u01d2\3\2\2\2\u01d4y\3\2\2\2\u01d5\u01d6\7\31\2\2\u01d6")
        buf.write(u"\u01d7\5J&\2\u01d7\u01d8\7\32\2\2\u01d8\u01db\3\2\2\2")
        buf.write(u"\u01d9\u01db\3\2\2\2\u01da\u01d5\3\2\2\2\u01da\u01d9")
        buf.write(u"\3\2\2\2\u01db{\3\2\2\2\u01dc\u01dd\7\6\2\2\u01dd\u01de")
        buf.write(u"\7\25\2\2\u01de\u01df\5J&\2\u01df\u01e0\7\26\2\2\u01e0")
        buf.write(u"\u01e1\5r:\2\u01e1}\3\2\2\2\u01e2\u01ec\5\32\16\2\u01e3")
        buf.write(u"\u01e4\7\23\2\2\u01e4\u01ec\5B\"\2\u01e5\u01e6\7\24\2")
        buf.write(u"\2\u01e6\u01ec\5v<\2\u01e7\u01ec\5|?\2\u01e8\u01ec\5")
        buf.write(u"\u008cG\2\u01e9\u01ec\5\u0082B\2\u01ea\u01ec\5\u0086")
        buf.write(u"D\2\u01eb\u01e2\3\2\2\2\u01eb\u01e3\3\2\2\2\u01eb\u01e5")
        buf.write(u"\3\2\2\2\u01eb\u01e7\3\2\2\2\u01eb\u01e8\3\2\2\2\u01eb")
        buf.write(u"\u01e9\3\2\2\2\u01eb\u01ea\3\2\2\2\u01ec\177\3\2\2\2")
        buf.write(u"\u01ed\u01ee\7\23\2\2\u01ee\u01f6\5B\"\2\u01ef\u01f0")
        buf.write(u"\7\24\2\2\u01f0\u01f6\5v<\2\u01f1\u01f6\5|?\2\u01f2\u01f6")
        buf.write(u"\5\u008cG\2\u01f3\u01f6\5\u0082B\2\u01f4\u01f6\5\u0086")
        buf.write(u"D\2\u01f5\u01ed\3\2\2\2\u01f5\u01ef\3\2\2\2\u01f5\u01f1")
        buf.write(u"\3\2\2\2\u01f5\u01f2\3\2\2\2\u01f5\u01f3\3\2\2\2\u01f5")
        buf.write(u"\u01f4\3\2\2\2\u01f6\u0081\3\2\2\2\u01f7\u01f8\7\3\2")
        buf.write(u"\2\u01f8\u01f9\7\25\2\2\u01f9\u01fa\5J&\2\u01fa\u01fb")
        buf.write(u"\5\u0084C\2\u01fb\u01fc\7\26\2\2\u01fc\u01fd\7*\2\2\u01fd")
        buf.write(u"\u0083\3\2\2\2\u01fe\u01ff\7)\2\2\u01ff\u0200\5J&\2\u0200")
        buf.write(u"\u0201\5\u0084C\2\u0201\u0204\3\2\2\2\u0202\u0204\3\2")
        buf.write(u"\2\2\u0203\u01fe\3\2\2\2\u0203\u0202\3\2\2\2\u0204\u0085")
        buf.write(u"\3\2\2\2\u0205\u0206\7\4\2\2\u0206\u0207\7\25\2\2\u0207")
        buf.write(u"\u0208\7-\2\2\u0208\u0209\5\u0088E\2\u0209\u020a\5\u008a")
        buf.write(u"F\2\u020a\u020b\7\26\2\2\u020b\u020c\7*\2\2\u020c\u0087")
        buf.write(u"\3\2\2\2\u020d\u020e\7,\2\2\u020e\u0211\7-\2\2\u020f")
        buf.write(u"\u0211\3\2\2\2\u0210\u020d\3\2\2\2\u0210\u020f\3\2\2")
        buf.write(u"\2\u0211\u0089\3\2\2\2\u0212\u0213\7\31\2\2\u0213\u0214")
        buf.write(u"\5J&\2\u0214\u0215\7\32\2\2\u0215\u0218\3\2\2\2\u0216")
        buf.write(u"\u0218\3\2\2\2\u0217\u0212\3\2\2\2\u0217\u0216\3\2\2")
        buf.write(u"\2\u0218\u008b\3\2\2\2\u0219\u021a\7\21\2\2\u021a\u021b")
        buf.write(u"\7\25\2\2\u021b\u021c\5J&\2\u021c\u021d\7\26\2\2\u021d")
        buf.write(u"\u021e\5n8\2\u021e\u021f\5\u008eH\2\u021f\u008d\3\2\2")
        buf.write(u"\2\u0220\u0221\7\22\2\2\u0221\u0224\5n8\2\u0222\u0224")
        buf.write(u"\3\2\2\2\u0223\u0220\3\2\2\2\u0223\u0222\3\2\2\2\u0224")
        buf.write(u"\u008f\3\2\2\2\u0225\u0226\7\13\2\2\u0226\u0227\7-\2")
        buf.write(u"\2\u0227\u0228\5\u0092J\2\u0228\u0229\5\u0094K\2\u0229")
        buf.write(u"\u0091\3\2\2\2\u022a\u022b\7\r\2\2\u022b\u022e\7-\2\2")
        buf.write(u"\u022c\u022e\3\2\2\2\u022d\u022a\3\2\2\2\u022d\u022c")
        buf.write(u"\3\2\2\2\u022e\u0093\3\2\2\2\u022f\u0230\7\27\2\2\u0230")
        buf.write(u"\u0231\5\u0096L\2\u0231\u0232\5\u009aN\2\u0232\u0233")
        buf.write(u"\7\30\2\2\u0233\u0095\3\2\2\2\u0234\u0235\7\16\2\2\u0235")
        buf.write(u"\u0236\7+\2\2\u0236\u0237\5\u0098M\2\u0237\u0097\3\2")
        buf.write(u"\2\2\u0238\u0239\5\32\16\2\u0239\u023a\5\u0098M\2\u023a")
        buf.write(u"\u023d\3\2\2\2\u023b\u023d\3\2\2\2\u023c\u0238\3\2\2")
        buf.write(u"\2\u023c\u023b\3\2\2\2\u023d\u0099\3\2\2\2\u023e\u023f")
        buf.write(u"\7\17\2\2\u023f\u0240\7+\2\2\u0240\u0241\5\u009cO\2\u0241")
        buf.write(u"\u009b\3\2\2\2\u0242\u0243\5`\61\2\u0243\u0244\5\u009c")
        buf.write(u"O\2\u0244\u0247\3\2\2\2\u0245\u0247\3\2\2\2\u0246\u0242")
        buf.write(u"\3\2\2\2\u0246\u0245\3\2\2\2\u0247\u009d\3\2\2\2-\u00a7")
        buf.write(u"\u00ad\u00b3\u00bf\u00cc\u00d3\u00e8\u00f5\u00fc\u0100")
        buf.write(u"\u0107\u0114\u011b\u011f\u012b\u0135\u013e\u0143\u014f")
        buf.write(u"\u0155\u015c\u0166\u016f\u017b\u0185\u018e\u0193\u019f")
        buf.write(u"\u01ac\u01b3\u01bd\u01c7\u01d3\u01da\u01eb\u01f5\u0203")
        buf.write(u"\u0210\u0217\u0223\u022d\u023c\u0246")
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

    claseRef = 0

    globalTof = 0


    tablaVariables = {}

    pilaO = [] #Pila de operandos

    pOper = [] #Pila de operadores

    pTipos = [] #Pila de tipos de los operadores

    quadruplos = [] #Lista de cuadruplos

    contQuadTemporales = 1 #Para variables temporales

    tofFactor = 0

    cuboSemantico = cuboSemantico() #Para hacer las validaciones semanticas
    
    checkifAttributeBelongsClassID = None

    lookForObjectClassObjectType = None
    lookForObjectClassClassID = None

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
    RULE_pr21 = 9
    RULE_pr22 = 10
    RULE_tipo = 11
    RULE_variables = 12
    RULE_v1 = 13
    RULE_v2 = 14
    RULE_v3 = 15
    RULE_v4 = 16
    RULE_v5 = 17
    RULE_v6 = 18
    RULE_valordeclaracion = 19
    RULE_valor = 20
    RULE_va1 = 21
    RULE_va2 = 22
    RULE_va3 = 23
    RULE_va4 = 24
    RULE_va5 = 25
    RULE_tiposimple = 26
    RULE_parametros = 27
    RULE_pa1 = 28
    RULE_pa11 = 29
    RULE_pa2 = 30
    RULE_pa3 = 31
    RULE_llamarfunmet = 32
    RULE_ll1 = 33
    RULE_ll2 = 34
    RULE_ll3 = 35
    RULE_expresion = 36
    RULE_ex1 = 37
    RULE_declaracion = 38
    RULE_de1 = 39
    RULE_de2 = 40
    RULE_exp = 41
    RULE_exp1 = 42
    RULE_termino = 43
    RULE_t1 = 44
    RULE_factor = 45
    RULE_f1 = 46
    RULE_funcion = 47
    RULE_fun1 = 48
    RULE_fun11 = 49
    RULE_fun12 = 50
    RULE_fun2 = 51
    RULE_fun21 = 52
    RULE_fun22 = 53
    RULE_bloque = 54
    RULE_b1 = 55
    RULE_bloquesimple = 56
    RULE_bs1 = 57
    RULE_asignacion = 58
    RULE_a1 = 59
    RULE_a2 = 60
    RULE_mientras = 61
    RULE_estatuto = 62
    RULE_estatutosimple = 63
    RULE_escritura = 64
    RULE_e1 = 65
    RULE_lectura = 66
    RULE_l1 = 67
    RULE_l2 = 68
    RULE_si = 69
    RULE_si1 = 70
    RULE_clases = 71
    RULE_cl1 = 72
    RULE_cl2 = 73
    RULE_atributos = 74
    RULE_atr1 = 75
    RULE_metodos = 76
    RULE_met1 = 77

    ruleNames =  [ u"programa", u"p1", u"p2", u"p3", u"principal", u"pr1", 
                   u"pr11", u"pr12", u"pr2", u"pr21", u"pr22", u"tipo", 
                   u"variables", u"v1", u"v2", u"v3", u"v4", u"v5", u"v6", 
                   u"valordeclaracion", u"valor", u"va1", u"va2", u"va3", 
                   u"va4", u"va5", u"tiposimple", u"parametros", u"pa1", 
                   u"pa11", u"pa2", u"pa3", u"llamarfunmet", u"ll1", u"ll2", 
                   u"ll3", u"expresion", u"ex1", u"declaracion", u"de1", 
                   u"de2", u"exp", u"exp1", u"termino", u"t1", u"factor", 
                   u"f1", u"funcion", u"fun1", u"fun11", u"fun12", u"fun2", 
                   u"fun21", u"fun22", u"bloque", u"b1", u"bloquesimple", 
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

    def insertarValorTipo(self,op,tipoOp):
        self.pilaO.append(op)
        self.pTipos.append(tipoOp)

    def insertarOperador(self,op):
        self.pOper.append(op)

    def crearCuadruplo(self,op):
        oper = self.pOper.pop()
        if oper == op:
            oDer = self.pilaO.pop()
            oIzq = self.pilaO.pop()
            res = self.cuboSemantico.checarSemanticaExp(oIzq,oDer,oper)
            if res != None:
                self.quadList.append([oper,oIzq,oDer,"t" + self.contQuadTemporales])
                self.insertarValorTipo("t" + self.contQuadTemporales,res)
                self.contQuadTemporales = self.contQuadTemporales + 1
            else:
                print ("Semantic error: line " + str(self.getCurrentToken().line) + ":" + str(self.getCurrentToken().column) + " Tipos de operadores no compatibles" )
                self._syntaxErrors = self._syntaxErrors + 1
                return
        else:
            self.pOper.append(oper)


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
            self.state = 156
            self.p1()
            self.state = 157
            self.p2()
            self.state = 158
            self.p3()
            self.state = 159
            self.principal()
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
            self.state = 165
            token = self._input.LA(1)
            if token in [coffParser.CLASE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 161
                self.clases()
                self.state = 162
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

        def funcion(self):
            return self.getTypedRuleContext(coffParser.FuncionContext,0)


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
            self.state = 171
            token = self._input.LA(1)
            if token in [coffParser.FUNCION]:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                ##########################
                self.metodoTof = 0
                ##########################
                self.funcion()
                self.state = 168
                self.p2()

            elif token in [coffParser.ENTERO, coffParser.DECIMAL, coffParser.TEXTO, coffParser.PRINCIPAL, coffParser.ID]:
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

        def variables(self):
            return self.getTypedRuleContext(coffParser.VariablesContext,0)


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
            self.state = 177
            token = self._input.LA(1)
            if token in [coffParser.ENTERO, coffParser.DECIMAL, coffParser.TEXTO, coffParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 173
                
                #####################################
                self.globalTof = 1
                self.variables()
                self.globalTof = 0
                #####################################

                self.state = 174
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
            self.state = 179

           
            self.match(coffParser.PRINCIPAL)

  
            
            self.state = 180
            self.pr1()
            self.state = 181

            ########################################
            self.idVariableActual = str(self.getCurrentToken().text)
            if (self.idVariableActual, 0) in self.dirProcs or (self.idVariableActual, True) in self.dirProcs:
                    print("Error, ya habia una funcion declarada con el nombre: "+self.idVariableActual)
                    sys.exit()
                    return
            


            self.scopeProcs = self.scopeProcs + 1
            self.dirProcs[self.idVariableActual,0] = [self.scopeProcs,self.tipoVariableActual]
            #print("")
            #for keys,values in self.dirProcs.items():
            #    print(str(keys))
            #    print(str(values))
            #print("")
            #########################################

            self.match(coffParser.ID)
            self.state = 182
            self.parametros()
            self.state = 183
            self.match(coffParser.BIZQ)
            self.state = 184
            self.pr2()
            self.state = 185
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
            self.state = 189
            token = self._input.LA(1)
            if token in [coffParser.ENTERO, coffParser.DECIMAL, coffParser.TEXTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 187
                self.pr11()

            elif token in [coffParser.VACIO]:
                self.enterOuterAlt(localctx, 2)
                self.state = 188
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
            self.state = 191
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
            self.state = 193

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
            self.state = 195
            self.pr21()
            self.state = 196
            self.pr22()
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
        self.enterRule(localctx, 18, self.RULE_pr21)
        try:
            self.state = 202
            token = self._input.LA(1)
            if token in [coffParser.IMPRIMIR, coffParser.LEER, coffParser.MIENTRAS, coffParser.ENTERO, coffParser.DECIMAL, coffParser.TEXTO, coffParser.SI, coffParser.EJEC, coffParser.ASIGNA, coffParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 198
                self.estatuto()
                self.state = 199
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
        self.enterRule(localctx, 20, self.RULE_pr22)
        try:
            self.state = 209
            token = self._input.LA(1)
            if token in [coffParser.RETORNA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 204
                self.match(coffParser.RETORNA)
                self.state = 205
                self.expresion()
                self.state = 206
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
        self.enterRule(localctx, 22, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            ############################################
            self.tipoVariableActual = str(self.getCurrentToken().text)
            if not((self.tipoVariableActual, False) in self.dirProcs) and not(self.tipoVariableActual == "entero" or self.tipoVariableActual == "decimal" or self.tipoVariableActual == "texto"):
                print("Error, tipo: "+self.tipoVariableActual+" no existe")
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
        self.enterRule(localctx, 24, self.RULE_variables)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.tipo()
            self.state = 214
            self.v1()
            self.state = 215
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
        self.enterRule(localctx, 26, self.RULE_v1)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            ########################################################
            self.idVariableActual = str(self.getCurrentToken().text)


            if self.globalTof:
                if (self.idVariableActual, 0) in self.tablaVariables:
                    print("Error, la variable "+ self.idVariableActual+" ya habia sido declarada")
                    sys.exit()
                    return
                else:
                    self.tablaVariables[self.idVariableActual,0] = self.tipoVariableActual
            else:
                if (self.idVariableActual, self.scopeProcs) in self.tablaVariables:
                    print("Error, la variable "+ self.idVariableActual+" ya habia sido declarada")
                    sys.exit()
                    return
                else:
                    self.tablaVariables[self.idVariableActual,self.scopeProcs] = self.tipoVariableActual

           
            ########################################################

            self.match(coffParser.ID)
            self.state = 218
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
        self.enterRule(localctx, 28, self.RULE_v2)
        try:
            self.state = 230
            token = self._input.LA(1)
            if token in [coffParser.CIZQ]:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.match(coffParser.CIZQ)
                self.state = 221
                self.match(coffParser.CTEENT)
                self.state = 222
                self.match(coffParser.CDER)
                self.state = 223
                self.v4()

            elif token in [coffParser.IGUAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 224
                self.match(coffParser.IGUAL)
                self.state = 225
                self.valordeclaracion()
                self.state = 226
                self.v6()

            elif token in [coffParser.COMA]:
                self.enterOuterAlt(localctx, 3)
                self.state = 228
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
        self.enterRule(localctx, 30, self.RULE_v3)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(coffParser.COMA)
            self.state = 233
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
        self.enterRule(localctx, 32, self.RULE_v4)
        try:
            self.state = 243
            token = self._input.LA(1)
            if token in [coffParser.COMA, coffParser.PUNTOYCOMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 235
                self.v6()

            elif token in [coffParser.IGUAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 236
                self.match(coffParser.IGUAL)
                self.state = 237
                self.match(coffParser.CIZQ)
                self.state = 238
                self.valordeclaracion()
                self.state = 239
                self.v5()
                self.state = 240
                self.match(coffParser.CDER)
                self.state = 241
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
        self.enterRule(localctx, 34, self.RULE_v5)
        try:
            self.state = 250
            token = self._input.LA(1)
            if token in [coffParser.COMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 245
                self.match(coffParser.COMA)
                self.state = 246
                self.valordeclaracion()
                self.state = 247
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
        self.enterRule(localctx, 36, self.RULE_v6)
        try:
            self.state = 254
            token = self._input.LA(1)
            if token in [coffParser.COMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 252
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
        self.enterRule(localctx, 38, self.RULE_valordeclaracion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << coffParser.CTEENT) | (1 << coffParser.CTEDEC) | (1 << coffParser.CTETEXTO))) != 0)):
                self._errHandler.recoverInline(self)
            else:

                if _la in [coffParser.CTEENT]:
                    self.insertarValorTipo(self.getCurrentToken().text, 'ENTERO')

                if _la in [coffParser.CTEDEC]:
                    self.insertarValorTipo(self.getCurrentToken().text, 'DECIMAL')
                
                if _la in [coffParser.CTETEXTO]:
                    self.insertarValorTipo(self.getCurrentToken().text, 'TEXTO')

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




    def valor(self):

        localctx = coffParser.ValorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_valor)
        try:
            self.state = 261
            token = self._input.LA(1)

    #############################################################################################
            
            if token in [coffParser.CTEENT, coffParser.CTEDEC, coffParser.CTETEXTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 258
                self.valordeclaracion()

            elif token in [coffParser.ID]:
                self.ejecToken = str(self.getCurrentToken().text)   
                #print(self.ejecToken)        
                self.enterOuterAlt(localctx, 2)
                #print(self.scopeProcs)

                self.insertarValorTipo(self.ejecToken,self.tablaVariables[self.ejecToken,self.scopeProcs])

                self.state = 259
                self.match(coffParser.ID)
                self.state = 260
                self.va1()
                

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

        def expresion(self):
            return self.getTypedRuleContext(coffParser.ExpresionContext,0)


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

        def va3(self):
            return self.getTypedRuleContext(coffParser.Va3Context,0)


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
        self.enterRule(localctx, 42, self.RULE_va1)
        try:
            self.state = 274
            token = self._input.LA(1)




            
            if token in [coffParser.PUNTO]:
                #self.idVariableActual = self.ejecToken  
                #print(self.idVariableActual) 

                #self.checkIfVariableExists()  
                self.enterOuterAlt(localctx, 1)
                self.state = 263
                self.va4()

            elif token in [coffParser.PIZQ]:
                
                self.enterOuterAlt(localctx, 2)
                self.state = 264
                self.match(coffParser.PIZQ)
                self.idVariableActual = self.ejecToken  
                if (self.ejecToken, 0) not in self.dirProcs:
                    print("Error, la funcion "+self.ejecToken+" no ha sido declarada")
                    sys.exit()
                self.state = 265
                self.expresion()
                self.state = 266
                self.va2()
                self.state = 267
                self.match(coffParser.PDER)

            elif token in [coffParser.CIZQ]:
                self.enterOuterAlt(localctx, 3)
                self.state = 269
                self.match(coffParser.CIZQ)
                self.state = 270
                self.match(coffParser.CTEENT)
                self.state = 271
                self.match(coffParser.CDER)
                self.state = 272
                self.va3()

            elif token in [coffParser.PDER, coffParser.CDER, coffParser.SUMA, coffParser.RESTA, coffParser.DIV, coffParser.MULT, coffParser.IGUALQUE, coffParser.MENQUE, coffParser.MAYQUE, coffParser.MAYIGUALQUE, coffParser.MENIGUALQUE, coffParser.DIF, coffParser.CONDICIONO, coffParser.CONDICIONY, coffParser.COMA, coffParser.PUNTOYCOMA]:
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

    class Va2Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.Va2Context, self).__init__(parent, invokingState)
            self.parser = parser

        def COMA(self):
            return self.getToken(coffParser.COMA, 0)

        def expresion(self):
            return self.getTypedRuleContext(coffParser.ExpresionContext,0)


        def va2(self):
            return self.getTypedRuleContext(coffParser.Va2Context,0)


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
        self.enterRule(localctx, 44, self.RULE_va2)
        try:
            self.state = 281
            token = self._input.LA(1)
            if token in [coffParser.COMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                self.match(coffParser.COMA)
                self.state = 277
                self.expresion()
                self.state = 278
                self.va2()

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

        def va4(self):
            return self.getTypedRuleContext(coffParser.Va4Context,0)


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
        self.enterRule(localctx, 46, self.RULE_va3)
        try:
            self.state = 285
            token = self._input.LA(1)
            if token in [coffParser.PUNTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 283
                self.va4()

            elif token in [coffParser.PDER, coffParser.CDER, coffParser.SUMA, coffParser.RESTA, coffParser.DIV, coffParser.MULT, coffParser.IGUALQUE, coffParser.MENQUE, coffParser.MAYQUE, coffParser.MAYIGUALQUE, coffParser.MENIGUALQUE, coffParser.DIF, coffParser.CONDICIONO, coffParser.CONDICIONY, coffParser.COMA, coffParser.PUNTOYCOMA]:
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
        self.enterRule(localctx, 48, self.RULE_va4)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.match(coffParser.PUNTO)
            self.state = 288
            self.tokenActual = str(self.getCurrentToken().text)
            self.lookForMethodClass()
            #self.checkIfVariableExists()
            self.match(coffParser.ID)
            self.state = 289
            self.va5()
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

        def expresion(self):
            return self.getTypedRuleContext(coffParser.ExpresionContext,0)


        def va2(self):
            return self.getTypedRuleContext(coffParser.Va2Context,0)


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
        self.enterRule(localctx, 50, self.RULE_va5)
        try:
            self.state = 297
            token = self._input.LA(1)
            if token in [coffParser.PIZQ]:
                self.enterOuterAlt(localctx, 1)
                self.state = 291
                self.match(coffParser.PIZQ)
                self.state = 292
                self.expresion()
                self.state = 293
                self.va2()
                self.state = 294
                self.match(coffParser.PDER)

            elif token in [coffParser.PDER, coffParser.CDER, coffParser.SUMA, coffParser.RESTA, coffParser.DIV, coffParser.MULT, coffParser.IGUALQUE, coffParser.MENQUE, coffParser.MAYQUE, coffParser.MAYIGUALQUE, coffParser.MENIGUALQUE, coffParser.DIF, coffParser.CONDICIONO, coffParser.CONDICIONY, coffParser.COMA, coffParser.PUNTOYCOMA]:
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
        self.enterRule(localctx, 52, self.RULE_tiposimple)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
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
        self.enterRule(localctx, 54, self.RULE_parametros)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.match(coffParser.PIZQ)
            self.state = 302
            self.pa1()
            self.state = 303
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
        self.enterRule(localctx, 56, self.RULE_pa1)
        try:
            self.state = 307
            token = self._input.LA(1)
            if token in [coffParser.ENTERO, coffParser.DECIMAL, coffParser.TEXTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 305
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
        self.enterRule(localctx, 58, self.RULE_pa11)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.tiposimple()
            self.state = 310
            self.pa2()
            self.state = 311

            ##########################################################
            self.idVariableActual = str(self.getCurrentToken().text)
            self.tablaVariables[self.idVariableActual,self.scopeProcs] = self.tipoVariableActual 

            ########################################################
            
            self.match(coffParser.ID)
            self.state = 312
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
        self.enterRule(localctx, 60, self.RULE_pa2)
        try:
            self.state = 316
            token = self._input.LA(1)
            if token in [coffParser.AMP]:
                self.enterOuterAlt(localctx, 1)
                self.state = 314
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
        self.enterRule(localctx, 62, self.RULE_pa3)
        try:
            self.state = 321
            token = self._input.LA(1)
            if token in [coffParser.COMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                self.match(coffParser.COMA)
                self.state = 319
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




    def llamarfunmet(self):

        localctx = coffParser.LlamarfunmetContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_llamarfunmet)
        try:
            self.ejecToken = str(self.getCurrentToken().text)
              
            self.enterOuterAlt(localctx, 1)
            self.state = 323

            

            #########################################

            #if not((self.idVariableActual, True)  in self.dirProcs or (self.idVariableActual, False)  in self.dirProcs):
            #    print(self.scopeProcs)
            #    print("Error, la variable "+self.idVariableActual+" no ha sido declarada")
            #    sys.exit()
            #    return


           
            

            self.match(coffParser.ID)
            self.state = 324
            self.ll1()

            self.state = 325
            self.match(coffParser.PIZQ)
            self.state = 326
            self.ll2()
            self.state = 327
            self.match(coffParser.PDER)
            self.state = 328
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


    def lookForMethodClass(self):  
        self.lookForObjectClassObjectType = self.tablaVariables[self.ejecToken,self.scopeProcs] #contiene el tipo del objeto
        self.lookForObjectClassClassID = self.dirProcs[self.lookForObjectClassObjectType,0][0]; #contiene el id de la clase
        if(self.tokenActual, self.lookForObjectClassClassID) not in self.dirProcs: #tokenActual contiene el nombre del metodo
            print("Error, el metodo "+self.tokenActual+" no es compatible con la clase de "+self.ejecToken)
            sys.exit()


    def ll1(self):

        localctx = coffParser.Ll1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_ll1)
        try:

            self.tokenActual = str(self.getCurrentToken().text)
           
            #print("")
            #for keys,values in self.tablaVariables.items():
            #    print(str(keys[1]))
            #    #print(str(values))
            #print("")



            if self.tokenActual == '(':
                if (self.ejecToken, 0) not in self.dirProcs:
                    print("Error, la funcion "+self.ejecToken+" no ha sido declarada")
                    sys.exit()
            elif self.tokenActual == '.':  
                self.idVariableActual = self.ejecToken
                self.checkIfVariableExists()
                #if (self.ejecToken, self.scopeProcs)  not in self.tablaVariables:
                #    print("Error, la variable "+self.ejecToken+" no ha sido declarada")
                #    sys.exit()



            self.state = 333

            token = self._input.LA(1)
            

            if token in [coffParser.PUNTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 330
                self.match(coffParser.PUNTO)
                self.state = 331
                #######################
                self.tokenActual = str(self.getCurrentToken().text)
                self.lookForMethodClass()
                ##############
                self.match(coffParser.ID)

            elif token in [coffParser.PIZQ]:
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




    def ll2(self):

        localctx = coffParser.Ll2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_ll2)
        try:
            self.state = 339
            token = self._input.LA(1)
            if token in [coffParser.PIZQ, coffParser.SUMA, coffParser.RESTA, coffParser.ID, coffParser.CTEENT, coffParser.CTEDEC, coffParser.CTETEXTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 335
                self.expresion()
                self.state = 336
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
        self.enterRule(localctx, 70, self.RULE_ll3)
        try:
            self.state = 346
            token = self._input.LA(1)
            if token in [coffParser.COMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 341
                self.match(coffParser.COMA)
                self.state = 342
                self.expresion()
                self.state = 343
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
        self.enterRule(localctx, 72, self.RULE_expresion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.declaracion()
            self.state = 349
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
        self.enterRule(localctx, 74, self.RULE_ex1)
        try:
            self.state = 356
            token = self._input.LA(1)
            if token in [coffParser.CONDICIONO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 351
                self.match(coffParser.CONDICIONO)
                self.state = 352
                self.expresion()

            elif token in [coffParser.CONDICIONY]:
                self.enterOuterAlt(localctx, 2)
                self.state = 353
                self.match(coffParser.CONDICIONY)
                self.state = 354
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
        self.enterRule(localctx, 76, self.RULE_declaracion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.exp()
            self.state = 359
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
        self.enterRule(localctx, 78, self.RULE_de1)
        try:
            self.state = 365
            token = self._input.LA(1)
            if token in [coffParser.IGUALQUE, coffParser.MENQUE, coffParser.MAYQUE, coffParser.MAYIGUALQUE, coffParser.MENIGUALQUE, coffParser.DIF]:
                self.enterOuterAlt(localctx, 1)
                self.state = 361
                self.de2()
                self.state = 362
                self.exp()

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
        self.enterRule(localctx, 80, self.RULE_de2)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
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
        self.enterRule(localctx, 82, self.RULE_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self.termino()
            self.state = 370
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
        self.enterRule(localctx, 84, self.RULE_exp1)
        try:
            self.state = 377
            token = self._input.LA(1)
            if token in [coffParser.RESTA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 372
                self.match(coffParser.RESTA)
                self.state = 373
                self.exp()

            elif token in [coffParser.SUMA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 374
                self.match(coffParser.SUMA)
                self.state = 375
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
        self.enterRule(localctx, 86, self.RULE_termino)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 379
            self.factor()
            self.state = 380
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
        self.enterRule(localctx, 88, self.RULE_t1)
        try:
            self.state = 387
            token = self._input.LA(1)
            if token in [coffParser.DIV]:
                self.enterOuterAlt(localctx, 1)
                self.state = 382
                self.match(coffParser.DIV)
                self.state = 383
                self.termino()

            elif token in [coffParser.MULT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 384
                self.match(coffParser.MULT)
                self.state = 385
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
        self.enterRule(localctx, 90, self.RULE_factor)
        try:
            self.state = 396
            token = self._input.LA(1)
            if token in [coffParser.SUMA, coffParser.RESTA, coffParser.ID, coffParser.CTEENT, coffParser.CTEDEC, coffParser.CTETEXTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 389
                self.f1()
                self.state = 390
                self.valor()

            elif token in [coffParser.PIZQ]:
                self.enterOuterAlt(localctx, 2)
                self.state = 392
                self.match(coffParser.PIZQ)
                self.state = 393
                self.expresion()
                self.state = 394
                self.match(coffParser.PDER)

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
        self.enterRule(localctx, 92, self.RULE_f1)
        try:
            self.state = 401
            token = self._input.LA(1)
            if token in [coffParser.RESTA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 398
                self.match(coffParser.RESTA)
                #Si entra por primera vez la expresion y es negativo
                tofFactor = 1

            elif token in [coffParser.SUMA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 399
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
        self.enterRule(localctx, 94, self.RULE_funcion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self.match(coffParser.FUNCION)
            self.state = 404
            self.fun1()
            self.state = 405

            ########################################
            self.scopeProcs = self.scopeProcs + 1
            self.idVariableActual = str(self.getCurrentToken().text)

            if self.metodoTof:
                self.dirProcs[self.idVariableActual,self.claseRef] = [self.scopeProcs,self.tipoVariableActual]
            else:
                self.dirProcs[self.idVariableActual,0] = [self.scopeProcs,self.tipoVariableActual]
                
            
            
            #########################################

            self.match(coffParser.ID)
            self.state = 406
            self.parametros()
            self.state = 407
            self.match(coffParser.BIZQ)
            self.state = 408
            self.fun2()
            self.state = 409
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
        self.enterRule(localctx, 96, self.RULE_fun1)
        try:
            self.state = 413
            token = self._input.LA(1)
            if token in [coffParser.ENTERO, coffParser.DECIMAL, coffParser.TEXTO, coffParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 411
                self.fun11()

            elif token in [coffParser.VACIO]:
                self.enterOuterAlt(localctx, 2)
                self.state = 412
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
        self.enterRule(localctx, 98, self.RULE_fun11)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 415
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
        self.enterRule(localctx, 100, self.RULE_fun12)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417

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

    class Fun2Context(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(coffParser.Fun2Context, self).__init__(parent, invokingState)
            self.parser = parser

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
        self.enterRule(localctx, 102, self.RULE_fun2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 419
            self.fun21()
            self.state = 420
            self.fun22()
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
        self.enterRule(localctx, 104, self.RULE_fun21)
        try:
            self.state = 426
            token = self._input.LA(1)
            if token in [coffParser.IMPRIMIR, coffParser.LEER, coffParser.MIENTRAS, coffParser.ENTERO, coffParser.DECIMAL, coffParser.TEXTO, coffParser.SI, coffParser.EJEC, coffParser.ASIGNA, coffParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 422
                self.estatuto()
                self.state = 423
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
        self.enterRule(localctx, 106, self.RULE_fun22)
        try:
            self.state = 433
            token = self._input.LA(1)
            if token in [coffParser.RETORNA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 428
                self.match(coffParser.RETORNA)
                self.state = 429
                self.expresion()
                self.state = 430
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
        self.enterRule(localctx, 108, self.RULE_bloque)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 435
            self.match(coffParser.BIZQ)
            self.state = 436
            self.b1()
            self.state = 437
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
        self.enterRule(localctx, 110, self.RULE_b1)
        try:
            self.state = 443
            token = self._input.LA(1)
            if token in [coffParser.IMPRIMIR, coffParser.LEER, coffParser.MIENTRAS, coffParser.ENTERO, coffParser.DECIMAL, coffParser.TEXTO, coffParser.SI, coffParser.EJEC, coffParser.ASIGNA, coffParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 439
                self.estatuto()
                self.state = 440
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
        self.enterRule(localctx, 112, self.RULE_bloquesimple)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 445
            self.match(coffParser.BIZQ)
            self.state = 446
            self.bs1()
            self.state = 447
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
        self.enterRule(localctx, 114, self.RULE_bs1)
        try:
            self.state = 453
            token = self._input.LA(1)
            if token in [coffParser.IMPRIMIR, coffParser.LEER, coffParser.MIENTRAS, coffParser.SI, coffParser.EJEC, coffParser.ASIGNA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 449
                self.estatutosimple()
                self.state = 450
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

    def checkIfVariableExists(self):
        if (self.idVariableActual, self.scopeProcs)  not in self.tablaVariables:
            if (self.idVariableActual, 0)  not in self.tablaVariables:
                print("Error, la variable "+self.idVariableActual+" no ha sido declarada")
                sys.exit()


    def asignacion(self):

        localctx = coffParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 455

            self.idVariableActual = str(self.getCurrentToken().text)
            self.ejecToken = self.idVariableActual
            
            #print("")
            #for keys,values in self.tablaVariables.items():
            #    print(str(keys[1]))
            #    #print(str(values))
            #print("")

            self.checkIfVariableExists()




            self.match(coffParser.ID)
            self.state = 456
            self.a1()
            self.state = 457
            self.a2()
            self.state = 458
            self.match(coffParser.IGUAL)
            self.state = 459
            self.expresion()
            self.state = 460
            self.match(coffParser.PUNTOYCOMA)
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


    def checkIfAttributeBelongs(self):
        #idVariableActual contiene el atributo
        #ejecToken contiene el id de la instancia de la clase
        self.ejecToken= self.tablaVariables[self.ejecToken,self.scopeProcs]
        self.checkifAttributeBelongsClassID = self.dirProcs[self.ejecToken, 0][0] 
        if (self.idVariableActual, self.checkifAttributeBelongsClassID)  not in self.tablaVariables:
                print("Error, el atributo "+self.idVariableActual+" no pertenece a la clase "+self.ejecToken)
                sys.exit()


    def a1(self):

        localctx = coffParser.A1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_a1)
        try:
            self.state = 465
            token = self._input.LA(1)
            if token in [coffParser.PUNTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 462
                self.match(coffParser.PUNTO)
                self.idVariableActual = str(self.getCurrentToken().text)

                self.checkIfAttributeBelongs()
                self.state = 463
                self.match(coffParser.ID)
            elif token in [coffParser.CIZQ, coffParser.IGUAL]:

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
        self.enterRule(localctx, 120, self.RULE_a2)
        try:
            self.state = 472
            token = self._input.LA(1)
            if token in [coffParser.CIZQ]:
                self.enterOuterAlt(localctx, 1)
                self.state = 467
                self.match(coffParser.CIZQ)
                self.state = 468
                self.expresion()
                self.state = 469
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
        self.enterRule(localctx, 122, self.RULE_mientras)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
            self.match(coffParser.MIENTRAS)
            self.state = 475
            self.match(coffParser.PIZQ)
            self.state = 476
            self.expresion()
            self.state = 477
            self.match(coffParser.PDER)
            self.state = 478
            self.bloquesimple()
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

        def variables(self):
            return self.getTypedRuleContext(coffParser.VariablesContext,0)


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
        self.enterRule(localctx, 124, self.RULE_estatuto)
        try:
            self.state = 489
            token = self._input.LA(1)
            if token in [coffParser.ENTERO, coffParser.DECIMAL, coffParser.TEXTO, coffParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 480
                self.variables()

            elif token in [coffParser.EJEC]:
                self.enterOuterAlt(localctx, 2)
                self.state = 481
                self.match(coffParser.EJEC)
                self.state = 482
                self.llamarfunmet()

            elif token in [coffParser.ASIGNA]:
                self.enterOuterAlt(localctx, 3)
                self.state = 483
                self.match(coffParser.ASIGNA)
                self.state = 484
                self.asignacion()

            elif token in [coffParser.MIENTRAS]:
                self.enterOuterAlt(localctx, 4)
                self.state = 485
                self.mientras()

            elif token in [coffParser.SI]:
                self.enterOuterAlt(localctx, 5)
                self.state = 486
                self.si()

            elif token in [coffParser.IMPRIMIR]:
                self.enterOuterAlt(localctx, 6)
                self.state = 487
                self.escritura()

            elif token in [coffParser.LEER]:
                self.enterOuterAlt(localctx, 7)
                self.state = 488
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
        self.enterRule(localctx, 126, self.RULE_estatutosimple)
        try:
            self.state = 499
            token = self._input.LA(1)
            if token in [coffParser.EJEC]:
                self.enterOuterAlt(localctx, 1)
                self.state = 491
                self.match(coffParser.EJEC)
                self.state = 492
                self.llamarfunmet()

            elif token in [coffParser.ASIGNA]:
                self.enterOuterAlt(localctx, 2)
                self.state = 493
                self.match(coffParser.ASIGNA)
                self.state = 494
                self.asignacion()

            elif token in [coffParser.MIENTRAS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 495
                self.mientras()

            elif token in [coffParser.SI]:
                self.enterOuterAlt(localctx, 4)
                self.state = 496
                self.si()

            elif token in [coffParser.IMPRIMIR]:
                self.enterOuterAlt(localctx, 5)
                self.state = 497
                self.escritura()

            elif token in [coffParser.LEER]:
                self.enterOuterAlt(localctx, 6)
                self.state = 498
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
        self.enterRule(localctx, 128, self.RULE_escritura)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 501
            self.match(coffParser.IMPRIMIR)
            self.state = 502
            self.match(coffParser.PIZQ)
            self.state = 503
            self.expresion()
            self.state = 504
            self.e1()
            self.state = 505
            self.match(coffParser.PDER)
            self.state = 506
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
        self.enterRule(localctx, 130, self.RULE_e1)
        try:
            self.state = 513
            token = self._input.LA(1)
            if token in [coffParser.COMA]:
                self.enterOuterAlt(localctx, 1)
                self.state = 508
                self.match(coffParser.COMA)
                self.state = 509
                self.expresion()
                self.state = 510
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
        self.enterRule(localctx, 132, self.RULE_lectura)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 515
            self.match(coffParser.LEER)
            self.state = 516
            self.match(coffParser.PIZQ)
            self.state = 517
            self.idVariableActual = str(self.getCurrentToken().text)
            self.checkIfVariableExists()
            
            self.match(coffParser.ID)
            self.state = 518
            self.l1()
            self.state = 519
            self.l2()
            self.state = 520
            self.match(coffParser.PDER)
            self.state = 521
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
        self.enterRule(localctx, 134, self.RULE_l1)
        try:
            self.state = 526
            token = self._input.LA(1)
            if token in [coffParser.PUNTO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 523
                self.match(coffParser.PUNTO)
                self.state = 524
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
        self.enterRule(localctx, 136, self.RULE_l2)
        try:
            self.state = 533
            token = self._input.LA(1)
            if token in [coffParser.CIZQ]:
                self.enterOuterAlt(localctx, 1)
                self.state = 528
                self.match(coffParser.CIZQ)
                self.state = 529
                self.expresion()
                self.state = 530
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
        self.enterRule(localctx, 138, self.RULE_si)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 535
            self.match(coffParser.SI)
            self.state = 536
            self.match(coffParser.PIZQ)
            self.state = 537
            self.expresion()
            self.state = 538
            self.match(coffParser.PDER)
            self.state = 539
            self.bloque()
            self.state = 540
            self.si1()
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
        self.enterRule(localctx, 140, self.RULE_si1)
        try:
            self.state = 545
            token = self._input.LA(1)
            if token in [coffParser.O]:
                self.enterOuterAlt(localctx, 1)
                self.state = 542
                self.match(coffParser.O)
                self.state = 543
                self.bloque()

            elif token in [coffParser.IMPRIMIR, coffParser.LEER, coffParser.MIENTRAS, coffParser.ENTERO, coffParser.DECIMAL, coffParser.TEXTO, coffParser.RETORNA, coffParser.SI, coffParser.EJEC, coffParser.ASIGNA, coffParser.BDER, coffParser.ID]:
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
        self.enterRule(localctx, 142, self.RULE_clases)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 547
            self.match(coffParser.CLASE)

            ########################################
            self.scopeProcs = self.scopeProcs + 1
            self.claseRef = self.scopeProcs
            self.dirProcs[str(self.getCurrentToken().text),0] = [self.scopeProcs,""]
            
            #########################################

            self.state = 548
            self.match(coffParser.ID)
            self.state = 549
            self.cl1()
            self.state = 550
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
        self.enterRule(localctx, 144, self.RULE_cl1)
        try:
            self.state = 555
            token = self._input.LA(1)
            if token in [coffParser.EXTIENDE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 552
                self.match(coffParser.EXTIENDE)
                self.state = 553
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
        self.enterRule(localctx, 146, self.RULE_cl2)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 557
            self.match(coffParser.BIZQ)
            self.state = 558
            self.atributos()
            self.state = 559
            self.metodos()
            self.state = 560
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
        self.enterRule(localctx, 148, self.RULE_atributos)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 562
            self.match(coffParser.ATRIBUTOS)
            self.state = 563
            self.match(coffParser.DOSPUNTOS)
            self.state = 564
            self.atr1()
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
        self.enterRule(localctx, 150, self.RULE_atr1)
        try:
            self.state = 570
            token = self._input.LA(1)
            if token in [coffParser.ENTERO, coffParser.DECIMAL, coffParser.TEXTO, coffParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 566
                self.variables()
                self.state = 567
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
        self.enterRule(localctx, 152, self.RULE_metodos)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 572
            self.match(coffParser.METODOS)
            self.state = 573
            self.match(coffParser.DOSPUNTOS)
            self.state = 574
            self.met1()
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
        self.enterRule(localctx, 154, self.RULE_met1)
        try:
            self.state = 580
            token = self._input.LA(1)
            if token in [coffParser.FUNCION]:
                self.enterOuterAlt(localctx, 1)
                self.state = 576
                self.funcion()
                self.state = 577
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




