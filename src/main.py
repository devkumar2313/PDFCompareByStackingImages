import sys
import os
from getPDFImage import extract_pdf_pages  # Assuming this function exists
from ChangeImageColor import change_black_to_red
from changeImageColorForStacking import change_black_to_blue
from createDiffPDF import insert_png_create_diffpdf

def main():
    """
    Main console application to compare PDF files by stacking images.
    Usage: python main.py <pdf1_path> <pdf2_path> [output_path]
    """
    if len(sys.argv) < 3:
        print("使用方法: python main.py <PDF1のパス> <PDF2のパス> [出力PDFパス]")
        print("例: python main.py document1.pdf document2.pdf comparison_result.pdf")
        print("")
        print("Usage: python main.py <pdf1_path> <pdf2_path> [output_path]")
        print("Example: python main.py document1.pdf document2.pdf comparison_result.pdf")
        return

    pdf1_path = sys.argv[1]
    pdf2_path = sys.argv[2]
    output_path = sys.argv[3] if len(sys.argv) > 3 else "comparison_result.pdf"

    # Validate input files exist
    if not os.path.exists(pdf1_path):
        print(f"エラー: ファイルが見つかりません - {pdf1_path}")
        print(f"Error: File not found - {pdf1_path}")
        return

    if not os.path.exists(pdf2_path):
        print(f"エラー: ファイルが見つかりません - {pdf2_path}")
        print(f"Error: File not found - {pdf2_path}")
        return

    print(f"PDFファイルを比較しています:")
    print(f"ファイル1: {pdf1_path}")
    print(f"ファイル2: {pdf2_path}")
    print(f"出力先: {output_path}")
    print()
    print(f"Comparing PDF files:")
    print(f"File 1: {pdf1_path}")
    print(f"File 2: {pdf2_path}")
    print(f"Output: {output_path}")

    try:
        # Step 1: Extract pages from PDFs as images
        print("ステップ1: PDFからページを画像として抽出中...")
        print("Step 1: Extracting pages from PDFs as images...")
        
        # Assuming getPDFImage.py has a function to extract pages
        # You may need to modify this based on the actual implementation
        page1_image = "page_1.png"
        page2_image = "page_2.png"
        
        # Step 2: Change colors for comparison
        print("ステップ2: 比較用に画像の色を変更中...")
        print("Step 2: Changing image colors for comparison...")
        
        # Convert first PDF page to red
        page1_red = "page_1_red.png"
        change_black_to_red(page1_image, page1_red)
        
        # Convert second PDF page to blue with transparency
        page2_blue = "page_2_blue.png"
        change_black_to_blue(page2_image, page2_blue)
        
        # Step 3: Create comparison PDF
        print("ステップ3: 比較用PDFを作成中...")
        print("Step 3: Creating comparison PDF...")
        
        insert_position = (0, 0)
        insert_size = (500, 500)
        
        insert_png_create_diffpdf(
            png_path=page2_blue,      # 2階層目（青色、透過）
            png_path2=page1_red,      # 1階層目（赤色、ベース）
            output_pdf_path=output_path,
            position=insert_position,
            image_size=insert_size
        )
        
        print(f"比較完了! 結果は '{output_path}' に保存されました。")
        print(f"Comparison completed! Result saved to '{output_path}'.")
        
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
