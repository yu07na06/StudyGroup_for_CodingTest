function solution(new_id) {
  let str = new_id
    .toLowerCase()
    .replace(/[^\w\-\.]/g, "")
    .replace(/\.+/g, ".")
    .replace(/^\.|\.$/g, "")
    .replace(/^$/g, "a")
    .slice(0, 15)
    .replace(/\.$/g, "");

  let lastchar = str[str.length - 1];
  while (str.length <= 2) {
    str += lastchar;
  }

  return str;
}
