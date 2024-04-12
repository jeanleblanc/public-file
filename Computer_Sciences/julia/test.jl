using Plots
using PlotThemes
using DifferentialEquations
# Define the differential equation as an anonymous function
dxdt = (t, x) -> x^2 - t

# Generate a mesh for the t and x values
t_vals = range(-2, stop=10, length=25)
x_vals = range(-4, stop=4, length=25)

# Create a plot for the direction field
field_plot = plot(title="Direction Field for x' = x^2 - t", xlabel="t", ylabel="x", 
                  xlims=(-2, 10), ylims=(-4, 4), legend=false)

# Add the direction field to the plot
    for x in x_vals
        # Calculate the slope of the field
        slope = dxdt(t, x)
        # Adjust the length of the arrow for visualization
        len = 0.1 / (1 + abs(slope))
        plot!([t, t + len], [x, x + slope * len], arrow=true, color=:black, lw=0.5)
    end
end

# Solve and plot a few trajectories with different initial conditions
initial_conditions = [-3, -1.5, 0, 1.5, 3]
for x0 in initial_conditions
    # Define the ODE problem
    prob = ODEProblem(dxdt, x0, (t_vals.start, t_vals.stop))
    # Solve the problem
    sol = solve(prob, Tsit5(), reltol=1e-8, abstol=1e-8)
    # Plot the solution trajectory
    plot!(sol, vars=(0, 1), lw=2, label="")
end

# Display the direction field and trajectories
display(field_plot)
