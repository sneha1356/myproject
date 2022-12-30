import tkinter as tk
from psutil import net_io_counters
KB=float(1024)
MB=float(KB**2)
GB=float(KB**3)
TB=float(KB**4)

def size(B):
    B=float(B)
    if B<KB:
        return f"{B} Bytes"
    elif KB<=B<MB:
        return f"{B/KB:.2f} KB"
    elif MB<=B<KB:
        return f"{B/MB:.2f} MB"
    elif GB<=B<MB:
        return f"{B/GB:.2f} GB"
    elif TB<=B<GB:
        return f"{B/TB:.2f} TB"
window_size=(400,400)
window_resizable=False
refresh_delay=1500
last_upload,last_download,upload_speed,down_speed=0,0,0,0
window=tk.Tk()
window.title("Network Bandwidth Monitor")
window.geometry(f"{window_size[0]}x{window_size[1]}")
window.resizable(wisth=window_resizable,height=window_resizable)
label_total_upload_header=tk.Label(text="total Uplaod",font="Quicksand 12 bold")
label_total_upload_header.pack()
label_total_upload=tk.Label(text="Calculating..",font="Quicksand 12")
label_total_download_header=tk.Label(text="total downlaod",font="Quicksand 12 bold")
label_total_download_header.pack()
label_total_download=tk.Label(text="Calculating..",font="Quicksand 12")
label_total_download.pack()
label_total_usage_header=tk.Label("Total Usage:",font="Quicksand 12")
label_total_usage_header.pack()
label_total_usage=tk.Label(text="Calculating..\n",font="Quciksand 12")
label_total_usage.pack()
label_upload_header=tk.Label(text="upload:",font="Quicksand 12")
label_upload_header.pack()
label_upload=tk.Label(text="Calculating..",font="Quicksand 12")
label_upload.pack()
label_download_header=tk.Label(text="Download:",font="")
label_download_header.pack()
label_download=tk.Label(text="Calculating..",font="Quicksand 12")
label_download.pack()
