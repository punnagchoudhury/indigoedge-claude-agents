#!/usr/bin/env python3
"""
Build the IndigoEdge branded pandoc reference template.

Usage:
    python build_ie_template.py [output.docx]      # default: IndigoEdge_Dossier_Template.docx

Then style any dossier with:
    pandoc dossier.md --reference-doc=IndigoEdge_Dossier_Template.docx -o dossier.docx

Produces a clean-professional Word style template (no cover band) in IndigoEdge brand
colours: deep indigo #3E3B95 (title, headings, table headers) and teal #00A4E4
(sub-headings, hyperlinks, section rule), with a branded page-number footer.
"""
import subprocess, sys, os, re, tempfile, zipfile, shutil

OUT = sys.argv[1] if len(sys.argv) > 1 else "IndigoEdge_Dossier_Template.docx"
work = tempfile.mkdtemp(); ref = os.path.join(work, "ref.docx"); up = os.path.join(work, "u")
subprocess.run(f'pandoc --print-default-data-file reference.docx > "{ref}"', shell=True, check=True)
with zipfile.ZipFile(ref) as z: z.extractall(up)
R = lambda p: open(os.path.join(up, p)).read()
W = lambda p, s: open(os.path.join(up, p), 'w').write(s)

x = R('word/styles.xml')
blk = lambda sid: re.compile(r'(<w:style [^>]*w:styleId="' + sid + r'".*?</w:style>)', re.S)
def setcol(x, sid, c):
    return blk(sid).sub(lambda m: re.sub(r'<w:color [^>]*/>', f'<w:color w:val="{c}" />', m.group(1), 1), x, 1)
for sid, c in [('Title','3E3B95'),('Heading1','3E3B95'),('Heading2','3E3B95'),('Heading3','00A4E4'),('Hyperlink','00A4E4')]:
    x = setcol(x, sid, c)
x = blk('Heading1').sub(lambda m: m.group(1).replace('<w:keepLines />',
    '<w:keepLines />\n      <w:pBdr><w:bottom w:val="single" w:sz="12" w:space="4" w:color="00A4E4" /></w:pBdr>', 1), x, 1)
TABLE = ('<w:style w:type="table" w:default="1" w:styleId="Table"><w:name w:val="Table" />'
 '<w:basedOn w:val="TableNormal" /><w:semiHidden /><w:unhideWhenUsed /><w:qFormat />'
 '<w:tblPr><w:tblInd w:w="0" w:type="dxa" />'
 '<w:tblBorders><w:bottom w:val="single" w:sz="4" w:color="D9D9D9" />'
 '<w:insideH w:val="single" w:sz="4" w:color="E8E8E8" /></w:tblBorders>'
 '<w:tblCellMar><w:top w:w="40" w:type="dxa" /><w:left w:w="108" w:type="dxa" />'
 '<w:bottom w:w="40" w:type="dxa" /><w:right w:w="108" w:type="dxa" /></w:tblCellMar></w:tblPr>'
 '<w:tblStylePr w:type="firstRow"><w:rPr><w:b /><w:color w:val="FFFFFF" /></w:rPr>'
 '<w:tcPr><w:shd w:val="clear" w:color="auto" w:fill="3E3B95" /><w:vAlign w:val="center" />'
 '<w:tcBorders><w:bottom w:val="single" w:sz="4" w:color="3E3B95" /></w:tcBorders></w:tcPr></w:tblStylePr></w:style>')
x = blk('Table').sub(lambda m: TABLE, x, 1)
W('word/styles.xml', x)

W('word/footer1.xml', '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
 '<w:ftr xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" '
 'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
 '<w:p><w:pPr><w:pBdr><w:top w:val="single" w:sz="4" w:space="6" w:color="00A4E4" /></w:pBdr>'
 '<w:jc w:val="center" /></w:pPr>'
 '<w:r><w:rPr><w:color w:val="3E3B95" /><w:sz w:val="16" /></w:rPr>'
 '<w:t xml:space="preserve">IndigoEdge   &#183;   Confidential   &#183;   Page </w:t></w:r>'
 '<w:r><w:rPr><w:color w:val="3E3B95" /><w:sz w:val="16" /></w:rPr><w:fldChar w:fldCharType="begin" /></w:r>'
 '<w:r><w:rPr><w:color w:val="3E3B95" /><w:sz w:val="16" /></w:rPr><w:instrText xml:space="preserve"> PAGE </w:instrText></w:r>'
 '<w:r><w:rPr><w:color w:val="3E3B95" /><w:sz w:val="16" /></w:rPr><w:fldChar w:fldCharType="end" /></w:r></w:p></w:ftr>')

r = R('word/_rels/document.xml.rels')
if 'footer1.xml' not in r:
    W('word/_rels/document.xml.rels', r.replace('</Relationships>',
      '<Relationship Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/footer" Id="rId40" Target="footer1.xml" /></Relationships>'))
c = R('[Content_Types].xml')
adds = ''
if 'Extension="png"' not in c:
    adds += '<Default Extension="png" ContentType="image/png" />'      # so embedded charts validate
if 'footer1.xml' not in c:
    adds += '<Override PartName="/word/footer1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml" />'
if adds:
    W('[Content_Types].xml', c.replace('</Types>', adds + '</Types>'))
d = R('word/document.xml')
W('word/document.xml', d.replace('<w:sectPr />',
  '<w:sectPr><w:footerReference w:type="default" r:id="rId40" />'
  '<w:pgSz w:w="11906" w:h="16838" />'
  '<w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440" w:header="720" w:footer="600" w:gutter="0" /></w:sectPr>'))

if os.path.exists(OUT): os.remove(OUT)
with zipfile.ZipFile(OUT, 'w', zipfile.ZIP_DEFLATED) as z:
    for root, _, files in os.walk(up):
        for fn in files:
            fp = os.path.join(root, fn); z.write(fp, os.path.relpath(fp, up))
shutil.rmtree(work)
print("wrote", OUT)
