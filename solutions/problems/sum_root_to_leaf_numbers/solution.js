var sumNumbers = function(root, subsum = 0) {
  let paths = getPaths(root);
  let sum = 0;
  paths.forEach(path => {
    sum += parseInt(path.join(""));
  });

  return sum;
};

var getPaths = function(root, currentPath = [], allPaths = []) {

  if (!root) {
    return [];
  }
  currentPath.push(root.val);

    
  if (!root.left && !root.right) {
    allPaths.push([...currentPath]);
    currentPath.pop();
    return allPaths;
  }

  getPaths(root.left, currentPath, allPaths);
  getPaths(root.right, currentPath, allPaths);
    currentPath.pop();

  return allPaths;
};