import fitz
import helper


def start_splitting(config_file_path):
    config_content = helper.read_config_file(config_file_path)
    
    doc = fitz.open("C:\\Users\\badhe\\Downloads\\127.pdf") # open document

    parsed_config = {}
    try:
        parsed_config = helper.parse_config(config_content)
        if not parsed_config.get("OCR"):
            print("No text configurations found")
    except ValueError as e:
        print(e)
    
    try:
        split_pdf(doc, parsed_config)
    except Exception as e:
        print(e)


def split_pdf(doc, parsed_config):
    title_visited = set()
    current_title = ""
    current_doc = fitz.open()
    for i, page in enumerate(doc):
        if not current_title:
            for config in parsed_config.get("OCR"): 
                title = config[0]
                location = config[1]
                if helper.get_ocr_title(page, title, location, helper.CONST_zoom_factor):
                    current_title = title
                    current_doc.insert_pdf(doc, from_page=i, to_page=i)
                    break

        else:
            for config in parsed_config.get("OCR"): 
                title = config[0]
                location = config[1]
                if helper.get_ocr_title(page, title, location, helper.CONST_zoom_factor):
                    if current_title != title:
                        if current_title not in title_visited: 
                            title_visited.add(current_title)
                            current_doc.save(f"{doc.name}_{current_title}.pdf")
                        else:
                            visited_doc = fitz.open(f"{doc.name}_{current_title}.pdf")
                            visited_doc.insert_pdf(current_doc)
                            visited_doc.saveIncr()
                            visited_doc.close()
                        
                        current_doc = fitz.open()
                        current_title = title
                        break
            
            current_doc.insert_pdf(doc, from_page=i, to_page=i)

    if current_title not in title_visited: 
        title_visited.add(current_title)
        current_doc.save(f"{doc.name}_{current_title}.pdf")
    else:
        visited_doc = fitz.open(f"{doc.name}_{current_title}.pdf")
        visited_doc.insert_pdf(current_doc)
        visited_doc.saveIncr()
        visited_doc.close()

    doc.close()