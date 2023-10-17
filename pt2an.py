def solve_eq(a1, b1, c1, a2, b2, c2):
  """
  Giải hệ phương trình 2 ẩn bằng phương pháp Cramer
  :param a1: hệ số x của phương trình thứ nhất
  :param b1: hệ số y của phương trình thứ nhất
  :param c1: hằng số của phương trình thứ nhất
  :param a2: hệ số x của phương trình thứ hai
  :param b2: hệ số y của phương trình thứ hai
  :param c2: hằng số của phương trình thứ hai
  :return: nghiệm của hệ phương trình
  """
  d = a1 * b2 - a2 * b1
  dx = c1 * b2 - c2 * b1
  dy = a1 * c2 - a2 * c1
  if d == 0:
    if dx + dy == 0:
      return "Phương trình có vô số nghiệm"
    else:
      return "Phương trình vô nghiệm"
  else:
    x = dx / d
    y = dy / d
    return x, y
