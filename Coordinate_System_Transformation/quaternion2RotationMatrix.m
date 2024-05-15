function R =  quaternion2RotationMatrix (q0, q1, q2, q3)
% Description: Converting the quaternions to a rotation matrix
% A quaternion is represented by four elements: q0+iq1+jq2+kq3, where q0, 
% q1, q2 and q3 are real numbers, and i, j and k are mutually orthogonal 
% imaginary unit vectors
%
% Input Parameters
% q0 = q0 term is referred to as the "real" component
% q1 = q1 term is referred to as the "imaginary" component
% q2 = q2 term is referred to as the "imaginary" component
% q3 = q3 term is referred to as the "imaginary" component
%
% Output Parameters
% Rotation Matrix generated from quaternions which work for all valid 
% rotation quaternions, including identity quaternion.
%

R = [q0^2+q1^2-q2^2-q3^2 2*q1*q2-2*q0*q3 2*q1*q3+2*q0*q2; ...
     2*q1*q2+2*q0*q3 q0^2-q1^2+q2^2-q3^2 2*q2*q3-2*q0*q1; ...
     2*q1*q3-2*q0*q2 2*q2*q3+2*q0*q1 q0^2-q1^2-q2^2+q3^2];
