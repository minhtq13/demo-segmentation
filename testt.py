import base64
import io
import gc
import cv2
import PIL
import time
import numpy as np
import streamlit as st
from streamlit_drawable_canvas import st_canvas


corners = [[[96, 144]], [[652, 98]], [[688, 999]], [[47, 946]]]
corners = sorted(np.concatenate(corners).tolist())
print("corners", corners)