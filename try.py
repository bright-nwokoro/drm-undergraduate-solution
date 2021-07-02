from pyexiftool import exiftool
import json

files = ["legend.jpg", "toplegend.pdf", "06175801.jpeg", "Mastering Windows PowerShell Scripting  Automate and Manage Your Environment Using PowerShell Core 6. 0, 3rd Edition. by Chris Dent (z-lib.org).pdf"]
with exiftool.ExifTool() as et:
    metadata = et.get_metadata_batch(files)

def search(myDict, lookup):
    for key, value in myDict.items():
        if lookup in key:
            return key

for d in metadata:
    copy_right = search(d, 'Copyright')
    xmp_title = search(d, 'XMP:Title')
    xmp_create_date = search(d, 'XMP:CreateDate')
    file_create_date = search(d, 'File:FileCreateDate')
    usage_terms = search(d, 'UsageTerms')
    
    
    # print(copy_right)
    # print(d)
    if copy_right != None:
        if xmp_title != None:
            if xmp_create_date != None:
                if file_create_date != None:
                    if usage_terms != None:
                        print("{:20.20} {:20.20} {:20.20} {:20.20} {:20.20} {:20.20} {:20.20}".format(d["SourceFile"],
                                    d["File:FileTypeExtension"],
                                    d[xmp_title],
                                    d[xmp_create_date],
                                    d[file_create_date],
                                    d[usage_terms],
                                    d[copy_right],
                                    ))
                    else:
                        print("{:20.20} {:20.20} {:20.20} {:20.20} {:20.20} {:20.20}".format(d["SourceFile"],
                                    d["File:FileTypeExtension"],
                                    d[xmp_title],
                                    d[xmp_create_date],
                                    d[file_create_date],
                                    d[copy_right],
                                    ))
                elif usage_terms != None:
                    print("{:20.20} {:20.20} {:20.20} {:20.20} {:20.20} {:20.20}".format(d["SourceFile"],
                                    d["File:FileTypeExtension"],
                                    d[xmp_title],
                                    d[xmp_create_date],
                                    d[usage_terms],
                                    d[copy_right],
                                    ))
                else:
                    print("{:20.20} {:20.20} {:20.20} {:20.20} {:20.20}".format(d["SourceFile"],
                                    d["File:FileTypeExtension"],
                                    d[xmp_title],
                                    d[xmp_create_date],
                                    d[copy_right],
                                    ))
            elif file_create_date != None:
                if usage_terms != None:
                    print("{:20.20} {:20.20} {:20.20} {:20.20} {:20.20} {:20.20}".format(d["SourceFile"],
                                        d["File:FileTypeExtension"],
                                        d[xmp_title],
                                        d[file_create_date],
                                        d[usage_terms],
                                        d[copy_right],
                                        ))
                else:
                    print("{:20.20} {:20.20} {:20.20} {:20.20} {:20.20}".format(d["SourceFile"],
                                        d["File:FileTypeExtension"],
                                        d[xmp_title],
                                        d[file_create_date],
                                        d[copy_right],
                                        ))
                    
            elif usage_terms != None:
                print("{:20.20} {:20.20} {:20.20} {:20.20} {:20.20}".format(d["SourceFile"],
                                        d["File:FileTypeExtension"],
                                        d[xmp_title],
                                        d[usage_terms],
                                        d[copy_right],
                                        ))
            else:
                print("{:20.20} {:20.20} {:20.20} {:20.20}".format(d["SourceFile"],
                                        d["File:FileTypeExtension"],
                                        d[xmp_title],
                                        d[copy_right],
                                        ))      
        elif xmp_create_date != None:
            if file_create_date != None:
                if usage_terms != None:
                    print("{:20.20} {:20.20} {:20.20} {:20.20} {:20.20} {:20.20}".format(d["SourceFile"],
                                d["File:FileTypeExtension"],
                                d[xmp_create_date],
                                d[file_create_date],
                                d[usage_terms],
                                d[copy_right],
                                ))                   
            elif usage_terms != None:
                print("{:20.20} {:20.20} {:20.20} {:20.20} {:20.20}".format(d["SourceFile"],
                                d["File:FileTypeExtension"],
                                d[xmp_create_date],
                                d[usage_terms],
                                d[copy_right],
                                ))
            else:
                print("{:20.20} {:20.20} {:20.20} {:20.20}".format(d["SourceFile"],
                                        d["File:FileTypeExtension"],
                                        d[xmp_title],
                                        d[copy_right],
                                        ))        
        elif file_create_date != None:
            if usage_terms != None:
                print("{:20.20} {:20.20} {:20.20} {:20.20} {:20.20}".format(d["SourceFile"],
                            d["File:FileTypeExtension"],
                            d[file_create_date],
                            d[usage_terms],
                            d[copy_right],
                            ))
            else:
                print("{:20.20} {:20.20} {:20.20} {:20.20}".format(d["SourceFile"],
                            d["File:FileTypeExtension"],
                            d[file_create_date],
                            d[copy_right],
                            ))
        elif usage_terms != None:
            print("{:20.20} {:20.20} {:20.20} {:20.20}".format(d["SourceFile"],
                        d["File:FileTypeExtension"],
                        d[usage_terms],
                        d[copy_right],
                        ))
        else:
            print("{:20.20} {:20.20} {:20.20}".format(d["SourceFile"],
                        d["File:FileTypeExtension"],
                        d[copy_right],
                        ))
    else:
        None                
    