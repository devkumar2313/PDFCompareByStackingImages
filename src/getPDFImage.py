import fitz  # PyMuPDF
import os

def extract_pdf_pages(pdf_path, output_prefix="page", page_num=0):
    """
    PDFファイルから指定されたページを画像として抽出する関数
    Extract specified page from PDF as image
    """
    try:
        # PDFを開く
        doc = fitz.open(pdf_path)
        
        # 指定されたページを取得（デフォルトは最初のページ）
        if page_num >= len(doc):
            page_num = 0
            
        page = doc[page_num]
        
        # ページを画像として取得
        pix = page.get_pixmap()
        
        # 画像を保存
        output_filename = f"{output_prefix}_{page_num + 1}.png"
        pix.save(output_filename)
        
        print(f"ページを画像として保存しました: {output_filename}")
        print(f"Page saved as image: {output_filename}")
        
        doc.close()
        return output_filename
        
    except Exception as e:
        print(f"エラー: PDFの処理中に問題が発生しました: {e}")
        print(f"Error: Problem occurred while processing PDF: {e}")
        return None

if __name__ == "__main__":
    # スクリプトの使用例
    pdf_file = "sample.pdf"
    if os.path.exists(pdf_file):
        extract_pdf_pages(pdf_file)
    else:
        print(f"ファイルが見つかりません: {pdf_file}")
        print(f"File not found: {pdf_file}")
