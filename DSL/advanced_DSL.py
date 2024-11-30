# **일반**
# 조건들로 오브젝트 선택
# 두 오브젝트 색 바꾸기
def switch_color(grid, color1, color2):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == color1:
                grid[i][j] = color2
            elif grid[i][j] == color2:
                grid[i][j] = color1
    return grid

# 선택할 수 있는 요소 확장(픽셀 -> 픽셀, 격자 선, 격자 점, 전체 행, 전체 열)
# 중점 선택 기능 (홀*홀, 짝*홀, 홀*짝, 짝*짝 일 경우)
def center(object):
    return pixels

# 회전 (대상, 축이 되는 점, 방향, 횟수)
# object, direction, count, pivot
def rotate(object, direction, count, pivot):
    return grid

# 반전 (대상, 축이 되는 선, 점)
# object, pivot(line or point)
def flip(object, pivot):
    return grid

# 이동 (대상, 방향, 거리)
# object, direction, distance, target, condition
# 오브젝트의 특정 방향 특정 거리 이동 - move
# 오브젝트의 특정 방향 특정 지점까지 이동 - teleport
# 오브젝트의 특정 방향 특정 조건 형성시까지 이동 - move_until   
def move(object, direction, distance, target, condition):
    return grid


# 다픽셀 선택-합집합(점, 네모, 점들, 네모들, 점+네모 혼합)
def select(object, condition):
    return grid

# 다중영역중 일부를 선택해제 하는 기능-차집합

# 지정영역을 제외한 부분을 선택하는 기능-여집합 (특정 범위 내에서도)

def union(condition):
    return grid

def intersection(condition):
    return grid

def difference(condition):
    return grid

def complement(condition):
    return grid


# 다양한 함수를 하나의 함수로 지정하는 함수
def combination(*functions):
    def combined_function(*args, **kwargs):
        result = args[0]  # Assume the first argument is the initial state
        for func in functions:
            result = func(result, *args[1:], **kwargs)
        return result
    return combined_function


# 두 점으로 선 만들기 (한점, 두점, 끝 점포함 여부) (가로세로 대각선)
def make_line(grid, row1, col1, row2, col2, color, include_ends=True):
    dx = abs(col2 - col1)
    dy = abs(row2 - row1)
    sx = 1 if col1 < col2 else -1
    sy = 1 if row1 < row2 else -1
    err = dx - dy

    is_start = True
    while True:
        if include_ends or (not is_start and (row1 != row2 or col1 != col2)):
            grid[row1][col1] = color
        
        if row1 == row2 and col1 == col2:
            break

        is_start = False
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            col1 += sx
        if e2 < dx:
            err += dx
            row1 += sy

    return grid

# 한 점 방향으로 선 만들기 (한 점, 방향, 덮어쓰기, 얼마나)
def line(grid, init, final, direction, color, width, style):
    return grid

# 두 점으로 네모 만들기 (한 점, 두점, 테두리 포함 여부)
def rectangle(grid, init, final, color, include_edges=True):
    return grid

# 복사 후 다른 변형가능 차원에 보존
def copy(object):
    return grid

# 잘라내기
def crop(grid, point1, point2):
    return grid

# 복사 후 특수 붙여넣기 (색일치 지점에 붙여넣기) - lefttop이외의 지점사용
def paste(object, target):
    return grid

# 픽셀단위 and, or
def pixel_and(object1, object2):
    return grid

def pixel_or(object1, object2):
    return grid

# 확대 축소
def scale(object, scale):
    return grid

# 그리드 만들기
def make_grid(height, width, color):
    assert height <=30 and width <= 30
    assert height > 0 and width > 0
    grid = []
    for i in range(height):
        row = []
        for j in range(width):
            row.append(color)
        grid.append(row)
    return grid
    
# object paste on grid
def paste_object(grid, object, row, col):
    for i in range(len(object)):
        for j in range(len(object[0])):
            if object[i][j] != 12:
                grid[row+i][col+j] = object[i][j]
    return grid

# 그리드 자르기
def cut_grid(grid, row, col, height, width):
    new_grid = []
    for i in range(row, row+height):
        new_grid.append(grid[i][col:col+width])
    return new_grid

# 의미론적 매칭 (색, 그리드 구성)
# 의미론적 그리드 구성




# **특징**
# 개수
def count(object):
    return number

# 크기, 가로, 세로
def size(object):
    return number

# 색깔
def color(object):
    return color

# 색 종류 개수
def color_count(object):
    return number

# 픽셀간거리
def pixel_distance(object1, object2):
    return number

# 방향
def direction(object):
    return vector

# 순서
def order(object):
    return number

# 노이즈 여부
def noise(object):
    return boolean

# 닿아 있는 지 여부 (한물체, 두물체, 가로세로대각선)
def touch(object1, object2, diagonal = False):
    return boolean

# 물체의 대칭여부
def symmetry(object):
    return boolean

# 물체의 모서리, 꼭지점, 내부, 테두리 여부
def corner(object):
    return boolean

def edge(object):
    return boolean

def margin(object):
    return boolean

def inner(object):
    return boolean

# 모양일치, 부분일치, 닮음
# 사방이 막혀 있는지 (가로 세로 대각선)
def closed(object, diagonal = False):
    return boolean

# divider 여부
def divider(object):
    return boolean

# 영역의 개념
# 모양 (색다르지만 모양 같음)
# 테두리
# 행, 열의 구성

# **애매한 것**
# 초점 변수? (한번에 변환하는 문제가 아닌 따라가면서 만드는 문제)