from jinja2 import Environment, FileSystemLoader, select_autoescape
import json
# from weasyprint import HTML
import pandoc
from pathlib import Path
import argparse
import pdb

def buildDocs_from_config(config):
    """Build the documents that are described in the configuration data."""
    outfmts = [".html",".pdf"]
    loader = FileSystemLoader("code/templates")
    env = Environment(loader=loader,autoescape=select_autoescape())
    for document in config:
        # pdb.set_trace()
        doctext = ""
        isTemplated = False
        for component in document["structure"]:
            cpath = Path(component)
            if (cpath.suffix in [".md",".markdown",".mdwn",".mdtext"]):
                # concatenate contents of file
                with open(cpath, encoding='utf8') as fp:
                    doctext += fp.read()
        if not document["useJinja"]:
            # pdb.set_trace()
            for fmt in outfmts:
                outname = "../output/"+document["output_name"]+fmt
                pandoc.write(pandoc.read(doctext), file=outname)  
        else:
            outname = "../output/"+document["output_name"]+".html"
            context = {"doc_title":document["output_name"],
            "doc_author":document["document_author"],
            "doc_date":document["document_modified_date"]}
            contents = []
            for item in document["definitions"]:
                cpath = Path(item["text"])
                with open(cpath, encoding='utf8') as fp:
                    importedtext =fp.read() 
                contents.append({"href":item["href"],"name":item["name"],"text":importedtext})
            context["contents"]=contents
            template = env.get_template(document["structure"])
            outputtext = template.render(context)
            pandoc.write(pandoc.read(outputtext),file=outname)
            
            

def read_config(filename):
    """Import a configuration file for documentation build."""
    with open(filename) as fp:
        config = json.load(fp)
    return config

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compile documentation versions.")
    parser.add_argument("config", metavar="C", type=str, help="configuration json that describes docs")
    args = parser.parse_args()
    config = read_config(args.config)
    buildDocs_from_config(config)