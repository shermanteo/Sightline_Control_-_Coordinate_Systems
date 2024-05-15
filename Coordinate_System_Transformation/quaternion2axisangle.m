function [x, y, z] =  quaternion2axisangle (q0, q1, q2, q3)
% Description: Converting the quaternion to axis angles
% A quaternion is represented by four elements: q0+iq1+jq2+kq3, where q0, 
% q1, q2 and q3 are real numbers, and i, j and k are mutually orthogonal 
% imaginary unit vectors
%
% Input parameters
% q0 = q0 term is referred to as the "real" component
% q1 = q1 term is referred to as the "imaginary" component
% q2 = q2 term is referred to as the "imaginary" component
% q3 = q3 term is referred to as the "imaginary" component
%
% Output Parameters
% Axis-Angle representation.
% There is one special case in which the equation will fail. 
% A quaternion with the value q = (1,0,0,0) is known as the identity 
% quaternion, and will produce no rotation. In this case, it will produce 
% a rotation angle (θ) of zero, which is what we expect. However, since the
% axis of rotation is undefined when there is no rotation, the equation 
% will generate a divide-by-zero error. Any software implementation should 
% therefore test whether q0 equals 1.0, and if it does should set θ = 0, 
% and (x̂, ŷ, ẑ) = (1, 0, 0).

theta = 2*acos(q0);

if theta = 0
  x = 1;
  y = 0;
  z = 0;
else
  x = q1/sin(theta/2);
  y = q2/sin(theta/2);
  z = q3/sin(theta/2);
